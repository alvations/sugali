# -*- coding: utf-8 -*-
from __future__ import division
import sys; sys.path.append('../') # Access modules from parent dir.
from math import sqrt

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

def tfidfize(_featureset):
  """
  Convert frequencies to tf-idf.
  """
  from collections import defaultdict
  import math
  fs = defaultdict(dict) 
  for lang in _featureset:
    for gram in _featureset[lang]:
      fs[lang][gram] /= len([i for i in _featureset if gram in _featureset[i]])
  return fs

def dot_product(featureset, sentfeat):
  """
  Calculates the dot product of a sentence's features with the feature weights
  for each each language.
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

def evaluator(data_source, option="all", model="cosine", tfidf=False, with_word_boundary=True, seed=0):
  """
  Segments the data into 90-10 portions using tenfold(), 
  then trains a model using 90% of the data and evaluates on the remaining 10%.
  """
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG
  from extractfeature import sentence2ngrams
  from collections import defaultdict, Counter
  from multinomialnaivebayes import SGT
  from time import time
  
  ### Choose the function that will be called when identifying a sentence
  if model == "cosine":
    identify = dot_product  # The sentence feature vectors will not be normalised, to save time. This does not affect classification.
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
    #print len(train), len(test)
    ### Extract the features
    featureset = defaultdict(Counter)
    for lang, trainsent in train:
      #print lang, trainsent
      if lang in ISO2LANG or lang in MACRO2LANG:
        trainsentcount = Counter(sentence2ngrams(trainsent, option=option, with_word_boundary=with_word_boundary))
        if len(trainsentcount) > 0:
          featureset[lang].update(trainsentcount)
    
    if tfidf:
      print "Calculating tf-idf..."
      featureset = tfidfize(featureset)
    
    if model == "cosine":
      print "Normalising to unit length..."
      for lang in featureset:
        norm = sqrt(sum([x**2 for x in featureset[lang].values()]))
        for feat in featureset[lang]:
          featureset[lang][feat] /= norm
    
    print "Evaluating..."
    fold_results = Counter()  # Records the number of times the correct language is at a specific rank 
    macro_true = defaultdict(int)  # These three are to calculate precision, recall, and f-score for each language
    macro_fpos = defaultdict(int)
    macro_fneg = defaultdict(int) 
    
    ### Identify each sentence in the test data
    for lang, testsent in test:
      ### Extract features
      sentfeat = Counter(sentence2ngrams(testsent, option=option, with_word_boundary=with_word_boundary))
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

evaluator('omniglot', option='all', model='cosine', tfidf=False, with_word_boundary=True, seed=0)