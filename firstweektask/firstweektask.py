from util import * 

def method1(text):
  return word_tokenize(text)

def method2(infile, outfile):
  fdist = FreqDist()
  for line in open(infile,'r'):
    fdist.update(word_tokenize(line))
  with open(outfile,'w') as fout:
    for i in fdist:
      print>>fout, i+"\t"+str(fdist[i])
  return fdist

def method3(text):
  lang = ("Indo-European","English")
  print "The language of the sentence is most probably: {1} ({0})".format(lang[0],lang[1])
  return lang

