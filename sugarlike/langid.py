# -*- coding: utf-8 -*-

from extractfeature import get_features, sentence2ngrams
from itertools import chain
import numpy as np
from collections import Counter

def features2numpy(data_source, option="char"):
  featureset = get_features(data_source, option=option)
  all_features = list(set(chain(*[i.keys() for i in featureset.values()])))
  all_tags = [i for i in featureset]
  data, target = [], []
  for lang in featureset:
    data.append([featureset[i][j] for j in all_features])
    target.append(lang)
    # Sanity check
    #print [(j,character_ngrams[i][j]) for j in all_features if character_ngrams[i][j] > 0]
  return np.array(data), np.array(target), all_features

def featurize(text, all_features):
  """ Inputs a sentence string and outputs the np.array() """
  return np.array([Counter(sentence2ngrams(text))[j] for j in all_features])

def sugarlid(text):
  from sklearn.naive_bayes import MultinomialNB
  featureset, tags, allfeatures = features2numpy('odin')
  mnb = MultinomialNB()
  guess = mnb.fit(featureset, tags).predict_proba(featurize(text, allfeatures))
  print guess
  
  
t = 'ich bin schwanger'
sugarlid(t)