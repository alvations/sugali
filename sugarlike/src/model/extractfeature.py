# -*- coding: utf-8 -*-

import sys; sys.path.append('../') # Access modules from parent dir.

import tarfile, tempfile, os, codecs
from itertools import chain
import cPickle as pickle
from collections import defaultdict, Counter
from miniethnologue import ISO2LANG

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
  """ Takes a document, convert into ngrams"""
  return list(chain(*[word2ngrams(i, n, option, with_word_boundary) \
                      for i in text.split()]))

def read_tarfile(intarfile):
  """ Extracts a tarfile to a temp directory, then yield one file at a time. """
  TEMP_DIR = tempfile.mkdtemp()
  with tarfile.open(intarfile) as tf:
    for member in tf.getmembers():
      tf.extract(member, TEMP_DIR)
  
  for infile in os.listdir(TEMP_DIR):
    yield TEMP_DIR+'/'+infile

def extract_sentence_from_tarfile(intarfile):
  """ Extracts character ngrams features given a tar ball. """
  for infile in read_tarfile(intarfile):
    language = infile.split('/')[-1].split('-')[1].split('.')[0].split('_')[0]
    with codecs.open(infile,'r','utf8') as fin:
      for line in fin.readlines():
        sentence = line.split('\t')[0]
        yield language, sentence

# DEPRECATED: use extract_sentence_from_tarfile() 
def extract_odin_sentences(intarfile):
  """ Extracts char ngrams features from odin. """
  for infile in read_tarfile(intarfile):
    language = infile.split('/')[-1].split('-')[1].split('.')[0]
    with codecs.open(infile,'r','utf8') as fin:
      for line in fin.readlines():
        sentence, sentence_morphemes, _ , _ ,_ = line.split('\t')
        yield language, sentence

# DEPRECATED: use extract_sentence_from_tarfile()         
def extract_udhr_sentences(intarfile):
  """ Extracts char ngrams features from udhr. """
  for infile in read_tarfile(intarfile):
    #language = infile.split('/')[-1][:3]
    language = infile.split('/')[-1].split('-')[1].split('.')[0].split('_')[0]
    with codecs.open(infile,'r','utf8') as fin:
      for sentence in fin.readlines():
        yield language, sentence

# DEPRECATED: use extract_sentence_from_tarfile() 
def extract_omniglot_phrases(intarfile):
  """ Extracts char ngrams features from omniglot. """
  for infile in read_tarfile(intarfile):
    language = infile.split('/')[-1].split('-')[1].split('.')[0]
    with codecs.open(infile,'r','utf8') as fin:
      for sentence in fin.readlines():
        yield language, sentence


# Informal tests.
data_source = {'odin':'../../data/odin/odin-cleaner.tar',
              'udhr':'../../data/udhr/udhr-unicode.tar',
              'omniglotphrase':'../../data/omniglot/omniglotphrases.tar'}

datalost = set()
##('aiz','aiw'),('baz','tvu'),('blu','hnj'),()

for s in data_source:
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)
  for lang, sent in extract_sentence_from_tarfile(data_source[s]):
    print s, lang
    if lang in ISO2LANG:
      for n in range(1,5):        
        charngrams[lang]+= Counter(sentence2ngrams(sent, n, 'char', True))
      wordfreqs[lang]+=Counter(sent.split())
    else:
      datalost.add((s, lang))
  with codecs.open(s+'-char.pk','wb') as fout:
    pickle.dump(charngrams, fout)
  with codecs.open(s+'-word.pk','wb') as fout:
    pickle.dump(charngrams, fout)

