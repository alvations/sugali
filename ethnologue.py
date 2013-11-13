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
  line = line.decode('utf-8')
  if  '''<div class="views-field views-field-name">''' in line:
    langfamlink = bs(line).find('a').get('href')
    langfamily = bs(line).get_text().strip()
    print langfamily, langfamlink
    for line2 in urllib2.urlopen(langfamlink):
      line2 = line2.decode('utf-8')
      if '''<span class="views-field views-field-field-iso-639-3">''' in line2:
        lang = bs(line2).get_text().strip()
        if lang.strip() == "": print line2
        langname = re.sub(r'[\[\(\<][^)]*[\]\)\>]', '', lang)
        isocode = re.findall(r'\[([^]]*)\]',lang)[0]
        geo = re.findall(r'\([^)]*\)',lang)[0].rpartition(" ")[2][:-1]
        print isocode, langname , geo
        language_families[langfamily].append((isocode, langname , geo))

with codecs.open('languagefamilies.pk','wb') as fout:
  pickle.dump(language_families, fout)

with codecs.open('languagefamilies.pk','rb') as fin2: 
  language_families = pickle.load(fin2)
  for lf in language_families:
    for l in language_families[lf]:
      print lf, l
