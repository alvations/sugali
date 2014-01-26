#!/usr/bin/env python -*- coding: utf-8 -*-

#import sys; sys.path.append('../')

from collections import Counter
from math import log, exp
from nltk.probability import SimpleGoodTuringProbDist, add_logs, sum_logs
from nltk import FreqDist

import sys; reload(sys); sys.setdefaultencoding("utf-8")

class SGT(SimpleGoodTuringProbDist): # Do we need the whole thing, or can we just extract the relevant bits?
  def __init__(self, data, vocab=None, min=10000):
    if type(data) == Counter or type(data) == dict:
      data = FreqDist(data)
    if vocab == None:
      vocab = max(2*len(data), min)
    assert vocab >= data.B()
    self._freqdist = data
    self._bins = vocab
    r, nr = self._r_Nr()
    self.find_best_fit(r, nr)
    self._switch(r, nr)
    self.log_renormalise(r, nr)
  
  def log_prob_measure(self, count):
    if count == 0 and self._freqdist.N() == 0 :
      return 0.0
    elif count == 0 and self._freqdist.N() != 0 :
      return log(self._freqdist.Nr(1), 2) - log(self._freqdist.N(), 2)
    
    if self._switch_at > count:
      Er_1 = self._freqdist.Nr(count+1)
      Er = self._freqdist.Nr(count)
    else:
      Er_1 = self.smoothedNr(count+1)
      Er = self.smoothedNr(count)
    
    log_r_star = log(count+1, 2) + log(Er_1, 2) - log(Er, 2)
    return log_r_star - log(self._freqdist.N(), 2)
  
  def log_renormalise(self, r, nr):
    log_prob_cov = sum_logs([log(nr_, 2) + self.log_prob_measure(r_) for r_, nr_ in zip(r, nr)])
    if self._prob_measure(0) < 1:
      self.log_renormal = log(1 - self._prob_measure(0), 2) + log_prob_cov
      self._renormal = exp(self.log_renormal)
    else:  # If this happens, Good-Turing smoothing is probably a bad idea...
      self.log_renormal = float('-inf')
      self._renormal = 0.0
  
  def logprob(self, sample):
    count = self._freqdist[sample]
    try:
      logp = self.log_prob_measure(count)
    except ValueError:  # In case of zero probability, which shouldn't happen for a normal corpus
      logp = float('-inf')
    if count == 0:
      if self._bins == self._freqdist.B():
        logp = float('-inf')
      else:
        logp -= log(self._bins - self._freqdist.B(), 2)
    else:
      logp += self.log_renormal
    return logp
  
  def estimate(self, test):
    value = 0.0
    for sample in test:
      value += test[sample] * self.logprob(sample)
    return value


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
train = Counter({'a':500,'b':200,'c':1})
test = [Counter({'a':1}),
        Counter({'b':1}),
        Counter({'c':1}),
        Counter({'d':1}),
        Counter({'a':1,'b':1,'c':1,'d':1})]

langSGT = SGT(train)
langMLE = MLE(train)

for x in test:
  print "{}\t{}".format(langSGT.estimate(x), MLEestimate(langMLE,x))
'''

'''
from extractfeature import sentence2ngrams, get_features
s = u"ich bin schwanger"
test = Counter(sentence2ngrams(s, with_word_boundary=True, option='allgrams'))
#print test

trainset = get_features('odin', option='char')
sgt_results = []
#mle_results = []

#maxlen = 0
for lang in trainset:
  train = trainset[lang]
  #if len(train) > maxlen:
  #  maxlen = len(train)
  sgt_results.append((SGT(train, min=6000).estimate(test),lang))
  #mle_results.append((MLEestimate(MLE(train), test),lang))

for i in sorted(sgt_results, reverse=True)[:10]:
  print i

#print maxlen
'''