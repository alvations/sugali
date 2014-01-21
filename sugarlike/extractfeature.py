# -*- coding: utf-8 -*-
from __future__ import print_function
import sys; sys.path.append('../') # Access modules from parent dir.

from itertools import chain

def word2ngrams(text, n=3, option='char'):
  """ Convert text into character ngrams. """
  text = text.lower()

  if option == 'char':
    char_ngrams =  ["".join(j) for j in zip(*[text[i:] for i in range(n)])]
    return char_ngrams

  if 'gram' in option:
    char_ngrams = ["".join(j) for j in zip(*[text[i:] \
                   for i in range(int(option[0]))])]
    
    return char_ngrams

def sentence2ngrams(text,n=3, option='char', with_word_boundary=False):
  """ 
  Takes a document/sentence, convert into ngrams.
  (NOTE: word boundary is counted as a character.)
  """
  if with_word_boundary:
    text = " ".join(["<"+i+">" for i in text.split()])
  
  if option == 'char':
    return list(chain(*[word2ngrams(i, n, option) for i in text.split()]))
  
  if option == 'word':
    return text.split()
  
  if "gram" in option and "all" not in option:
    n = int(option[0])
    return list(chain(*[word2ngrams(i, n, option) for i in text.split()]))

  if "allgrams" in option or 'all' in option:
    return list(chain(*[sentence2ngrams(text,n=i) for i in range(1,5)]))

def extract_feature_from_datasource(data_source, outputpath):
  """ Returns a Counter object with the ngrams/word counts. """
  import tarfile, codecs, os
  import cPickle as pickle
  from collections import defaultdict, Counter
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG
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
  
def crubadan2counters(crubadanfile='crub-131119.zip', lower=False):
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
          if lower: key = key.lower()
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

def tfidfize(_featureset, data_source, option):
  """ Normalized the feature counts with TF-IDF."""
  from collections import defaultdict
  import math, os, io
  import cPickle as pickle
  
  tfidf_pickle = ''.join([data_source,'-',option,'-tfidf','.pk'])
  
  if os.path.exists(tfidf_pickle): # If feature already tfidfized before.
    with io.open(tfidf_pickle,'rb') as fin:
      fs = pickle.load(fin)
  else:
    fs = defaultdict(dict) 
    for lang in _featureset:
      for gram in _featureset[lang]:
        tf = _featureset[lang][gram] / float(sum(_featureset[lang].values()))
        idf = math.log(len(_featureset)) / len([i for i in _featureset if gram in _featureset[i]])
        fs[lang][gram] = tf * idf
        print('Calculating TF-IDF for %s please wait patiently...' % data_source)
        print (lang, gram, _featureset[lang][gram], tf, idf, tf*idf)
        
    with io.open(tfidf_pickle,'wb') as fout:
      pickle.dump(fs, fout)
      
  return fs
    
def get_features(data_source, language=None, option='char', \
                 with_word_boundary=True, tfidf=False):  
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
      _tempcounter = Counter({j:_result[i][j] for j in _result[i] \
                           if len(j) == int(option[0])})
      if len(_tempcounter) > 0: # Ensures that no Counter are empty.
        result[i] = _tempcounter
  if option == None:
    return charngs, wordfqs
  
  if tfidf:
    result = tfidfize(result,data_source, option)
  
  if not with_word_boundary: #TODO: to filter features with "<" or ">" 
    pass
  
  return result if result else print('%s does not have %s features' \
                                     % (data_source, language))

'''
#Informal Test:

x = get_features('odin',option='char', tfidf=True) # get_features() with tfidf
for i in x:
  print(i, x[i])

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

