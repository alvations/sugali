# -*- coding: utf-8 -*-
from __future__ import division
import sys; sys.path.append('../') # Access modules from parent dir.
from math import sqrt
from collections import Counter

def tenfold(data_source, randseed=0):
  """
  Randomly split data in 90-10 portions.
  randseed can be used for different random partitions.
  """
  import random, sys
  from extractfeature import get_features, sentence2ngrams
  from universalcorpus import odin, omniglot, udhr
  random.seed(randseed)
  corpus = list(locals()[data_source].source_sents())
  corpus = sorted(iter(corpus), key=lambda k: random.random())
  totrain = len(corpus)/10
  
  for i in range(1,11):
    ##print i*totrain
    yield corpus[:int((i-1)*totrain)] + corpus[int(i*totrain):], \
          corpus[int((i-1)*totrain):int(i*totrain)] # yield train, test

def tfidfize(featureset):
  """
  Convert frequencies to tf-idf.
  """
  from collections import defaultdict
  import math.log
  fs = defaultdict(dict) 
  for lang in featureset:
    for gram in featureset[lang]:
      fs[lang][gram] /= log(len([i for i in featureset if gram in featureset[i]]))
  return fs

class MultiCounter(list):
  """
  Six counters combined (to record words and 1-5 grams)
  """
  def __init__(self, data=["","","","","",""]):
    for x in data:
      self.append(Counter(x))
  
  def update(self, data):
    i = 0
    for x in data:
      self[i].update(x)
      i += 1
  
  def __len__(self):
    return sum([len(x) for x in self])

def normalise(featurevector, length=1):
  """
  Normalises a feature vector to a specific length.
  Zero vectors are left zero.
  """
  try:
    norm = length / sqrt(sum([x**2 for x in featurevector.values()]))
  except ZeroDivisionError:
    return
  for feat in featurevector:
    featurevector[feat] *= norm

def dot_product(featureset, sentfeat):
  """
  Calculates the dot product of a sentence's features with the feature weights
  for each language.
  """
  results = []
  for langcode in featureset:
    langfeat = featureset[langcode]
    dotprod = 0
    for x in sentfeat:
      if x in langfeat:
        dotprod += sentfeat[x] * langfeat[x]
    results.append((dotprod, langcode))
  return results

def combined_dp(featureset, sentfeat):
  """
  Calculates the dot product of a sentence's features with the feature weights
  for each language, when there are different sets of features.
  """
  results = []
  for langcode in featureset:
    langfeat = featureset[langcode]
    dotprod = 0
    for i in range(6):
      for x in sentfeat[i]:
        if x in langfeat[i]:
          dotprod += sentfeat[i][x] * langfeat[i][x]
    results.append((dotprod, langcode))
  return results

def sum_cosine(featureset, sentfeat):
  """
  Sums the cosines between a sentence's features and each set of feature weights,
  for each language.
  """
  for x in sentfeat:
    normalise(x)
  return combined_dp(featureset, sentfeat)

def evaluator(data_source, option="all", model="cosine", tfidf=False, with_word_boundary=True, seed=0, warnings=False, weight=None):
  """
  Segments the data into 90-10 portions using tenfold(), 
  then trains a model using 90% of the data and evaluates on the remaining 10%.
  """
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG
  from extractfeature import sentence2ngrams
  from collections import defaultdict, Counter
  from multinomialnaivebayes import SGT
  from time import time
  
  ### Choose the data structure to record features, and the function that will be called when identifying a sentence
  if model == "cosine":
    DataStr = Counter
    identify = dot_product  # The sentence feature vectors will not be normalised, to save time. This does not affect classification.
  
  elif model == "cosine-combined":
    DataStr = MultiCounter
    identify = sum_cosine
    option = "separate"
    if not weight:
      weight = [1,1,1,1,1,1]
    
  else:
    print "Sorry, the model '{}' isn't available!".format(model)
    return None
  
  ### Get ready to record these statistics
  ten_fold_accuracy = []
  ten_fold_mrr = []
  ten_fold_precision = []
  ten_fold_recall = []
  ten_fold_fscore = []
  
  fold_counter = 0
  
  ### Set up the tenfold cross-validation, then evaluate on each fold 
  for train, test in tenfold(data_source, randseed=seed):
    fold_counter += 1
    print "Loading fold {}...".format(fold_counter)
    start = time()
    
    ### Extract the features
    featureset = defaultdict(DataStr)
    for lang, trainsent in train:
      if lang in ISO2LANG or lang in MACRO2LANG:
        trainsentcount = DataStr(sentence2ngrams(trainsent, option=option, with_word_boundary=with_word_boundary))
        if len(trainsentcount) > 0:
          featureset[lang].update(trainsentcount)
        elif warnings:
          print("*** No features for: {}".format(trainsent))
      elif warnings:
        print("*** {} not recognised!".format(lang))
    
    ### Process the features to produce weights
    if model == "cosine":
      print "Normalising to unit length..."
      for lang in featureset:
        normalise(featureset[lang])
      if tfidf:
        print "Calculating tf-idf..."
        featureset = tfidfize(featureset)
    
    elif model == "cosine-combined":
      print "Normalising and re-weighting components..."
      for lang in featureset:
        for i in range(6):
          normalise(featureset[lang][i], weight[i])
    
    print "Evaluating..."
    fold_results = Counter()  # Records the number of times the correct language is at a specific rank 
    macro_true = defaultdict(int)  # These three are to calculate precision, recall, and f-score for each language
    macro_fpos = defaultdict(int)
    macro_fneg = defaultdict(int)
    
    ### Identify each sentence in the test data
    for lang, testsent in test:
      ### Extract features
      sentfeat = DataStr(sentence2ngrams(testsent, option=option, with_word_boundary=with_word_boundary))
      if len(sentfeat) == 0:
        print "*** No features for: {}".format(testsent)
        continue
      
      ### Predict the language
      results = identify(featureset, sentfeat)
      result_list = [code for score, code in sorted(results, reverse=True)]
      try:
        rank = result_list.index(lang) + 1  # Compare the prediction with the answer
      except ValueError:  # If the language was not seen in training
        rank = float('inf')
      #print rank
      
      ### Note the result
      fold_results[rank] += 1
      if rank == 1:
        macro_true[lang] += 1
      else:
        macro_fneg[lang] += 1
        macro_fpos[result_list[0]] += 1
    
    ### Calculate statistics for this fold
    accuracy = fold_results[1] / sum(fold_results.values())
    print "Accuracy: {}".format(accuracy)
    ten_fold_accuracy.append(accuracy)
    
    mrr = sum([count/rank for rank, count in fold_results.items()]) / sum(fold_results.values())
    print "Mean Reciprocal Rank: {}".format(mrr)
    ten_fold_mrr.append(mrr)
    
    langset = set(macro_true.keys()) & set(macro_fpos.keys()) & set(macro_fneg.keys()) 
    precision = {lang : macro_true[lang] / (macro_true[lang] + macro_fpos[lang]) for lang in langset}
    recall = {lang : macro_true[lang] / (macro_true[lang] + macro_fneg[lang]) for lang in langset}
    fscore = {lang : 2*precision[lang]*recall[lang]/(precision[lang]+recall[lang]) for lang in langset}
    
    average_precision = sum(precision.values()) / len(langset)
    average_recall = sum(recall.values()) / len(langset)
    average_fscore = sum(fscore.values()) / len(langset)
    
    print "Macro precision: {}".format(average_precision)
    print "Macro recall: {}".format(average_recall)
    print "Macro f-score: {}".format(average_fscore)
    
    ten_fold_precision.append(average_precision)
    ten_fold_recall.append(average_recall)
    ten_fold_fscore.append(average_fscore)
    
    end = time() - start
    print "{} seconds to evaluate {} sentences in fold {}\n".format(end, sum(fold_results.values()), fold_counter)
  
  ### Average over all folds
  overall_accuracy = sum(ten_fold_accuracy)/10
  overall_mrr = sum(ten_fold_mrr)/10
  overall_precision = sum(ten_fold_precision)/10
  overall_recall = sum(ten_fold_recall)/10
  overall_fscore = sum(ten_fold_fscore)/10
  
  print "=============================================="
  print "Average accuracy: {}".format(overall_accuracy)
  print "Average MRR: {}".format(overall_mrr)
  print "Average macro precision: {}".format(overall_precision)
  print "Average macro recall: {}".format(overall_recall)
  print "Average macro f-score: {}".format(overall_fscore)
  
  return (overall_accuracy, overall_mrr, overall_precision, overall_recall, overall_fscore)

if __name__ == "__main__":
  evaluator('odin', model='cosine-combined', with_word_boundary=True, weight=[3,1,2,3,4,5], seed=7)