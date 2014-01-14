# -*- coding: utf-8 -*-

from extractfeature import get_features, sentence2ngrams
from itertools import chain
import numpy as np
from collections import Counter

def features2numpy(data_source, option="3gram"):
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

def featurize(text, all_features, option="3gram"):
  """ Inputs a sentence string and outputs the np.array() """
  return np.array([Counter(sentence2ngrams(text, option=option))[j] \
                   for j in all_features])

def sugarlid_nb(text, nbc='mnb',option="3gram"):
  """ Generic Naive Bayes sugarlid. """
  featureset, tags, allfeatures = features2numpy('udhr',option=option)
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
  
def sugarlid_mnb(text, option='3grams'):
  """ Ducktype for Multinomial Naive Bayes sugarlid. """
  return sugarlid_nb(text,'mnb', option=option)
  
def sugarlid_gnb(text, option='3gram'):
  """ Ducktype for Gaussian Naive Bayes sugarlid. """
  return sugarlid_nb(text,'gnb', option=option)

def sugarlid_bnb(text, option='3gram'):
  """ Ducktype for Bernoulli Naive Bayes sugarlid. """
  return sugarlid_nb(text,'bnb', option=option)
  
def sugarlid_cosine(text, option='3gram'):
  """ Cosine Vector based sugarlid. """
  from cosine import cosine_similarity
  char_ngrams = get_features('udhr', option=option)
  ##for i in char_ngrams:
  ##  print char_ngrams[i]
  try:
    query_vector = " ".join(sentence2ngrams(text, option=option))
  except TypeError:
    query_vector = " ".join(["_".join(i) for i in \
                             sentence2ngrams(text, n=2, option=option)])
    print query_vector
  results = []
  for i in char_ngrams:
    lang_vector = " ".join([str(j+" ")*char_ngrams[i][j] \
                            for j in char_ngrams[i]])
    score = cosine_similarity(query_vector, lang_vector)
    if score > 0:
      results.append((score,i))
  return sorted(results, reverse=True)
  
t = 'ich bin schwanger'
#print sugarlid_mnb(t, option='2gram')[:10]
#print sugarlid_gnb(t, option='2gram')[:10]
#print sugarlid_bnb(t, option='2gram')[:10]
print sugarlid_cosine(t, option='word')[:10]