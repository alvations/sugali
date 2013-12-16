# -*- coding: utf-8 -*-

import sys; sys.path.append('../') # Access modules from parent dir.

import codecs, os, zipfile, urllib, urllib2, tempfile, shutil, re, io
from unicodize import is_utf8, what_the_encoding
from utils import make_tarfile

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

get_from_unicodedotorg()

def enumerate_udhr(intarfile):
  """
  Returns the number of languages in a defaultdict(list). If language(s) has
  dialects/registers in the UDHR, len(enumerate_udhr(intarfile)[lang]) > 1 .
  
  # USAGE:
  >>> ls = count_udhr('../data/udhr/udhr-unicode.tar')
  >>> for i in sorted(ls):
  >>>   print i, ls[i]
  >>> print len(ls) # Number of languages
  """
  from collections import defaultdict
  import tarfile
  TEMP_DIR = tempfile.mkdtemp()
  with tarfile.open(intarfile) as tf:
    for member in tf.getmembers():
      tf.extract(member, TEMP_DIR)
  languages = defaultdict(list)
  for infile in os.listdir(TEMP_DIR):
    lang = infile.partition('.')[0].lower()
    try:
      lang, dialect = lang.split('_')
      languages[lang].append(dialect)
    except:
      languages[lang].append(lang)
  return languages

'''
# DEPRECATED: Use instead get_from_unicodedotorg() !!!!
def convert_to_utf8(testing=False):
  """ Converts UDHR files to utf8. """
  # Make temp directories to keep the UDHR files.
  TEMP_DIR = tempfile.mkdtemp() # for keeping the udhr.zip
  TEMP_UDHR_DIR = tempfile.mkdtemp() # for extracting the udhr.
  
  # Downloads and extract the UDHR files into temp directory.
  UDHR_DOWNLOAD = 'http://nltk.googlecode.com/svn/trunk/nltk_data/'+\
                  'packages/corpora/udhr.zip'
  urllib.urlretrieve(UDHR_DOWNLOAD, filename=TEMP_DIR+'udhr.zip')  
  with zipfile.ZipFile(TEMP_DIR+'udhr.zip', "r") as z:
    z.extractall(TEMP_UDHR_DIR)
  TEMP_UDHR_DIR+='/udhr/'
  
  # Makes a temp output directory for the files that can be converted into utf8.
  UDHR_UTF8_DIR = '../data/udhr-utf8/'
  if not os.path.exists(UDHR_UTF8_DIR):
    os.makedirs(UDHR_UTF8_DIR)
  
  # Iterate through the extracted files.
  for filename in os.listdir(TEMP_UDHR_DIR):
    if "~" in filename: continue
    infile = TEMP_UDHR_DIR+filename
    # Uses libmagic to determine the encoding.
    encoding = what_the_encoding(infile)
    # If libmagic doesn't give unknown or binary as encoding.
    if 'unknown' not in str(encoding) and 'binary' not in str(encoding):
      try:
        # Reads the file with encoding specified by libmagic.
        readfile = codecs.open(infile, 'r',encoding).read()
        infile = infile.rpartition("/")[2] 
        # Outputs file into utf8. 
        with codecs.open(UDHR_UTF8_DIR+infile+'.utf8','w','utf8') as outfile:
          print>>outfile, readfile
      except UnicodeDecodeError:
        # Sometimes the file has some chars that cannot be converted into utf8.
        ##print infile, encoding
        pass
    else:
      # If libmagic fails, try the encoding as specified by the filename.
      given_encoding = infile.rpartition('-')[2].lower()
      try:
        # Reads the file with encoding specified by the filename.
        readfile = codecs.open(infile, 'r',given_encoding).read()
        infile = infile.rpartition("/")[2]
        # Outputs file into utf8.
        with codecs.open(UDHR_UTF8_DIR+infile+'.utf8','w','utf8') as outfile:
          print>>outfile, readfile
      except:
        # Sometimes the file has some chars that cannot be converted into utf8.
        ##print infile, given_encoding
        pass
    if testing:
      break
  
  if testing:
    # Compress the utf8 UDHR files into a single tarfile in the test dir.
    make_tarfile('../test/udhr-utf8.tar','../data/udhr-utf8/')
  else:
    # Compresses the utf8 UDHR files into a single tarfile.
    make_tarfile('../data/udhr/udhr-utf8.tar','../data/udhr-utf8/')
  # Remove the udhr-utf8 directory.
  shutil.rmtree(UDHR_UTF8_DIR)
'''
