# -*- coding: utf-8 -*-



import codecs, urllib2,re
from bs4 import BeautifulSoup as bs
import urllib2
from collections import defaultdict
import cPickle as pickle

fin = codecs.open('ethnologue-family.html','r','utf8')
ethnologue_domain = "http://www.ethnologue.com/"

language_families = defaultdict(list)

for line in fin.readlines():
  if  '''<div class="views-field views-field-name">''' in line:
    langfamlink = bs(line).find('a').get('href')
    langfamily = bs(line).get_text().strip()
    #print langfamily, langfamlink
    for line2 in urllib2.urlopen(langfamlink):
      if '''<span class="views-field views-field-field-iso-639-3">''' in line2:
        langlink = ethnologue_domain+bs(line2).find('a').get('href')
        lang = bs(line2).get_text().strip()
        langname = re.sub(r'[\[\(][^)]*[\]\)]', '', lang)
        isocode = re.findall(r'\[([^]]*)\]',lang)[0]
        geo = re.findall(r'\([^)]*\)',lang)[0].rpartition(" ")[2][:-1]
        language_families[langfamily].append((isocode, langname , geo))
    break

with codecs.open('languagefamilies','wb') as fout:
  pickle.dump(language_families, fout)

with codecs.open('languagefamilies','rb') as fin2: 
  language_families = pickle.load(fin2)
  for lf in language_families:
    for l in language_families[lf]:
      print lf, l
