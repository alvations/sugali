# -*- coding: utf-8 -*-

import tarfile, codecs, os
from collections import defaultdict
from bs4 import BeautifulSoup as bs
import cPickle as pickle

ODIN = '../data/odin/odin-full.tar'
ODIN_DIR = '../data/odin/'

def get_odin_examples():
  """
  Extracts the examples from the ODIN igts and returns a defaultdict(list),
  where the keys are the lang iso codes and values are the examples.
  """
  tar = tarfile.open(ODIN)
  docs = defaultdict(list)
  for infile in tar:
    if '.xml' in infile.name: # there's a rogue file in the tar that is not xml.
      lang = infile.name[:-4].lower()
      # Find the <igt>...</igt> in the xml.
      for igt in bs(tar.extractfile(infile).read()).find_all('igt'):
        # Find the <example>...</example> in the igt.
        for eg in bs(unicode(igt)).find_all('example'):
          try:
            # Only use triplets lines and assumes that
            # line1: src, line2:eng, line3:gloss 
            src, eng, gloss = bs(unicode(eg)).find_all('line')
            src, eng, gloss = map(unicode, [src, eng, gloss])
            docs[lang].append((src, eng, gloss))
          except:
            pass; print eg
  return docs

def load_odin_examples():
  """
  Loads languagefamilies.pk and return it as a defaultdict(list).
  
  >>> for lang, examples in load_odin_examples():
  >>>   print lang, examples
  """
  # If odin-docs.pk is not available create it.
  if not os.path.exists(ODIN_DIR+'odin-docs.pk'):
    odindocs = get_odin_examples()
    # Outputs the odin igts examples into '../data/odin/odin-docs.pk'.
    with codecs.open(ODIN_DIR+'odin-docs.pk','wb') as fout:
      pickle.dump(odindocs, fout)
  # Loads the pickled file.
  with codecs.open(ODIN_DIR+'odin-docs.pk','rb') as fin2: 
    docs = pickle.load(fin2)
    for lang in docs:
      # the data might be too much for the RAM, so yield instead of return.
      yield (lang, docs[lang]) 