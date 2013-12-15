# -*- coding: utf-8 -*-

import sys; sys.path.append('../') # Access modules from parent dir.

import tarfile, codecs, os, re, string
from collections import defaultdict
import cPickle as pickle
from utils import remove_tags

try:
  from bs4 import BeautifulSoup as bs
except:
  from BeautifulSoup import BeautifulSoup as bs
#bs.find_all = getattr(bs, 'find_all',False) or getattr(bs, 'findAll')

def get_odin_igts(ODINFILE = '../../data/odin/odin-full.tar'):
  """
  Extracts the examples from the ODIN igts and returns a defaultdict(list),
  where the keys are the lang iso codes and values are the examples.
  
  >>> igts = get_odin_igts()
  >>> for lang in igts:
  >>>  for igt in igts[lang]:
  >>>    print lang, igt
  """
  tar = tarfile.open(ODINFILE)
  docs = defaultdict(list)
  for infile in tar:
    if '.xml' in infile.name: # there's a rogue file in the tar that is not xml.
      lang = infile.name[:-4].lower()
      # Find the <igt>...</igt> in the xml.
      igts = bs(tar.extractfile(infile).read()).findAll('igt')
      for igt in igts:
        # Find the <example>...</example> in the igt.
        examples = bs(unicode(igt)).findAll('example')
        for eg in examples:
          try:
            # Only use triplets lines and assumes that
            # line1: src, line2:eng, line3:gloss
            src, eng, gloss = bs(unicode(eg)).findAll('line')
            src, eng, gloss = map(unicode, [src, eng, gloss])
            docs[lang].append((src, eng, gloss))
            ##print src, eng, gloss
          except:
            raise; print eg
  return docs

def load_odin_pickle(ODIN_DIR='../../data/odin/'):
  """
  Loads odin-docs.pk and yield one IGT at a time.
  
  >>> for lang, igts in load_odin_pickle():
  >>>   for igt in igts:
  >>>     print lang, igt
  """
  # If odin-docs.pk is not available create it.
  if not os.path.exists(ODIN_DIR+'odin-docs.pk'):
    odindocs = get_odin_igts()
    # Outputs the odin igts examples into '../data/odin/odin-docs.pk'.
    with codecs.open(ODIN_DIR+'odin-docs.pk','wb') as fout:
      pickle.dump(odindocs, fout)
  # Loads the pickled file.
  with codecs.open(ODIN_DIR+'odin-docs.pk','rb') as fin2: 
    docs = pickle.load(fin2)
    for lang in docs:
      # the data might be too much for the RAM, so yield instead of return.
      yield (lang, docs[lang])

def load_odin_tarfile():
  """
  Loads odin-igts.tar and yield one IGT at a time.
  
  """
  prev_lang = ''
  
  for lang, igts in load_odin_pickle():
    for igt in igts:
      print lang, igt
   
##load_odin_tarfile()
      
def odin_src_only(outputtofile=True, testing=False):
  """ Extracts only the source language tokens from the ODIN IGTs."""
  for language, documents in sorted(load_odin_pickle()):
    for d in documents:
      if d[0].strip() == "": continue;
      src = remove_tags(d[0])
      # Removes heading bullets, e.g. (1)... | 1) | ( 12 ) | i. ... | A2. ...
      src = re.sub(r'^\(?\s?\w{1,5}\s*[):.]\s*', '', src)
      src = re.sub(r'^\(?\w{1,5}\s*[):.]\s*', '', src)
      src = re.sub(r'^\(?\w{1,5}\s*[):.]\s*', '', src)
      morphemes = src
      # Joins the morphemes up into words.
      words = re.sub( ' *- *', '', src)
      if src == '' or any(i for i in string.punctuation if i in src):
        continue
      yield language, words, morphemes, remove_tags(d[1]), remove_tags(d[2])
      
  #if outputtofile == True:
  #  with codecs.open(ODIN_DIR+'odin-src.pk','wb') as fout:
  #    pickle.dump(odinsrc, fout)

'''
all_lang = set()
for lang, tokens, morphs, gloss, eng, in odin_src_only():
  print "\t".join([lang, tokens, morphs, gloss, eng])
  all_lang.add(lang)
print len(all_lang)
'''

def load_odin_src():
  """
  Loads odin-docs.pk and returns it as a defaultdict
  
  >>> for lang, text in load_odin_src():
  >>>   print lang, text
  """
  pass