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
    data.append([featureset[lang][j] for j in all_features])
    target.append(lang)
    # Sanity check
    ##print [(j,featureset[lang][j]) for j in all_features if featureset[lang][j] > 0]
  return np.array(data), np.array(target), all_features

def featurize(text, all_features):
  """ Inputs a sentence string and outputs the np.array() """
  return np.array([Counter(sentence2ngrams(text))[j] for j in all_features])

def sugarlid_nb(text, nbc='mnb'):
  """ Generic Naive Bayes sugarlid. """
  featureset, tags, allfeatures = features2numpy('udhr')
  if nbc == "mnb":
    from sklearn.naive_bayes import MultinomialNB
    nb = MultinomialNB()
  elif nbc == "gnb":
    from sklearn.naive_bayes import GaussianNB
    nb = GaussianNB()
  elif nbc == 'bnb':
    from sklearn.naive_bayes import BernoulliNB
    nb = BernoulliNB()
  guess = nb.fit(featureset, tags).predict_proba(featurize(text, allfeatures))
  
  return sorted(zip(guess.tolist()[0], tags), reverse=True)
  
def sugarlid_mnb(text):
  """ Ducktype for Multinomial Naive Bayes sugarlid. """
  return sugarlid_nb(text,'mnb')
  
def sugarlid_gnb(text):
  """ Ducktype for Gaussian Naive Bayes sugarlid. """
  return sugarlid_nb(text,'gnb')

def sugarlid_bnb(text):
  """ Ducktype for Bernoulli Naive Bayes sugarlid. """
  return sugarlid_nb(text,'bnb')
  
def sugarlid_cosine(text):
  """ Cosine Vector based sugarlid. """
  from cosine import cosine_similarity
  char_ngrams = get_features('udhr', option='char')
  query_vector = " ".join(sentence2ngrams(text))
  results = []
  for i in char_ngrams:
    lang_vector = " ".join([str(j+" ")*char_ngrams[i][j] \
                            for j in char_ngrams[i]])
    score = cosine_similarity(query_vector, lang_vector)
    if score > 0:
      results.append((score,i))
  return sorted(results, reverse=True)
  
t = 'ich bin schwanger'
print sugarlid_mnb(t)[:10]
print sugarlid_gnb(t)[:10]
print sugarlid_bnb(t)[:10]
print sugarlid_cosine(t)[:10]