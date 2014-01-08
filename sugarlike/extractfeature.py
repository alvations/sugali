# -*- coding: utf-8 -*-

import sys; sys.path.append('../') # Access modules from parent dir.

from itertools import chain

def word2ngrams(text, n=3, option='char', with_word_boundary=False, ):
  """ Convert text into character ngrams. """
  text = text.lower()
  if option == 'char':
    char_ngrams =  ["".join(j) for j in zip(*[text[i:] for i in range(n)])]
    if with_word_boundary:
      char_ngrams+=["<"+text[:2],text[-2:]+">"]
    return char_ngrams
  if option == 'word':
    if n > len(text.split()):
      n = len(text.split()) 
    word_ngrams = [j for j in zip(*[text.split()[i:] for i in range(n)])]
    return word_ngrams  

def sentence2ngrams(text,n=3, option='char', with_word_boundary=False):
  """ Takes a document/sentence, convert into ngrams"""
  return list(chain(*[word2ngrams(i, n, option, with_word_boundary) \
                      for i in text.split()]))

