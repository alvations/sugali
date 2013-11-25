# -*- coding: utf-8 -*-

import codecs, os, zipfile, urllib, urllib2, tempfile, shutil
from unicodize import is_utf8, what_the_encoding
from utils import make_tarfile

def convert_udhr_to_utf8(testing=False):
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
        print infile, encoding 
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
        print infile, given_encoding
  
  if testing:
    # Compress the utf8 UDHR files into a single tarfile in the test dir.
    make_tarfile('../test/udhr-utf8.tar','../data/udhr-utf8/')
  else:
    # Compresses the utf8 UDHR files into a single tarfile.
    make_tarfile('../data/udhr/udhr-utf8.tar','../data/udhr-utf8/')
  # Remove the udhr-utf8 directory.
  shutil.rmtree(UDHR_UTF8_DIR)