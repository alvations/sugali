#!/usr/bin/env python -*- coding: utf-8 -*-

from nltk import NaiveBayesClassifier as nbc 
from itertools import chain
from collections import defaultdict, Counter
import codecs

def word2ngrams(text, n=3, with_word_boundary=False):
  """ Convert text into character ngrams. """
  text = text.lower()
  char_ngrams =  ["".join(j) for j in zip(*[text[i:] for i in range(n)])]
  if with_word_boundary:
    char_ngrams+=["<"+text[:2],text[-2:]+">"]
  return char_ngrams

def doc2ngrams(text,n=3,with_word_boundary=False):
  """ Takes a documents/sentence, convert into ngrams"""
  return list(chain(*[word2ngrams(i) for i in text.split()]))
  ''' # Informal test: see some magically characters that disappears in vie
  test_sentence = u'Nay, Đại hội đò̂ng Liên Hợp Quó̂c tuyên bó̂:'
  for i in doc2ngrams(test_sentence):
    print i
  test_sentence = u'Nay, dai hoi dong lien hop quoc tuyen bo:'
  for i in doc2ngrams(test_sentence):
    print i
  '''

def file2str(infile, encoding='utf8'):
  return " ".join([i.strip('﻿ ﻿').strip() for i in \
                   codecs.open(infile,'r',encoding).readlines()])

def file2ngrams(infile, n=3,with_word_boundary=False):
  return doc2ngrams(file2str(infile))

viefile = '../data/udhr/vie'
engfile = '../data/udhr/eng'
featuresets = [({'3gram':i},'vie') for i in file2ngrams(viefile)]
featuresets+= [({'3gram':i},'eng') for i in file2ngrams(engfile)]

classifier = nbc.train(featuresets)
classifier.show_most_informative_features(5)

st = u'Nay, dai hoi dong lien hop quoc tuyen bo:'

def test(test_sentence):
  testfeatures = word2ngrams(test_sentence)
  num_features = float(len(testfeatures))
  results = Counter() 
  for i in word2ngrams(test_sentence):
    results[classifier.classify({'3gram':i})]+=1
  return {i:j/num_features for i, j in results.items()}
    
print test(st)
    

  





