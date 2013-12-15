# -*- coding: utf-8 -*-

import tarfile, codecs, tempfile, os
import sys; sys.path.append('../src/')
from universalcorpus import omniglot, udhr, odin
import ethnologue

def test_tarfile_for_utf8(intarfile):
  """ 
  Checks if tarfile contains readable utf8 files and prints out
  the first file in the tarball. 
  """
  TEMP_DIR = tempfile.mkdtemp()
  with tarfile.open(intarfile) as tf:
    for member in tf.getmembers():
      tf.extract(member, TEMP_DIR)
  
  for infile in os.listdir(TEMP_DIR):
    try:
      print codecs.open(infile,'r','utf8').read()
    except IOError:
      ##print TEMP_DIR+infile
      print codecs.open(TEMP_DIR+'/'+infile,'r','utf8').read()
    break

def test_omniglot_get_phrase():
  """
  The omniglot.get_phrases() function will crawl and clean the multilingual 
  phrases from Omniglot, and saves the resulting tarfile in 
  '../data/omniglot/omniglot-phrases.tar'.
  
  When parameter **testing=True**, a single page will be crawled and the tarfile
  will be output to 'sugarlike/test/omniglot-phrases.tar'.
  
  NOTE: the tarfile is already in the github, please avoid re-running
        this function. Because omniglot's firewall blocks excessive crawling.
  
  P/S: REQUIRES INTERNET CONNECTION to crawl Omniglot!!!
  """
  omniglot.get_phrases(testing=True)
  test_tarfile_for_utf8("omniglot-phrases.tar")
  os.remove("omniglot-phrases.tar")
  
def test_udhr_convert_to_utf8():
  """
  The udhr.convert_to_utf8() function converts the UDHR files from various 
  encodings into utf8, and saves the resulting tarfile in 
  '../data/udhr/udhr-utf8.tar'.
  
  When parameter **testing=True**, the resulting tarfile will be output to 
  'sugarlike/test/udhr-utf8.tar' instead of '../data/udhr/udhr-utf8.tar'.
  
  NOTE: the tarfile is already in the github, please avoid re-running
        this function.
  
  P/S: REQUIRES INTERNET CONNECTION to download the udhr.zip!!!
  """
  ##udhr.convert_to_utf8(testing=True)
  udhr.get_from_unicodedotorg(testing=True)
  test_tarfile_for_utf8("udhr-unicode.tar")
  os.remove("udhr-unicode.tar")
  
def test_load_language_families():
  """
  The load_language_families() function loads the language families from
  languagefamilies.pk and return it as a defaultdict(list). 
  """
  language_families = ethnologue.load_language_families()
  numlang = 0 
  numfam = 0
  for lf in language_families:
    numfam +=1
    for l in language_families[lf]:
      print lf, l
      numlang+=1  
  print "#language_families:",numfam
  print "#language:",numlang

# DEPRECATED.
def test_load_odin_examples():
  """
  The load_odin_examples() function loads the odin igts examples from
  odin-doc.pk and retrn it as a defaultdict(list).
  """
  for lang, examples in odin.load_odin_pickle():
    print lang, examples
    break

test_omniglot_get_phrase()
test_udhr_convert_to_utf8()

#test_load_odin_examples()


#test_load_language_families()


#for lang, examples in odin.load_odin_examples():
#  print examples[0]
#  break


