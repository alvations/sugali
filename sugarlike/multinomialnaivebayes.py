#!/usr/bin/env python -*- coding: utf-8 -*-

#import sys; sys.path.append('../')

from __future__ import division
from collections import Counter
from math import log, exp
from nltk.probability import SimpleGoodTuringProbDist, add_logs, sum_logs
from nltk import FreqDist

import sys; reload(sys); sys.setdefaultencoding("utf-8"); sys.path.append('../')

from universalcorpus import odin
from extractfeature import sentence2ngrams, get_features

class SGT(SimpleGoodTuringProbDist):
  '''
  Performs Simple Good-Turing smoothing for frequency counts.
  More care is taken to avoid underflow errors than in the NLTK base class.
  '''
  def __init__(self, data, vocab=None, min=10000):
    '''
    By default, the vocabulary size (vocab) is taken to be twice the number of observed items,
    with a minimum size (min) of 10,000.
    This is somewhat ad hoc, but considering Zipf's Law, we would expect vocabulary size to be infinite.
    '''
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
    '''
    Calculates the unnormalised log-probability of generating a sample with observed frequency 'count'.
    '''
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
    '''
    Calculates the renormalisation factor for observed sample types.
    '''
    log_prob_cov = sum_logs([log(nr_, 2) + self.log_prob_measure(r_) for r_, nr_ in zip(r, nr)])
    if self._prob_measure(0) < 1:
      self.log_renormal = log(1 - self._prob_measure(0), 2) + log_prob_cov
      self._renormal = exp(self.log_renormal)
    else:  # If this happens, Good-Turing smoothing is probably a bad idea...
      self.log_renormal = float('-inf')
      self._renormal = 0.0
  
  def logprob(self, sample):
    '''
    Calculates the normalised log-probability of generating a sample.
    '''
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
    '''
    Calculates the normalised log probability of generating a sample sequence.
    (Technically speaking, this function accepts input as a bag of samples,
     not a sequence, but the probability of any permutation is the same.)
    '''
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
  Given a multinomial language model, calculates the log-probability of an input string.
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

def classify_odin(sentence, verbose=True):
  '''
  Given an input string, classifies it based on Odin character n-grams.
  Effectively an informal test.
  '''
  test = Counter(sentence2ngrams(sentence, with_word_boundary=True, option='allgrams'))
  trainset = get_features('odin', option='char')
  sgt_results = []
  for lang in trainset:
    train = trainset[lang]
    sgt_results.append((SGT(train, min=6000).estimate(test),lang))
  sgt_results.sort(reverse=True)
  if verbose:
    for i in sgt_results[:10]:
      print i
  return sgt_results

def evaluate_crubadan_odin(filename):
  '''
  Trains models from the Crubadan data and runs them on Odin
  '''
  print "Loading character features..."
  trainsetchar = get_features('crubadan', option='char')
  print "Loading word features..."
  trainsetword = get_features('crubadan', option='word')
  print "Loading test data..."
  labels = [x[0] for x in odin.source_sents()]
  test = [(Counter(sentence2ngrams(x[1], with_word_boundary=True, option='allgrams')), Counter(x[1].split())) for x in odin.source_sents()]
  
  print "Calculating results..."
  with open(filename,'w') as f:
    f.write(' '.join(labels)+'\n')
    labels = None
    for lang in sorted(trainsetchar.keys()):
      print lang
      charresult = lang
      wordresult = lang
      modelchar = SGT(trainsetchar.pop(lang))
      modelword = SGT(trainsetword.pop(lang))
      for sentence in test:
        charresult += ' ' + float.hex(modelchar.estimate(sentence[0]))
        wordresult += ' ' + float.hex(modelword.estimate(sentence[1]))
      f.write(charresult+'\n')
      f.write(wordresult+'\n')
  print "Done!"
  
def sort_results(inputfilename, charfilename, wordfilename, combfilename, weight=1):
  print "Loading data..."
  data = []
  with open(inputfilename,'r') as f:
    answer = f.readline().split()
    N = len(answer)
    datachar = [[] for i in range(N)]
    dataword = [[] for i in range(N)]
    datacomb = [[] for i in range(N)]
    charprob = None
    wordprob = True
    for line in f:
      code, rest = line.split(None,1)
      print code
      if wordprob:
        charprob = [float.fromhex(x) for x in rest.split()]
        wordprob = None
      else:
        wordprob = [float.fromhex(x) for x in rest.split()]
        combprob = [charprob[i]+weight*wordprob[i] for i in range(N)]
        for i in range(N):
          datachar[i].append((charprob[i], code))
          dataword[i].append((wordprob[i], code))
          datacomb[i].append((combprob[i], code))
  print "Sorting data..."
  '''
  with open(charfilename,'w') as f:
    for i in range(N):
      print answer[i]
      ordered = [lang for prob, lang in sorted(datachar[i], reverse=True)]
      f.write('{}: {}\n'.format(answer[i], ' '.join(ordered)))
  with open(wordfilename,'w') as f:
    for i in range(N):
      print answer[i]
      ordered = [lang for prob, lang in sorted(dataword[i], reverse=True)]
      f.write('{}: {}\n'.format(answer[i], ' '.join(ordered)))
  '''
  with open(combfilename,'w') as f:
    for i in range(N):
      print answer[i]
      ordered = [lang for prob, lang in sorted(datacomb[i], reverse=True)]
      f.write('{}: {}\n'.format(answer[i], ' '.join(ordered)))
  print "Done!"

def calculate_statistics(inputfilename, outputfilename):
  from collections import defaultdict
  print "Loading data..."
  data = defaultdict(list)
  with open(inputfilename,'r') as f:
    for line in f:
      answer, rest = line.split(':',1)
      code = rest.split()
      try:
        rank = code.index(answer) + 1
      except ValueError:
        rank = float('Inf')
      data[answer].append(rank)
  
  print "Calculating statistics..."
  with open(outputfilename,'w') as f:
    sumfirst = 0
    sumtopten = 0
    sumaverage = 0
    filterfirst = 0
    filtertopten = 0
    filteraverage = 0
    filtertotal = 0
    for code in data:
      rank = data[code]
      total = len(rank)
      first = rank.count(1) / total
      topten = len([x for x in rank if x<=10]) / total
      average = sum(rank) / total
      sumfirst += first
      sumtopten += topten
      sumaverage += average
      if rank[0] != float('Inf'):
        filterfirst += first
        filtertopten += topten
        filteraverage += average
        filtertotal += 1
      print code, first, topten, average
      f.write("{}: {} {} {}\n".format(code,float.hex(first),float.hex(topten),float.hex(average)))
    total = len(data)
    sumfirst /= total
    sumtopten /= total
    sumaverage /= total
    filterfirst /= filtertotal
    filtertopten /= filtertotal
    filteraverage /= filtertotal
    print total - filtertotal, "languages not found"
    print "all:", sumfirst, sumtopten, sumaverage
    print "filtered:", filterfirst, filtertopten, filteraverage
    f.write("average: {} {} {}\n".format(sumfirst,sumtopten,sumaverage))
    f.write("filtered: {} {} {}".format(filterfirst,filtertopten,filteraverage))

#sort_results('newresults.txt', 'bla', 'bla', 'sorted-scrap.txt', 2**10)
#calculate_statistics('sorted-scrap.txt','summary-scrap.txt')