# -*- coding: utf-8 -*-

import codecs, os, subprocess, sys, re, tempfile
import bz2

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), \
             os.path.pardir))
sys.path.append(parentddir)
from utils import make_tarfile

try:
  from bs4 import BeautifulSoup
except: # TODO: Installation of BeautifulSoup 4 necessary?
  from BeautifulSoup import BeautifulSoup 


def extract_wikipedia(WIKIDUMP_DIR):
  run_wikiextractor(WIKIDUMP_DIR, WIKITEXTS_DIR='../data/wikipedia/texts/')
  print('Wikipedia texts are extracted.')
  clean_wikipedia('../data/wikipedia/texts/')
  print('Wikipedia is cleaned.')



# Extracts all documents (articles) from wikipedia dumps (in WIKIDUMP_DIR)
def run_wikiextractor(WIKIDUMP_DIR, WIKITEXTS_DIR):
  WIKIEXTRACTOR_DIR = '../'
  if not os.path.exists('../data/wikipedia/texts/'):
    os.makedirs('../data/wikipedia/texts/')

  for root, dirnames, filenames in os.walk(WIKIDUMP_DIR):
    for filename in filenames:
      print('extracting ' + filename)
      filepath = os.path.join(root, filename)
      # run WikiExtractor
      process = subprocess.Popen('bzcat ' + filepath + ' | python ' 
                        + WIKIEXTRACTOR_DIR + 'WikiExtractor.py -cb 5000K -o '
                        + WIKITEXTS_DIR + filename , stdout=subprocess.PIPE, 
                                                                   shell=True)
      outputRaw, error = process.communicate()





def clean(s):
    '''Clean a string taken from Wikipedia texts.'''
    # disallow for wikipedia magic words
    # (http://en.wikipedia.org/wiki/Help:Magic_words)
    s = re.sub('__[A-Z]+__', '', s)
    
    # delete all square backets along wiht thier content          
    s = re.sub(' ?\[.*?\]', '', s)

    # delete parentheses that contain no letters           
    s = re.sub(' ?\([\s,;"#\']*?\)', '', s)

    # clean: (, ; 4 ш. до н.э. - 26-36 н.э.) 
    s = re.sub('\([\s,;]+','(', s)

    # delete codice_13, etc.       
    #s = re.sub ('[Cc]odice_\d+', '', s)
    
    # delete formula_1, etc.  
    #s = re.sub ('[Ff]ormula_\d+', '', s)

    # delete newlines     
    s = re.sub('\n+', '\n', s)               
    return s



def clean_wikipedia(wiki_raw_dir):
    '''Clean all files in wiki_raw_dir and write clean files into
       ../data/wikipedia/clean/'''
    if not os.path.exists('../data/wikipedia/'):
        os.makedirs('../data/wikipedia/')

    WIKIPEDIA_CLEAN_DIR = '../data/wikipedia/clean/'
    TEMP_WIKIPEDIA_CLEAN_DIR = tempfile.mkdtemp()

    for root, dirnames, filenames in os.walk(wiki_raw_dir):
        for filename in filenames:
          filepath = os.path.join(root, filename)
          
          # get number for language file
          count = re.search('wiki_([\d]+).bz2', filepath).group(1)  

          # get language code from filepath
          language = re.search('\/([\w]+)wiki-', filepath).group(1)
  
          if not os.path.exists('../data/wikipedia/clean/' + language):
              os.makedirs('../data/wikipedia/clean/' + language)

          print('cleaning ' + filepath)
          with bz2.BZ2File(filepath, 'r') as openZip:
              f = openZip.read()
              
              # closing ref tags without a corresponding opening tag are a 
              # problem for BeautifulSoup3
              #uni_f = re.sub('</[^d]+.*?>', '', f)
              #uni_f = re.sub('</br', '', uni_f)
              
              uni_f = re.sub('<!\[', '', f)
              soup = BeautifulSoup('<docs>' + uni_f + '</docs>')
              doclist = soup.findAll('doc')

              with codecs.open(TEMP_WIKIPEDIA_CLEAN_DIR + '/' + language + '_'
                               + str(count), 'a', 'utf-8') as out:

                  for doc in doclist:
                      content = doc.getText()
                      cleancontent = clean(content.strip())
                      out.write(cleancontent.strip() + '\n')

                  make_tarfile(WIKIPEDIA_CLEAN_DIR + language + '/' + language
                               + '_' + str(count) + '.tar', 
                               TEMP_WIKIPEDIA_CLEAN_DIR + '/' + language + '_'
                               + str(count))




#extract_wikipedia('/media/ec609cb5-510c-467e-9655-5e72e99c4153/wikidumps/')
clean_wikipedia('../data/wikipedia/texts/')
