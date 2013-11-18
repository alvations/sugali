#!/usr/bin/env python -*- coding: utf-8 -*-

from nltk import NaiveBayesClassifier as nbc 

def txt2ngrams(text, n):
  """ Convert text into character ngrams. """
  text = text.lower()
  return ["".join(j) for j in zip(*[text[i:] for i in range(n)])]


