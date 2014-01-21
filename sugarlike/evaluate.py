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
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG
  from extractfeature import sentence2ngrams
  from collections import defaultdict, Counter
  
  from multinomialnaivebayes import SGTestimate, SGT, MLEestimate, MLE
  
  for fold in tenfold(data_source):
    train, test = fold
    #print len(train), len(test)
    # Extracts the features.
    featureset = defaultdict(Counter)
    for lang, trainsent in train:
      if lang in ISO2LANG or lang in MACRO2LANG:
        _tempcounter = Counter(sentence2ngrams(trainsent, option=option))
        if len(_tempcounter) > 0:
          featureset[lang] = _tempcounter
    '''
    # Trains the model and test using langid.py
    featureset, tags, allfeatures = features2numpy(tfidfize(featureset)) 
    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB(alpha=0.00000000001)   
    for lang, testsent in test:
      guess = mnb.fit(featureset, tags).predict_proba(featurize(testsent, allfeatures, option=option))
      print lang, sorted(zip(guess.tolist()[0], tags), reverse=True)[0], testsent
    '''
    # Trains the model and test using NLTK MNB
    
    x = featureset
    for lang, testsent in test:
      sgt_results = []
      testsent = Counter(sentence2ngrams(testsent))
      for flang in x:
        train = featureset[flang]
        ##print train
        sgt = SGT(train, min=3000)
        sgt_results.append((SGTestimate(sgt, testsent),flang))
      best = sorted(sgt_results, reverse=True)[0]
      print lang, sorted(sgt_results, reverse=True)[0], lang == best[1]
      
    
      
  
evaluator('udhr','char')
#evaluator(1,2)
