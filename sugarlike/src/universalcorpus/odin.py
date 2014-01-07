# -*- coding: utf-8 -*-

import sys; sys.path.append('../') # Access modules from parent dir.

import tarfile, codecs, os, re, string, shutil
from collections import defaultdict
import cPickle as pickle
from utils import remove_tags, make_tarfile

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
      print lang
      # Find the <igt>...</igt> in the xml.
      odinfile = tar.extractfile(infile).read()
      igts = bs(odinfile).findAll('igt')
      citations = bs(odinfile).findAll('citation')
      for igt, cite in zip(igts, citations):        
        # Find the <example>...</example> in the igt.
        examples = bs(unicode(igt)).findAll('example')
        cite = remove_tags(unicode(cite)).strip(' &lt;/p&gt;')
        for eg in examples:
          try:
            # Only use triplets lines and assumes that
            # line1: src, line2:eng, line3:gloss
            src, eng, gloss = bs(unicode(eg)).findAll('line')
            src, eng, gloss, cite = map(unicode, [src, eng, gloss, cite])
            docs[lang].append((src, eng, gloss, cite))
            ##print src, eng, gloss, cite
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
 
def pickle2plaintext(testing=False,option='cleanest'):
  """ Converted ODIN IGTs from the .pk file into tab-delimited plaintexts."""  
  # Makes a temp output directory for the individual files.
  TEMPODIN_DIR = './tmpodin/' # for saving the temp udhr files.
  if not os.path.exists(TEMPODIN_DIR):
    os.makedirs(TEMPODIN_DIR)
    
  for language, documents in sorted(load_odin_pickle()):
    tab_igts = []
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
      
      if option == 'cleanest': # Accepts only IGTs without punctuation.
        if src == '' or any(i for i in string.punctuation if i in src):
          continue
      elif option == 'cleaner': # Removes the example number at the end.  
        patterns = [r"\(.{1,}\)",r"[\(\)]"]
        for pat in patterns:
          src = re.sub(pat,'',src)
      else: # Accepts IGTs as they are.
        if src == '':
          continue
      
      # src, eng, gloss, cite = d[0], d[1], d[2], d[3]
      tab_igts.append([words, morphemes, remove_tags(d[1]), \
            remove_tags(d[2]), d[3]])
    if len(tab_igts) > 0:
      with codecs.open(TEMPODIN_DIR+'odin-'+language+'.txt','w','utf8') as fout:
        for igt in tab_igts:
          print>>fout, "\t".join(igt)
    
    if testing:
      break
    
  if testing:
  # Compress the utf8 UDHR files into a single tarfile in the test dir.
    try:
      make_tarfile('../test/odin-'+option+'.tar',TEMPODIN_DIR)
    except IOError:
      # if function is called within the sugarlike/src/universalcorpus dir
      # To move up directory to access sugarlike/data/ and sugarlike/test/.
      make_tarfile('../../test/odin-'+option+'.tar',TEMPODIN_DIR)
  else:
    # Compresses the utf8 UDHR files into a single tarfile.
    try:
      make_tarfile('../../data/odin/odin-'+option+'.tar',TEMPODIN_DIR)
    except IOError:
      # if function is called within the sugarlike/src/universalcorpus dir
      # To move up directory to access sugarlike/data/ and sugarlike/test/.
      make_tarfile('../../data/odin/odin-'+option+'.tar',TEMPODIN_DIR)  
  # Remove the udhr-utf8 directory.
  shutil.rmtree(TEMPODIN_DIR)
