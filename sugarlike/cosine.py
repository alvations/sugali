#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Cosine function to calculate similary between 2 documents.

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
