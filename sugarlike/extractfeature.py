# -*- coding: utf-8 -*-
from __future__ import print_function
import sys; sys.path.append('../') # Access modules from parent dir.

from itertools import chain

def word2ngrams(text, n=3, option='char', with_word_boundary=False):
  """ Convert text into character ngrams. """
  text = text.lower()

  if option == 'char':
    char_ngrams =  ["".join(j) for j in zip(*[text[i:] for i in range(n)])]
    if with_word_boundary:
      char_ngrams+=["<"+text[:2],text[-2:]+">"]
    return char_ngrams

  if 'gram' in option:
    char_ngrams = ["".join(j) for j in zip(*[text[i:] \
                   for i in range(int(option[0]))])]
    if with_word_boundary:
      char_ngrams+=["<"+text[:2],text[-2:]+">"]
    return char_ngrams

def sentence2ngrams(text,n=3, option='char', with_word_boundary=False):
  """ Takes a document/sentence, convert into ngrams"""
  if option == 'char':
    return list(chain(*[word2ngrams(i, n, option, with_word_boundary) \
                        for i in text.split()]))
  if option == 'word':
    from nltk.util import ngrams
    return list(ngrams(text.split(), 1))
  
  if "gram" in option:
    n = int(option[0])
    return list(chain(*[word2ngrams(i, n, option, with_word_boundary) \
                        for i in text.split()]))

  if "all" in option:
    return list(chain(*[sentence2ngrams(text,n=i) for i in range(1,5)]))


def extract_feature_from_datasource(data_source, outputpath):
  """ Returns a Counter object with the ngrams/word counts. """
  import tarfile, codecs, os
  import cPickle as pickle
  from collections import defaultdict, Counter
  from universalcorpus.miniethnologue import ISO2LANG
  from universalcorpus import odin, omniglot, udhr
  
  assert data_source in ['odin','omniglot','udhr','crubadan','wiki'], \
        'Only data from crubadan/odin/ominglot/udhr/wikipedia available.'
  
  datalost = set() # To keep track of which languages not in ISO.
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)

  if data_source in ['odin','omniglot','udhr','wiki']:
    for lang, sent in locals()[data_source].source_sents():
      print (data_source, lang, 'Creating feature sets, please be patient...')
      ##print (sent)
      if lang in ISO2LANG or lang in MACRO2LANG:
        for n in range(1,5): # Generates 1-5character ngrams.
          charngrams[lang]+= Counter(sentence2ngrams(sent, n, 'char', True))
        wordfreqs[lang]+=Counter(sent.split())
      else:
        datalost.add((data_source, lang))
  elif data_source == 'crubadan':
    charngrams, wordfreqs, datalost = crubadan2counters()
    
  if outputpath and os.path.exists(outputpath):
    with codecs.open(outputpath+'/'+data_source+'-char.pk','wb') as fout:
      pickle.dump(charngrams, fout)
    with codecs.open(outputpath+'/'+data_source+'-word.pk','wb') as fout:
      pickle.dump(wordfreqs, fout)
        
  return charngrams, wordfreqs, datalost
  
def crubadan2counters(crubadanfile='crub-131119.zip'):
  """ 
  Returns the character ngrams, word frequences and list of files that are 
  in crubadan but not listed in the ISO code.
  """
  import os, zipfile, time
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG, LANG2ISO
  from collections import defaultdict, Counter
  crubadanfile = os.path.dirname(__file__) + \
                     '/../universalcorpus/data/crubadan/' + crubadanfile
  assert os.path.exists(crubadanfile)
  
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)
  datalost = set()
  
  with zipfile.ZipFile(crubadanfile,'r') as inzipfile:
    for infile in inzipfile.namelist():
      path, filename = os.path.split(infile)
      lang = filename.rpartition('.')[0]
      if '-' in lang: lang = lang.partition('-')[0]
      if not lang: continue
      ##start = time.time()
      if lang not in ISO2LANG:
        print('converting', lang,  'to', LANG2ISO[lang],'...')
        if LANG2ISO[lang][0] in ISO2LANG: 
          lang = LANG2ISO[lang][0] 
      ##print (time.time() -start)
      if lang in ISO2LANG:
        print ('crubadan', infile, lang, 'Creating feature sets, please be patient...')
        for line in inzipfile.open(infile):
          key, count = line.strip().split(' ')
          
          if 'words' in path: # Updates wordfreq
            wordfreqs[lang][key] = int(count)
          if 'chars' in path: # Updates charngrams
            charngrams[lang][key] = int(count)
      else:
        datalost.add(infile)
  return charngrams, wordfreqs, datalost

def feature_interface(data_source):
  """ Unpickle the feature pickles if exists else create them. """
  import cPickle as pickle
  import os, io
  
  if not os.path.exists(data_source+'-char.pk') or \
  not os.path.exists(data_source+'-word.pk'):
    extract_feature_from_datasource(data_source, '.')
  
  with io.open(data_source+'-char.pk','rb') as fin:
    charngrams = pickle.load(fin)
  with io.open(data_source+'-word.pk','rb') as fin2:
    wordfreqs = pickle.load(fin2)
  
  return charngrams, wordfreqs

def get_features(data_source, language=None, option='char', \
                 with_word_boundary=True):  
  """ Get features given the data_source, language and option"""
  charngs, wordfqs = feature_interface(data_source)  
  if option == 'char':
    result = charngs[language] if language else charngs
  elif option == 'word':
    result = wordfqs[language] if language else wordfqs
  elif 'gram' in option:
    from collections import Counter, defaultdict
    _result = charngs[language] if language else charngs
    result = defaultdict(Counter)
    for i in _result:
      result[i] = Counter({j:_result[i][j] for j in _result[i] \
                           if len(j) == int(option[0])})
  if option == None:
    return charngs, wordfqs
  
  if not with_word_boundary: #TODO: 
    pass
  
  return result if result else print('%s does not have %s features' \
                                     % (data_source, language))


'''
#Informal Test:
x = get_features('odin','xxx','char') # Gets nothing since there is no lang xxx.

x = get_features('odin','deu','char') # Gets feature for 1 language.
print(x)

y = get_features('odin',option='char') # Gets feature for 1 language.
for i in y:
  print(y[i])
  
x = get_features('odin',option='3gram')
for i in x:
  print(i, x[i])
'''
'''
x = get_features('crubadan', option='3gram')
for i in x:
  for j in x[i]:
    print (i,j, x[i][j])
'''

