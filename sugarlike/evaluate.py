# -*- coding: utf-8 -*-
import sys; sys.path.append('../') # Access modules from parent dir.

def tenfold(data_source, randseed=0):
  """ Randomly split data in 90-10 portions. """
  import random, sys
  from extractfeature import get_features, sentence2ngrams
  from universalcorpus import odin, omniglot, udhr
  random.seed(randseed)
  corpus = list(locals()[data_source].source_sents())
  corpus = sorted(iter(corpus), key=lambda k: random.random())
  totrain = int(len(corpus)/10)
  
  for i in range(1,10):
    ##print i*totrain
    yield corpus[:(i-1)*totrain] + corpus[i*totrain:], \
          corpus[(i-1)*totrain:i*totrain] # yield train, test

def featurize(text, all_features, option="3gram"):
  """ Inputs a sentence string and outputs the np.array() """
  import numpy as np
  from collections import Counter
  from extractfeature import sentence2ngrams
  return np.array([Counter(sentence2ngrams(text, option=option))[j] \
                   for j in all_features])

def features2numpy(featureset):
  """ Converts a feature counter in numpy arrays. """  
  from itertools import chain
  import numpy as np
  all_features = list(set(chain(*[i.keys() for i in featureset.values()])))
  all_tags = [i for i in featureset]
  data, target = [], []
  for lang in featureset:
    data.append([featureset[lang][j] if j in featureset[lang] else 0 \
                 for j in all_features])
    target.append(lang)
  return np.array(data), np.array(target), all_features
 
def tfidfize(_featureset):
  from collections import defaultdict, Counter
  import math
  featureset = defaultdict(Counter)
  for lang in _featureset:
    for gram in _featureset[lang]:
      tf = _featureset[lang][gram] / float(sum(_featureset[lang].values()))
      idf = math.log(len(_featureset)) / len([i for i in _featureset if gram in _featureset[i]])
      featureset[lang][gram] = tf * idf
  return featureset
 
def evaluator(data_source, option, smoothing=0.00001):
  """
  Segments the data into 90-10 portions using tenfold(), 
  then trains a model using 90% of the data and evaluated the remaining 10%.
  """
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG
  from extractfeature import sentence2ngrams
  from collections import defaultdict, Counter
  
  from multinomialnaivebayes import SGT
  import time
  
  fold_counter = 0
  ten_fold_accuracies = []
  ten_fold_mrr = []
  ten_fold_mrrpos = []
  for fold in tenfold(data_source):
    start = time.time()
    fold_counter+=1
    train, test = fold
    #print len(train), len(test)
    # Extracts the features.
    featureset = defaultdict(Counter)
    for lang, trainsent in train:
      if lang in ISO2LANG or lang in MACRO2LANG:
        _tempcounter = Counter(sentence2ngrams(trainsent, option=option))
        if len(_tempcounter) > 0:
          featureset[lang] = _tempcounter
    
    '''# Trains the model and test using langid.py
    featureset, tags, allfeatures = features2numpy(tfidfize(featureset)) 
    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB(alpha=0.01)   
    for lang, testsent in test:
      guess = mnb.fit(featureset, tags).predict_proba(featurize(testsent, allfeatures, option=option))
      best = sorted(zip(guess.tolist()[0], tags), reverse=True)[0]
      print lang, sorted(zip(guess.tolist()[0], tags), reverse=True)[0], lang == best[1] # testsent
    '''
    # Trains the model and test using NLTK MNB
    x = featureset
    fold_results = Counter() # for accuracy calculation
    rr = [] # Mean Reciprocal Rank, top 10.
    print "Calculating Fold", fold_counter, ", please wait patiently..."
    for lang, testsent in test:
      sgt_results = []
      testsent = Counter(sentence2ngrams(testsent))
      for flang in x:
        train = featureset[flang]
        ##print train
        sgt = SGT(train)
        sgt_results.append((sgt.estimate(testsent),flang))
      best = sorted(sgt_results, reverse=True)[0]
      ##print lang, sorted(sgt_results, reverse=True)[:3], lang == best[1]
      fold_results[lang == best[1]]+=1
      top10 = [i[1] for i in sorted(sgt_results, reverse=True)[:10]]
      if lang in top10:
        ##print 1/float(top10.index(lang)+1)
        rr.append(1/float(top10.index(lang)+1))
      else:
        rr.append(0)
    
    accuracy = fold_results[True] / float(sum(fold_results.values()))
    print "Accuracy:", "%0.6f" % (accuracy*100), "%"
    ten_fold_accuracies.append(accuracy)
    
    mrr = sum(rr)/len(rr)
    print "Mean Reciprocal Rank:", "%0.6f" % mrr
    ten_fold_mrr.append(mrr)
    
    rrpos = [i for i in rr if i != 0] # Only counts results in top10
    mrrpos = sum(rrpos)/len(rrpos)
    print "Mean Reciprocal Rank (only positive):", \
          "%0.4f" % mrrpos 
    ten_fold_mrrpos.append(mrrpos)
    
    end = time.time() - start
    print str(end), "seconds to evaluation Fold-"+ str(fold_counter), \
          ", evaluated", str(sum(fold_results.values())), "test sentences"
    print
  
  print "=============================================="
  print "Ten-fold Accuracies:", ten_fold_accuracies
  print "Average ten-fold accuracies:", "%0.6f"% (sum(ten_fold_accuracies)/float(10))
  print
  print "Ten-fold MRRs:", ten_fold_mrr
  print "Average ten-fold MRR:", "%0.6f"%(sum(ten_fold_mrr)/float(10))
  print
  print "Ten-fold MRRs (only in top10):", ten_fold_mrrpos
  print "Average ten-fold MRR (only in top10):", \
        "%0.6f"%(sum(ten_fold_mrrpos)/float(10))
  
  

evaluator('omniglot','char')
#evaluator(1,2)