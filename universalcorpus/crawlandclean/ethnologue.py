# -*- coding: utf-8 -*-

import codecs, urllib2, re, os, sys
from collections import defaultdict
import cPickle as pickle

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

ETHNOLOGUE_DOMAIN = "http://www.ethnologue.com/"
LANG_FAMILY_TAG = '''<div class="views-field views-field-name">'''
LANG_TAG = '''<span class="views-field views-field-field-iso-639-3">'''
ETHNO_DIR = parentddir+"/data/ethnologue/"

class Tree(defaultdict):
  """
  A tree is a dictionary of trees (recursively). 
  New elements can created by calling them.
  """
  def __init__(self, label=""):
    """
    Use a defaultdict(Tree), with two extra attributes to help navigate in the tree
    """
    super(Tree, self).__init__(Tree) 
    self.mother = None
    self.name = label
    
  def __missing__(self, key): 
    """
    Do the same as defaultdict, then propagate labels to the newborn child
    """
    child = super(Tree, self).__missing__(key)
    child.name = key
    child.mother = self
    return child
  
  def __str__(self):
    """ Descriptor function for pretty display. """
    if self.keys():
      childStrings = [str(child) for child in self.itervalues()]
      return "[{} {}]".format(self.name," ".join(childStrings))
    else:
      return "[{}]".format(self.name)
    
  def ancestors(self):
    """
    Returns a list, giving the names of all nodes from the given node 
    to the root.
    """ 
    ancestorList = [self.name]
    currentNode = self
    while currentNode.mother:
      ancestorList.append(currentNode.mother.name)
      currentNode = currentNode.mother
    return ancestorList
  
  def leaves(self): 
    """
    Returns a set, giving the names of all leaves dominated by the given node.
    """
    if self.keys():
      return set().union(*[child.leaves() for child in self.itervalues()])
    else:
      return set(self.name)

def read_language(filehandle):
  """
  Extracts languages names, the language family, and dialect information 
  from a page on Ethnologue.
  """ 
  soup = bs(filehandle.read())
  primary_name = soup.find("meta", property="og:title")["content"]
  alternate_names = soup.find("div", class_="field-name-field-alternate-names"       ).find("div", class_=["field-item", "even"]).string.split(", ")
  classification  = soup.find("div", class_="field-name-language-classification-link").find("div", class_=["field-item", "even"]).string.split(", ")
  dialects        = soup.find("div", class_="field-name-field-dialects"              ).find("div", class_=["field-item", "even"]).p.get_text()
  return ([unicode(primary_name)]+alternate_names, classification, dialects)

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
  
  fin = codecs.open(ETHNO_DIR+'ethnologue-family.html','r','utf8')
  lang_fams = defaultdict(list)
  
  for line in fin.readlines():
    line = line.decode('utf-8')
    # Detects the language family and its link.
    if LANG_FAMILY_TAG in line:
      langfamlink = bs(line).find('a').get('href')
      langfamily = bs(line).get_text().strip()
      print langfamily, langfamlink
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
          lang_fams[langfamily].append((isocode, langname , geo, langfamlink))
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

def lang_families():
  from bs4 import BeautifulSoup as bs
  langfamfile = 'languagefamilies_with_info.pk'
  fout_tmp = codecs.open('langfam.tmp','w','utf8')
  if not os.path.exists(ETHNO_DIR+langfamfile):
    ethno = {'pop':"field field-name-field-population field-type-"+\
             "text-with-summary field-label-inline clearfix",
             'altnames':"field field-name-field-alternate-names field-type-"+\
             "text-long field-label-inline clearfix",
             'loc':"field field-name-field-region field-type-"+\
             "text-with-summary field-label-inline clearfix",
             'status':"field field-name-language-status field-type-"+\
             "ds field-label-inline clearfix"}
    _lf = {k:[j[0] for j in v] for k,v in load_language_families().items()}
    lf = defaultdict(list)
    for i in _lf:
      for j in _lf[i]:
        site = bs(urllib2.urlopen('https://www.ethnologue.com/language/'+j).read().decode('utf8'))
        name = site.find('title').text.replace(' | Ethnologue','').strip()
        try:
          pop = site.find(attrs={"class": ethno['pop']}).find(attrs={"class": 'even'}).text.strip()
        except AttributeError:
          pop = None  
        status = site.find(attrs={"class": ethno['status']}).find(attrs={"class": 'even'}).text.strip()
        try:
          loc = site.find(attrs={"class": ethno['loc']}).find(attrs={"class": 'even'}).text.strip()
        except AttributeError:
          loc = None
        try:
          altnames = site.find(attrs={"class": ethno['altnames']}).find(attrs={"class": 'even'}).text.strip()
        except AttributeError:
          altnames = None
        lf[i].append((j, name, pop, altnames, loc, status))
        print>>fout_tmp, "\t".join(map(str,[j, i, name, pop, altnames, loc, status]))
    with codecs.open(ETHNO_DIR+langfamfile,'wb') as fout:
      pickle.dump(lf, fout)
  
  with codecs.open(ETHNO_DIR+langfamfile,'wb') as fin2:
    return pickle.load(lf, fin2)
  
##lang_families()

def download_lang_families():
  _lf = {k:[j[0] for j in v] for k,v in load_language_families().items()}
  for i in _lf:
    for j in _lf[i]:
      if os.path.exists(parentddir+"/data/ethnologue/languages/"+j+'.ethno'):
        print i
      try:
        site = urllib2.urlopen('https://www.ethnologue.com/language/' \
                                  +j).read().decode('utf8')
      except urllib2.HTTPError:
        time.sleep(5)
        site = urllib2.urlopen('https://www.ethnologue.com/language/' \
                                  +j).read().decode('utf8')
        
      with codecs.open(parentddir+"/data/ethnologue/languages/"+j+'.ethno','w','utf8') as fout:
        print>>fout, site

'''
from bs4 import BeautifulSoup as bs
langfamfile = 'languagefamilies_with_info.pk'
_lf = {k:[j[0] for j in v] for k,v in load_language_families().items()}
ethno = {'pop':"field field-name-field-population field-type-"+\
             "text-with-summary field-label-inline clearfix",
             'altnames':"field field-name-field-alternate-names field-type-"+\
             "text-long field-label-inline clearfix",
             'loc':"field field-name-field-region field-type-"+\
             "text-with-summary field-label-inline clearfix",
             'status':"field field-name-language-status field-type-"+\
             "ds field-label-inline clearfix"}


import udhr, odin, omniglot
from miniethnologue import WIKI2ISO, ISO2LANG

wikilangs = [WIKI2ISO[i] for i in WIKI2ISO if WIKI2ISO[i] and WIKI2ISO[i] in ISO2LANG]
langs_we_have = sorted(set(udhr.languages() + odin.languages() + omniglot.languages() + wikilangs))

lf = defaultdict(list)
for i in _lf:
  for j in _lf[i]:
    try:
      infile = codecs.open(parentddir+"/data/ethnologue/languages/"+j+'.ethno','r','utf8').read()
    except IOError:
      if j in langs_we_have: print i, j
      continue
    site = bs(infile)
    name = site.find('title').text.replace(' | Ethnologue','').strip()
    try:
      pop = site.find(attrs={"class": ethno['pop']}).find(attrs={"class": 'even'}).text.strip()
    except AttributeError:
      pop = None  
    status = site.find(attrs={"class": ethno['status']}).find(attrs={"class": 'even'}).text.strip()
    try:
      loc = site.find(attrs={"class": ethno['loc']}).find(attrs={"class": 'even'}).text.strip()
    except AttributeError:
      loc = None
    try:
      altnames = site.find(attrs={"class": ethno['altnames']}).find(attrs={"class": 'even'}).text.strip()
    except AttributeError:
      altnames = None
    lf[j].append((i, name, pop, altnames, loc, status))
    
with codecs.open(ETHNO_DIR+langfamfile,'wb') as fout:
  pickle.dump(lf, fout)
'''



def language_families():
  langfam = pickle.load(codecs.open(ETHNO_DIR+\
                                  'languagefamilies_with_info.pk','rb'))
  return langfam

langfam = language_families()
ISO2FAMILY = {i:langfam[i][0][0] for i in langfam}
FAMILIES2ISO = defaultdict(list)
for i in langfam:
  FAMILIES2ISO[langfam[i][0][0]].append(i)



