# -*- coding: utf-8 -*-

def check_data_integrity(data_source="all", remove=True):
  """
  Remove and repickle the extracted feature files and count:
  i.   no. of languages in original source data
  ii.  no. of languages in extracted features  
  """
  import os, glob
  from extractfeature import get_features
  from universalcorpus import odin, omniglot, udhr, wikipedia
  if remove:
    # Remove all/selected pickled files
    toremove = '*.pk' if data_source == "all" else data_source+"*"
    for i in glob.glob(toremove):
      os.remove(i)
    
  # Rebuild pickled files.
  torebuild = ['odin','omniglot','udhr','crubadan','wikipedia'] \
              if data_source == 'all' else [data_source]
  for i in torebuild:
    print "Accessing features from %s, please wait ..." % (i)
    charngrams,wordfreq = get_features(i, option=None, shutup=True)
    print "%s-word.pk contains data for %d Languages." % (i,len(wordfreq))
    print "Original source contains data for %d Languages" % \
          locals()[i].num_languages()
    missing = set(locals()[i].languages()) - set(wordfreq.keys()) 
    print "Thrown languages:",missing, "\n"

def feature_count():
  """
  Measures skew-ness of features.
  """
  pass


#check_data_integrity('odin', remove=False)
#check_data_integrity('omniglot', remove=False)
#check_data_integrity('udhr', remove=False)

import os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
import sys; sys.path.append(parentddir)
from universalcorpus.miniethnologue import ISO2LANG
from universalcorpus import odin
print len(set([lang for lang, igts in odin.igts() if lang in ISO2LANG]))
  
