from collections import Counter
from math import log, exp
from nltk.probability import SimpleGoodTuringProbDist as SGTdist
from nltk import FreqDist

def SGT(data, vocab=None):
  '''
  Calculates a multinomial model with Simple Good-Turing smoothing.
  By default, the estimated vocabulary size is twice the observed size.
  Assumes frequencies in the form of a Counter.
  '''
  if vocab == None:
    vocab = 2 * len(data)
  return SGTdist(FreqDist(data),vocab)

def SGTestimate(language, input):
  '''
  Given a multinomial model with SGT smoothing, calculates the probability of an input string.
  Assumes input in the form of a Counter.
  '''
  result = 0
  for x in input:
    result += language.logprob(x) * input[x]
  return exp(result)

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
  return exp(result)

'''
train = Counter({'a':1,'b':5,'c':2})
test = Counter({'b':1,'a':1})

langSGT = SGT(train)
langMLE = MLE(train)

print SGTestimate(langSGT,test)
print MLEestimate(langMLE,test)
'''
