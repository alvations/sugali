# -*- coding: utf-8 -*-

# Access modules from parent dir, see http://goo.gl/dZ5HVk
import os, sys
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)


import codecs, os, zipfile, urllib, urllib2, tempfile, shutil, re, io
from unicodize import is_utf8, what_the_encoding
from utils import make_tarfile, read_tarfile

def get_from_unicodedotorg(testing=False):
  """ Crawl and clean UDHR files from www.unicode.org . """
  TEMP_RAW_DIR = tempfile.mkdtemp()
  UDHR_DOWNLOAD = 'http://www.unicode.org/udhr/d/'
  AHREF_REGEX = '<a href="?\'?([^"\'>]*)'
  
  # Makes a temp output directory for the files that can be converted into utf8.
  UDHR_UTF8_DIR = './udhr-utf8/' # for saving the temp udhr files.
  if not os.path.exists(UDHR_UTF8_DIR):
    os.makedirs(UDHR_UTF8_DIR)
  # Get the directory page from the www.unicode.org UDHR page
  unicode_page = urllib.urlopen(UDHR_DOWNLOAD).read()
  # Crawls the www.unicode.org page for all udhr txt files.
  for i in re.findall(AHREF_REGEX,unicode_page):
    if i.endswith('.txt'):
      print UDHR_DOWNLOAD+i
      urllib.urlretrieve(UDHR_DOWNLOAD+i, filename=TEMP_RAW_DIR+i)
      with io.open(TEMP_RAW_DIR+i,'r',encoding='utf8') as udhrfile:
        # Gets the language from the end of the file line.
        lang = udhrfile.readline().partition('-')[2].strip()
        # Gets the language code from the filename.
        langcode = i.partition('.')[0].partition('_')[2]
        # Skip the header lines.
        for _ in range(5): udhrfile.readline();
        # Reads the rest of the lines and that's the udhr data.
        the_rest = udhrfile.readlines()
        data = "\n".join([i.strip() for i in the_rest if i.strip() != ''])
        ##print langcode, data.split('\n')[0]
        with codecs.open(UDHR_UTF8_DIR+'udhr-'+langcode+'.txt','w','utf8') as outfile:
          print>>outfile, data
      if testing:
        break

  if testing:
    # Compress the utf8 UDHR files into a single tarfile in the test dir.
      try:
        make_tarfile('../test/udhr-unicode.tar',UDHR_UTF8_DIR)
      except IOError:
        # if function is called within the sugarlike/src/universalcorpus dir
        # To move up directory to access sugarlike/data/ and sugarlike/test/.
        make_tarfile('../../test/udhr-unicode.tar',UDHR_UTF8_DIR)
      
  else:
    # Compresses the utf8 UDHR files into a single tarfile.
    try:
      make_tarfile('../data/udhr/udhr-unicode.tar',UDHR_UTF8_DIR)
    except IOError:
      # if function is called within the sugarlike/src/universalcorpus dir
      # To move up directory to access sugarlike/data/ and sugarlike/test/.
      make_tarfile('../../data/udhr/udhr-unicode.tar',UDHR_UTF8_DIR)  
  # Remove the udhr-utf8 directory.
  shutil.rmtree(UDHR_UTF8_DIR)

def enumerate_udhr(intarfile):
  """
  Returns the number of languages in a defaultdict(list). If language(s) has
  dialects/registers in the UDHR, len(enumerate_udhr(intarfile)[lang]) > 1 .
  
  # USAGE:
  >>> ls = enumerate_udhr('../data/udhr/udhr-unicode.tar')
  >>> for i in sorted(ls):
  >>>   print i, ls[i]
  >>> print len(ls) # Number of languages
  """
  from collections import defaultdict
  import tarfile
  TEMP_DIR = tempfile.mkdtemp()
  # Reads the tarfile and extract to temp directory.
  with tarfile.open(intarfile) as tf:
    for member in tf.getmembers():
      tf.extract(member, TEMP_DIR)
  languages = defaultdict(list)
  # Loop through temp directory.
  for infile in os.listdir(TEMP_DIR):
    lang = infile.partition('.')[0].lower()
    try:
      lang, dialect = lang.split('_') # Checks for dialects denoted by "_".
      languages[lang].append(dialect)
    except:
      languages[lang].append(lang)
  return languages

def documents(intarfile=parentddir+'/data/udhr/udhr-unicode.tar', \
              bysentence=False):
  """ Yields UDHR by documents. """
  for infile in read_tarfile(intarfile):
    #language = infile.split('/')[-1][:3]
    language = infile.split('/')[-1].split('-')[1].split('.')[0].split('_')[0]
    with codecs.open(infile,'r','utf8') as fin:
      if bysentence:
        for sentence in fin.readlines():
          yield language, sentence
      else:
        yield language, fin.read()
        
def sents(intarfile=parentddir+'/data/udhr/udhr-unicode.tar', \
          bysentence=True):
  return documents(intarfile, bysentence)

def source_sents(intarfile=parentddir+'/data/udhr/udhr-unicode.tar', \
          bysentence=True):
  return sents(intarfile, bysentence)

def languages():
  """ Returns a list of available languages from original data source. """
  langs = enumerate_udhr(intarfile=parentddir+ '/data/udhr/udhr-unicode.tar')
  return langs

def num_languages():
  """ Returns the number of languages available from original data source. """
  return len(languages())