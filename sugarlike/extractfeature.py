# -*- coding: utf-8 -*-
from __future__ import print_function
#import sys; sys.path.append('../') # Access modules from parent dir.
import os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
import sys; sys.path.append(parentddir)

from itertools import chain

global shutup   # To shut the console prints up, i.e. 
shutup = False  # "Creating feature sets, please be patient..."

def word2ngrams(text, n=3, exact=True):
  """ Convert text into character ngrams. """
  return [text[i:i+n] for i in range(0, len(text)+1-n)]

def sentence2ngrams(text, n=3, option='char', with_word_boundary=False):
  """ 
  Takes a document/sentence, convert into ngrams.
  (NOTE: word boundary is counted as a character.)
  """
  if with_word_boundary:
    words = ["<"+x+">" for x in text.split()]
  else:
    words = text.split()
  
  if option == 'word':
    return words
  
  elif option == 'char' or option[1:5] == 'gram':  # Extracts character n-grams.
    if option[0].isdigit():
      n = int(option[0])
    return list(chain(*[word2ngrams(x, n) for x in words]))
  
  elif option == 'allgrams' or option == 'all':  # Extracts 1 to 5 character n-grams.
    return list(chain(*[list(chain(*[word2ngrams(x, i) for x in words])) for i in range(1,6)]))
  
  elif option == 'separate':
    return [text.split()] + [list(chain(*[word2ngrams(x, i) for x in words])) for i in range(1,6)]
  
  else:
    print("The option '{}' is not recognised!".format(option))
    raise ValueError(option)

def extract_feature_from_datasource(data_source, outputpath):
  """ Returns a Counter object with the ngrams/word counts. """
  import tarfile, codecs, os
  import cPickle as pickle
  from collections import defaultdict, Counter
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG, wikicode2iso
  from universalcorpus import odin, omniglot, udhr, wikipedia
  
  assert data_source in ['odin','omniglot','udhr','crubadan','wikipedia'], \
        'Only data from crubadan/odin/ominglot/udhr/wikipedia available.'
  
  datalost = set() # To keep track of which languages not in ISO.
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)

  if data_source in ['odin','omniglot','udhr']:
    for lang, sent in locals()[data_source].source_sents():
      if not shutup:
        print (data_source, lang, 'Creating feature sets, please be patient...')
      print (lang, sent)
      if lang in ISO2LANG or lang in MACRO2LANG:
        for n in range(1,6): # Generates 1-5character ngrams.
          charngrams[lang]+= Counter(sentence2ngrams(sent, n, 'char', True))
        wordfreqs[lang]+=Counter(sent.split())
      else:
        datalost.add((data_source, lang))
  elif data_source == 'crubadan':
    charngrams, wordfreqs, datalost = crubadan2counters()
  elif data_source == 'wikipedia':
    charngrams, wordfreqs, datalost = wiki2counters('wikipedia')
    
  if outputpath and os.path.exists(outputpath):
    with codecs.open(outputpath+'/'+data_source+'-char.pk','wb') as fout:
      pickle.dump(charngrams, fout)
    with codecs.open(outputpath+'/'+data_source+'-word.pk','wb') as fout:
      pickle.dump(wordfreqs, fout)
        
  return charngrams, wordfreqs, datalost


def wiki2counters(data_source='wikipedia'):
  '''Extract features from wikipedia. This is not Wikipedia specific. It requires the data to be structured (one language after another). Much faster than other extract_feature_from_datasource.'''

  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG, LANG2ISO, WIKI2ISO, wikicode2iso
  from collections import defaultdict, Counter
  from universalcorpus import odin, omniglot, udhr, wikipedia

  datalost = set() # To keep track of which languages not in ISO.
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)

  if data_source == 'wikipedia':
     lang_old = None
     d_chars = dict()
     d_words = Counter()

     for lang, sent in locals()[data_source].source_sents():
      if data_source == 'wikipedia':
       try:
         lang = WIKI2ISO[lang]
       except KeyError:
         lang = wikicode2iso(lang)
       if lang == None:
          datalost.add((data_source, lang))
          continue 
       if lang_old != lang and lang_old != None:
         charngrams[lang_old] = d_chars
         wordfreqs[lang_old] = d_words
         print('next language: ' + str(lang))
         d_chars = Counter()
         d_words = Counter()
       if lang in ISO2LANG or lang in MACRO2LANG:
          for gram in sentence2ngrams(sent, option='allgrams', with_word_boundary=True):
             try:
               d_chars[gram] += 1
             except KeyError:
               d_chars[gram] = 1
          for word in sent.split():
           try:
             d_words[word] += 1
           except KeyError:
             d_words[word] = 1
         #d_chars += Counter(sentence2ngrams(sent, option='allgrams', with_word_boundary=True))
         #d_words += Counter(sent.split())
       else:
         datalost.add((data_source, lang))
       lang_old = lang
     charngrams[lang_old] = d_chars
  #print(charngrams)
  return charngrams, wordfreqs, datalost

def crubadan2counters(crubadanfile='crub-131119.zip', lower=False):
  """ 
  Returns the character ngrams, word frequences and list of files that are 
  in crubadan but not listed in the ISO code.
  """
  import os, zipfile, time
  from universalcorpus.miniethnologue import ISO2LANG, MACRO2LANG, LANG2ISO
  from collections import defaultdict, Counter
  thisdir = os.path.dirname(__file__) if os.path.dirname(__file__) \
            is not "" else "."
  crubadanfile =  thisdir + '/../universalcorpus/data/crubadan/' + crubadanfile
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
        if not shutup:
          print ('crubadan', infile, lang, \
                 'Creating feature sets, please be patient...')
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
                 with_word_boundary=True, tfidf=False, shutup=False):  
  """ Get features given the data_source, language and option"""
  
  globals()['shutup'] = shutup # To shut the console prints up
  charngs, wordfqs = feature_interface(data_source)
  
  if isinstance(option, str):
    if option == 'char':
      result = charngs[language] if language else charngs
    elif option == 'word':
      result = wordfqs[language] if language else wordfqs
    elif 'gram' in option:
      from collections import Counter, defaultdict
      _result = charngs[language] if language else charngs
      result = defaultdict(Counter)
      # BUG: the following loop doesn't work if a language is given. Do we really need the option to specify a language here, anyway?
      for i in _result:
        _tempcounter = Counter({j:_result[i][j] for j in _result[i] \
                             if len(j) == int(option[0])})
        if len(_tempcounter) > 0: # Ensures that no Counter are empty.
          result[i] = _tempcounter
  elif None == option:
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

for i in get_features('wikipedia'):
  print(i)
'''

'''
# To view the features.
x = get_features('odin',option='3gram')
for i in x:
  for j in x[i]:
    print (i, j, x[i][j])
'''

'''
# Testing speed
from time import time

start = time()

for i in range(100000):
  x = sentence2ngrams("this is a reasonably long sentence because of the extra padding", option="allgrams", with_word_boundary=True)
  
end = time()
print(end-start)
print(x)
'''
