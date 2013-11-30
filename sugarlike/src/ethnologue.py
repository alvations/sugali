# -*- coding: utf-8 -*-

import codecs, urllib2, re, os
from collections import defaultdict
import cPickle as pickle

ETHNOLOGUE_DOMAIN = "http://www.ethnologue.com/"
LANG_FAMILY_TAG = '''<div class="views-field views-field-name">'''
LANG_TAG = '''<span class="views-field views-field-field-iso-639-3">'''
ETHNO_DIR = "../data/ethnologue/"

class Tree(defaultdict):  # A tree is a dictionary of trees (recursively). New elements can created by calling them.
  def __init__(self, label=""):  # Use a defaultdict(Tree), with two extra attributes
    super(Tree, self).__init__(Tree)
    self.mother = None
    self.name = label
  def __missing__(self, key):  # Do the same as defaultdict, then propagate labels to children
    child = super(Tree, self).__missing__(key)
    child.name = key
    child.mother = self
    return child
  def __str__(self):  # Pretty display
    if self.keys():
      childStrings = [str(child) for child in self.itervalues()]
      return "[{} {}]".format(self.name," ".join(childStrings))
    else:
      return "[{}]".format(self.name)
  def ancestors(self):  # Returns a list, giving all nodes from the given node to the root 
    ancestorList = [self.name]
    currentNode = self
    while currentNode.mother:
      ancestorList.append(currentNode.mother.name)
      currentNode = currentNode.mother
    return ancestorList

def read_language(filehandle):
  soup = bs(filehandle.read())
  for meta in soup.find_all("meta"):
    try:
      if meta["property"] == "og:title":
        primary_name = meta["content"]
        break
    except KeyError:
      continue
  for div in soup.find_all("div"):
    try: fieldName = div["class"][1]
    except KeyError: continue
    except IndexError: continue
    if fieldName[0:10] == "field-name":
      for subdiv in div.find_all("div"):
        if subdiv["class"] == ["field-item", "even"]:
          if fieldName == "field-name-field-alternate-names":
            alternate_names = subdiv.string.split(", ")
          if fieldName == "field-name-language-classification-link":
            classification = subdiv.string.split(", ")
          if fieldName == "field-name-field-dialects":
            dialects = subdiv.p.get_text()
  return (primary_name, alternate_name, classification, dialects)

def get_language_families():
  """ REQUIRES INTERNET CONNECTION !!!! (takes ~3mins with 1.8 MB/s)
  Downloads the language families and its children from www.ethnologue.com, and 
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

# TODO:
def get_langinfo(isocode):
  """ Gets language information from Ethnologue. """
  page = "http://www.ethnologue.com/language/"+isocode

# TODO:
def langiso():
  """ [in]: Language name, [out]: isocode. """
  pass
