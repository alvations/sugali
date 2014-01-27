# -*- coding: utf-8 -*-

def check_data_integrity(data_source="all", remove=True):
  """
  Remove and repickle the extracted feature files and count:
  i.   no. of languages in original source data
  ii.  no. of languages in extracted features  
  """
  import os, glob
  from extractfeature import get_features
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
    print "%s-word.pk contains data for %d Languages.\n" % (i,len(wordfreq)) 

def feature_count():
  """
  Measures skew-ness of features.
  """
  pass


check_data_integrity('odin', remove=False)
check_data_integrity('omniglot', remove=False)
check_data_integrity('udhr', remove=False)