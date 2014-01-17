#!/usr/bin/env python -*- coding: utf-8 -*-

#import sys; sys.path.append('../')

from collections import Counter
from math import log, exp
from nltk.probability import SimpleGoodTuringProbDist as SGTdist
from nltk import FreqDist

import sys; reload(sys); sys.setdefaultencoding("utf-8")

def SGT(data, vocab=None, min=10000):
  '''
  Calculates a multinomial model with Simple Good-Turing smoothing.
  By default, the estimated vocabulary size is twice the observed size, or 10 000, whichever is larger
  Assumes frequencies in the form of a Counter.
  '''
  if vocab == None:
    vocab = max( 2 * len(data), min)
  return SGTdist(FreqDist(data),vocab)

def SGTestimate(language, input):
  '''
  Given a multinomial model with SGT smoothing, calculates the probability of an input string.
  Assumes input in the form of a Counter.
  '''
  result = 0
  for x in input:
    result += language.logprob(x) * input[x]
  return result

def combined_estimate(classifiers, input):
  '''
  Naively combines a set of SGT-smoothed models.
  '''
  result = 0
  for model in classifiers:
    result += SGTestimate(model, input)
  return result

def MLE(freq):
  '''
  Calculates the maximum likelihood estimator for a multinomial distribution.
  Assumes frequencies in the form of a Counter.
  '''
  total = log(sum(freq.values()),2)
  return {x: log(freq[x],2) - total for x in freq}

def MLEestimate(language, input, oov=-float('inf')):
  '''
  Given a multinomial language model, calculates the probability of an input string.
  Optionally, use an ad-hoc probability for OOV items
  Assumes input in the form of a Counter.
  '''
  result = 0
  for x in input:
    try:
      result += language[x] * input[x]
    except KeyError:  # Out of vocabulary items
      result += oov
  return result

'''
train = Counter({'a':1,'b':5,'c':2})
test = Counter({'b':1,'a':1})

langSGT = SGT(train)
langMLE = MLE(train)

print SGTestimate(langSGT,test)
print MLEestimate(langMLE,test)
'''

from extractfeature import sentence2ngrams, get_features
s = u"je m'appelle Claude"
test = Counter(sentence2ngrams(s, with_word_boundary=True))
print test

trainset = get_features('odin', option='3gram')
sgt_results = []
#mle_results = []


for lang in trainset:
  train = trainset[lang]
  if train: # no data from feature extractor (PLEASE CHECK)
    sgt_results.append((SGTestimate(SGT(train, min=3000), test),lang))
    #mle_results.append((MLEestimate(MLE(train), test),lang))

for i in sorted(sgt_results, reverse=True)[:10]:
  print i

