# -*- coding: utf-8 -*-
from __future__ import division
import sys; sys.path.append('../') # Access modules from parent dir.
from collections import defaultdict, Counter
from extractfeature import feature_interface, sentence2ngrams
from evaluate import normalise, MultiCounter, dot_product, sum_cosine
from universalcorpus.miniethnologue import ISO2LANG, LANG2ISO
 
source = None
model = None

while source == None:
  input = raw_input("Please choose a data source: ")
  if input in ["crubadan", "odin", "udhr," "omniglot"]:
    source = input
  #else:
  #  source = "odin"

while model == None:
  input = raw_input("Please choose a model: ")
  if input in ["cosine-word", "cosine-char", "cosine-combined"]:
    model = input
  #else:
  #  model = "cosine-combined"

print "Loading..."
char, word = feature_interface(source)

if model == "cosine-word":
  featureset = word
  for lang in featureset:
    normalise(featureset[lang])
  identify = dot_product
  DataStr = Counter
  option = "word"
  with_word_boundary = False
  
elif model == "cosine-char":
  featureset = char
  for lang in featureset:
    normalise(featureset[lang])
  identify = dot_product
  DataStr = Counter
  option = "allgrams"
  with_word_boundary = True
  
elif model == "cosine-combined":
  featureset = defaultdict(MultiCounter)
  for lang in word:
    if source == "crubadan":
      print lang
    featureset[lang][0] = word[lang]
    for ngram, count in char[lang].items():
      ngram = unicode(ngram)
      if len(ngram) > 5:  # There are still some encoding issues for the language "enc", whose characters are recognised as two characters long
        continue
      featureset[lang][len(ngram)][ngram] = count
  for lang in featureset:
    for i in range(6):
      normalise(featureset[lang][i])
  identify = sum_cosine
  DataStr = MultiCounter
  option = "separate"
  with_word_boundary = True

char = None
word = None
numlang = len(featureset)

while True:
  input = raw_input("\nEnter text to be identified: ").decode(sys.stdin.encoding)
  sentfeat = DataStr(sentence2ngrams(input, option=option, with_word_boundary=with_word_boundary))
  results = identify(featureset, sentfeat)
  result_list = [code for score, code in sorted(results, reverse=True)]
  for i in range(5):
    code = result_list[i]
    print "  {}. {}: {}".format(i+1, code, unicode(ISO2LANG[code][0]).title())
  #print "\tTop ten results: {}".format(" ".join(result_list[0:10]))
  answercode = raw_input("What was the correct answer? ").decode(sys.stdin.encoding)
  try:
    answerlang = unicode(ISO2LANG[answercode][0]).title()
  except IndexError:
    try:
      answerlang = unicode(answercode)
      answercode = LANG2ISO[answerlang.lower()][0]
      print '  We interpret "{}" to mean "{}"'.format(answerlang, answercode)
      answerlang = answerlang.title()
    except IndexError:
      print "  Sorry, that is not a recognised code or langauge name..."
      continue
  try:
    rank = result_list.index(answercode) + 1
    print "  {} was rank {} out of {}.".format(answerlang, rank, numlang)
  except ValueError:
    print "  Sorry, {} was not seen in training!".format(answerlang)
  