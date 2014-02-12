#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Cosine function to calculate similary between 2 documents.
This is no longer used by evaluate.py

Source: https://github.com/alvations/pywsd/blob/master/cosine.py 
"""

import re, math
from collections import Counter

def cosine_similarity(sent1, sent2):
  """ Calculates cosine between 2 sentences/documents. """
  WORD = re.compile(r'\w+')
  def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
      return 0.0
    else:
      return float(numerator) / denominator

  def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

  vector1 = text_to_vector(sent1)
  vector2 = text_to_vector(sent2)
  cosine = get_cosine(vector1, vector2)
  return cosine

"""
I've moved some functions from evaluate.py that we were no longer using.
"""

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


'''
# Alternative models:
    elif model == "sklearn":  # Multinomial Naive Bayes with addiditve smoothing
      featureset, tags, allfeatures = features2numpy(tfidfize(featureset)) 
      from sklearn.naive_bayes import MultinomialNB
      mnb = MultinomialNB(alpha=1)   
      for lang, testsent in test:
        guess = mnb.fit(featureset, tags).predict_proba(featurize(testsent, \
                                                  allfeatures, option=option))
        sklearn_results = sorted(zip(guess.tolist()[0], tags), reverse=True)
        best = sklearn_results[0]
        fold_results[lang == best[1]]+=1
        top10 = [i[1] for i in sklearn_results[:10]]
        if lang in top10:
          ##print 1/float(top10.index(lang)+1)
          rr.append(1/float(top10.index(lang)+1))
        else:
          rr.append(0)
    
    
    if model == "sgt": # Multinomial Naive Bayes with Simple Good-Turing smoothing
      """
      Need to test this...
      """
      for lang, testsent in test:
        sgt_results = []
        testsent = Counter(sentence2ngrams(testsent))
        for flang in featureset:
          train = featureset[flang]
          sgt = SGT(train)
          sgt_results.append((sgt.estimate(testsent),flang))
'''
