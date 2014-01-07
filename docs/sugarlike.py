# -*- coding: utf-8 -*-

import sys; reload(sys); sys.setdefaultencoding("utf-8")

import codecs, os
from unicodize import is_utf8, what_the_encoding

udhr = 'udhr/'
encodingprobs = codecs.open('encoding-problems', 'w','utf8')
udhrutf8 = 'udhr-utf8/'

for filename in os.listdir(udhr):
  #if not filename.endswith("-UTF8"): continue;
  encoding = what_the_encoding(udhr+filename)
  if encoding.startswith('unknown') or encoding == "binary":
    print>>encodingprobs, filename+"\t"+ encoding 
    continue;
  with codecs.open(udhr+filename,'r',encoding) as fin:
    try:
      text = fin.read()
      #filename = filename.rpartition("-")[0]
      #print filename
      print>>codecs.open(udhrutf8+filename,'w','utf8'), \
              text.encode('utf8').strip()
      #print filename, encoding, text.encode('utf8').strip()
    except:
      #print filename
      print>>encodingprobs, filename+"\t"+encoding
      
stuff = codecs.open('rere-encode','w','utf8')
for probfile in codecs.open('encoding-problems','r','utf8'):
  #print probfile
  prob, magic_encoding =  probfile.strip().split('\t')
  given_encoding = prob.rpartition("-")[2].lower()
  if given_encoding[-1].isdigit():
    given_encoding = given_encoding[:-1] +"-" + given_encoding[-1]
  try:
    lines = codecs.open(udhr+prob,'r',given_encoding).read()
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    lines = lines.replace(u"","").replace(u"","").replace(u"","")
    #print>>stuff, lines.encode('utf8')
    #print prob #, magic_encoding, given_encoding, #lines.encode('utf8')
    #filename = filename.rpartition("-")[0]
    print>>codecs.open(udhrutf8+filename,'w','utf8'), \
              text.encode('utf8').strip()
  except:
    #print prob, magic_encoding, given_encoding
    pass
