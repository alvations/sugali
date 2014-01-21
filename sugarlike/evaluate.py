# -*- coding: utf-8 -*-

def tenfold(data_source, randseed=0):
  import random, sys
  from extractfeature import get_features, sentence2ngrams
  from universalcorpus import odin, omniglot, udhr
  random.seed(randseed)
  corpus = list(locals()[data_source].source_sents())
  corpus = sorted(iter(corpus), key=lambda k: random.random())
  totrain = int(len(corpus) * 90 / 100)
  yield corpus[:totrain] # train data
  yield corpus[totrain:] # test data

'''  
for i in tenfold('odin'):
  for j in i:
    print j
'''