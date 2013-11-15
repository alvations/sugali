# -*- coding: utf-8 -*-

import codecs, urllib2, re, os
from collections import defaultdict
import cPickle as pickle

ETHNOLOGUE_DOMAIN = "http://www.ethnologue.com/"
LANG_FAMILY_TAG = '''<div class="views-field views-field-name">'''
LANG_TAG = '''<span class="views-field views-field-field-iso-639-3">'''
ETHNO_DIR = "../data/ethnologue/"

def get_language_families():
  """ REQUIRES INTERNET CONNECTION !!!! (takes ~3mins with 1.8 MB/s)
  Downloads the language families and its children from www.ethnology.com, and 
  return it as a defaultdict(list).
  """
  from bs4 import BeautifulSoup as bs
  # If ethnologue language family html doesn't exist yet, download it.
  if not os.path.exists(ETHNO_DIR+'ethnologue-family.html'):
    fin = urllib2.urlopen(ETHNOLOGUE_DOMAIN+'browse/families')\
          .read().decode('utf8')
    with codecs.open(ETHNO_DIR+'ethnologue-family.html','w','utf8') as fout:
      print>>fout, fin
  
  fin = codecs.open('ethnologue-family.html','r','utf8')
  lang_fams = defaultdict(list)
  
  for line in fin.readlines():
    line = line.decode('utf-8')
    # Detects the language family and its link.
    if LANG_FAMILY_TAG in line:
      langfamlink = bs(line).find('a').get('href')
      langfamily = bs(line).get_text().strip()
      ##print langfamily, langfamlink
      # Downloads the page of a language family and gets its:
      # (1) name, (2) iscode (3) geographical information
      for line2 in urllib2.urlopen(ETHNOLOGUE_DOMAIN+langfamlink):
        line2 = line2.decode('utf-8')
        if LANG_TAG in line2:
          lang = bs(line2).get_text().strip()
          if lang.strip() == "": continue
          langname = re.sub(r'[\[\(\<][^)]*[\]\)\>]', '', lang)
          isocode = re.findall(r'\[([^]]*)\]',lang)[0]
          geo = re.findall(r'\([^)]*\)',lang)[0].rpartition(" ")[2][:-1]
          ##print isocode, langname , geo
          lang_fams[langfamily].append((isocode, langname , geo))
  return lang_fams

def load_language_families():
  """
  Loads languagefamilies.pk and return it as a defaultdict(list).
  
  USAGE:
  >>> language_families = get_language_families()
  >>> for family in language_families:
  >>>  for language in language_families[family]:
  >>>    isocode, language_name, geo = language
  
  """
  # If languagefamilies.pk is not available, create it. 
  if not os.path.exists(ETHNO_DIR+'languagefamilies.pk'):
    lfs = get_language_families()
    with codecs.open(ETHNO_DIR+'languagefamilies.pk','wb') as fout:
      pickle.dump(lfs, fout)
  # Loads the pickled file.
  with codecs.open(ETHNO_DIR+'languagefamilies.pk','rb') as fin2: 
    return pickle.load(fin2)

''' Informal test...
language_families = load_language_families() 
for lf in language_families:
  for l in language_families[lf]:
    print lf, l
'''