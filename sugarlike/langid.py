# -*- coding: utf-8 -*-

from extractfeature import get_features, sentence2ngrams
from itertools import chain
import numpy as np
from collections import Counter

def features2numpy(data_source, option="3gram", tfidf=False):
  if tfidf:
    featureset = tfidfize(data_source, option=option)
  else:
    featureset = get_features(data_source, option=option)
  
  all_features = list(set(chain(*[i.keys() for i in featureset.values()])))
  all_tags = [i for i in featureset]
  data, target = [], []
  for lang in featureset:
    data.append([featureset[lang][j] if j in featureset[lang] else 0 for j in all_features])
    target.append(lang)
    # Sanity check
    ##print [(j,featureset[lang][j]) for j in all_features if featureset[lang][j] > 0]
  return np.array(data), np.array(target), all_features

def tfidfize(data_source, option='3gram'):
  # see http://timtrueman.com/a-quick-foray-into-linear-algebra-and-python-tf-idf/
  # see http://scikit-learn.org/stable/modules/preprocessing.html
  from collections import defaultdict
  import math, os, io
  import cPickle as pickle

  tfidf_pickle = ''.join([data_source,'-',option,'-tfidf','.pk'])

  if os.path.exists(tfidf_pickle):
    with io.open(tfidf_pickle,'rb') as fin:
      featureset = pickle.load(fin)
  else:
    featureset = defaultdict(dict)
    _featureset = get_features(data_source, option=option)
    
    for lang in _featureset:
      for gram in _featureset[lang]:
        tf = _featureset[lang][gram] / float(sum(_featureset[lang].values()))
        idf = math.log(len(_featureset)) / len([i for i in _featureset if gram in _featureset[i]])
        featureset[lang][gram] = tf * idf
        print 'Calculating TF-IDF for %s please wait patiently...' % data_source
        print lang, gram, _featureset[lang][gram], tf, idf, tf * idf
        
    with io.open(tfidf_pickle,'wb') as fout:
      pickle.dump(featureset, fout)
    
  return featureset

def featurize(text, all_features, option="3gram"):
  """ Inputs a sentence string and outputs the np.array() """
  return np.array([Counter(sentence2ngrams(text, option=option))[j] \
                   for j in all_features])

def sugarlid_nb(text, nbc='mnb',option="3gram", data_source='crubadan',
                smoothing=1.0, tfidf=False):
  """ Generic Naive Bayes sugarlid. """
  featureset, tags, allfeatures = features2numpy(data_source,option=option,
                                                 tfidf=tfidf)
  if nbc == "mnb":
    from sklearn.naive_bayes import MultinomialNB
    nb = MultinomialNB(alpha=smoothing)
  elif nbc == "gnb":
    from sklearn.naive_bayes import GaussianNB
    nb = GaussianNB(alpha=smoothing)
  elif nbc == 'bnb':
    from sklearn.naive_bayes import BernoulliNB
    nb = BernoulliNB(alpha=smoothing)
  guess = nb.fit(featureset, tags).predict_proba(featurize(text, allfeatures))
  return sorted(zip(guess.tolist()[0], tags), reverse=True)
  
def sugarlid_mnb(text, option='3grams', data_source='crubadan', 
                 smoothing=1.0, tfidf=False):
  """ Ducktype for Multinomial Naive Bayes sugarlid. """
  return sugarlid_nb(text,'mnb', option=option, data_source=data_source,
                     smoothing=smoothing, tfidf=tfidf)
  
def sugarlid_gnb(text, option='3gram', data_source='crubadan',
                 smoothing=1.0, tfidf=False):
  """ Ducktype for Gaussian Naive Bayes sugarlid. """
  return sugarlid_nb(text,'gnb', option=option, data_source=data_source,
                     smoothing=smoothing, tfidf=tfidf)

def sugarlid_bnb(text, option='3gram', data_source='crubadan',
                 smoothing=1.0, tfidf=False):
  """ Ducktype for Bernoulli Naive Bayes sugarlid. """
  return sugarlid_nb(text,'bnb', option=option, data_source=data_source,
                     smoothing=smoothing, tfidf=tfidf)
  
def sugarlid_cosine(text, option='3gram', data_source='crubadan'):
  """ Cosine Vector based sugarlid. """
  from cosine import cosine_similarity
  char_ngrams = get_features(data_source, option=option)
  ##for i in char_ngrams:
  ##  print char_ngrams[i]
  #print sentence2ngrams(text, option=option)
  try:
    query_vector = " ".join(sentence2ngrams(text, option=option))
  except TypeError:
    query_vector = " ".join(["_".join(i) for i in \
                             sentence2ngrams(text, option=option)])
    print query_vector
  results = []
  for i in char_ngrams:
    lang_vector = " ".join([str(j+" ")*char_ngrams[i][j] \
                            for j in char_ngrams[i]])
    score = cosine_similarity(query_vector, lang_vector)
    if score > 0:
      results.append((score,i))
  return sorted(results, reverse=True)
  

from universalcorpus.miniethnologue import ISO2LANG
t = 'ich bin schwanger'
#print sugarlid_mnb(t, option='3gram')[:10]
#print sugarlid_gnb(t, option='3gram')[:10]
#print sugarlid_bnb(t, option='3gram')[:10]
#print sugarlid_cosine(t, option='char', data_source='odin')[:10]
x = sugarlid_mnb(t, option='3gram', data_source='crubadan', smoothing=0.00001, tfidf=True)[:10]
for i in x:
  print i[0], i[1], ISO2LANG[i[1]] 


#print sugarlid_cosine(t, option='2gram')[:10]
#print sugarlid_cosine(t, option='1gram')[:10]
#print sugarlid_cosine(t, option='4gram')[:10]
#print sugarlid_cosine(t, option='5gram')[:10]