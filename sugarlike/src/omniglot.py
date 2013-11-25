# -*- coding: utf-8 -*-

import urllib2, re, time, codecs, os, random
from bs4 import BeautifulSoup as bs
from collections import defaultdict

OMNIGLOT = 'http://www.omniglot.com'
HTTP_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|'+\
                '(?:%[0-9a-fA-F][0-9a-fA-F]))+'
AHREF_REGEX = '<a href="?\'?([^"\'>]*)'
  
def crawl_omniglot():
  """ Full crawl within the omniglot domain."""
  homepage = urllib2.urlopen(OMNIGLOT).read()
  crawled = []
  
  for i in re.findall(AHREF_REGEX,homepage):  
    if not i.startswith("http://") and not i.endswith("/") and \
    not i.startswith('https://'): 
      if OMNIGLOT+i not in crawled:
        print OMNIGLOT+i
        x = urllib2.urlopen(OMNIGLOT+i).read()
        filename = (OMNIGLOT+i).rpartition('/')[2]
        print filename
        print>>codecs.open('../data/omniglot/'+filename,'w','utf8'), x 
        time.sleep(random.randrange(5,10))
        crawled.append(OMNIGLOT+i)

# Multilingual pages in Omniglot.
MULTILING_URLS = {
'phrase_lang':"http://www.omniglot.com/language/phrases/langs.htm", # Parsable.
'babel':"http://www.omniglot.com/babel/index.htm", # Parsable.

'continent':'http://www.omniglot.com/countries/continents.htm', # Single page.
'color':"http://www.omniglot.com/language/colours/index.php", # Single page.
'dwarf':"http://www.omniglot.com/language/names/7dwarfs.htm", # Single page.
'omni':"http://www.omniglot.com/language/omniglot.htm", # Single page.
'twister':"http://www.omniglot.com/language/tonguetwisters/index.htm", # Single.
'idiom':"http://www.omniglot.com/language/idioms/index.php", # Single page.
'multisong':'http://www.omniglot.com/songs/multilingual/index.php', # 3 songs.
'prov':"http://www.omniglot.com/language/proverbs/language.htm", # Single pages,

'num':"http://www.omniglot.com/language/numbers/index.htm", # Irregular pages.
'country': 'http://www.omniglot.com/countries/', # Irregular pages.
'kinship':"http://www.omniglot.com/language/kinship/index.htm", # Irregular pages. 
'song':"http://www.omniglot.com/songs/index.php" # Irregular pages.
}

def get_phrases(with_mp3=False, outputdir='../data/omniglot/'):
  """ Gets phrases list from Omniglot. """
  # Downloads and open the phrases index.htm on Omniglot.
  phrase_lang = urllib2.urlopen(MULTILING_URLS['phrase_lang']).read()
  for i in re.findall(AHREF_REGEX,phrase_lang):
    # Finds all link for the phrases page for each language.
    if '/language/phrases/' in i and not i.endswith('index.htm'):
      # Get name of language in English.
      langname = i.rpartition('/')[2].strip().rpartition('.')[0]
      # Create a textfile for the output.
      outfile = codecs.open(outputdir+'phrases.'+langname,'w','utf8')
      # Finds the section that starts with <div id="unicode">
      soup = bs(urllib2.urlopen(OMNIGLOT+i).read()).find_all(id='unicode')[0]
      # Get name of language in the particular language.
      langname2 = bs(str(soup.find_all('th')[1])).text
      all_phrases = defaultdict(list)
      # Each <tr>...</tr> is a phrase in the table.
      for phrases in soup.find_all('tr'):
        try:
          # Each <td>...</td> is a column in the <tr/>.
          eng,phrase =  bs(unicode(phrases)).find_all('td')
          eng = str(eng.text)
          if with_mp3:
            # Maps the phrase to the corresponding mp3.
            phrase_mp3 = zip([i.strip() for i in \
                              unicode(phrase.text).split('\n') if i != ''],
                             re.findall(AHREF_REGEX,str(phrase)))
            all_phrases[eng]+=phrase_mp3
          else:
            all_phrases[eng]+=[i.strip() for i in \
                          unicode(phrase.text).split('\n') if i.strip() != '']
        except ValueError:
          pass
        
      # Outputs to file.
      for gloss in all_phrases:
        eng = gloss.replace('\n  ',' ').strip()
        for trg in all_phrases[gloss]:
          if type(trg) is tuple:
            trg = "\t".join(trg)
          print>>outfile, eng+"\t"+trg
      time.sleep(random.randrange(5,10))

def get_num_pages():
  """ Returns a list of linked pages from Omniglot's numbers page"""
  NUMBERS = "http://www.omniglot.com/language/numbers/"
  num = urllib2.urlopen(MULTILING_URLS['num']).read()
  return list(set([NUMBERS+str(re.findall(AHREF_REGEX,str(i))[0]) \
          for i in bs(num).find_all('dd')]))  

