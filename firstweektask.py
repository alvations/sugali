from util import * 

def method1(text):
  return word_tokenize(text)

def method2(infile, outfile):
  fdist = FreqDist()
  for line in open(infile,'r'):
    fdist.update(word_tokenize(line))
  return fdist

def method3(text):
  lang = "Proto-Indo European: English"
  print "The language of the sentence is most probably",lang
  pass

fd = method2("test1.in", "test1.out")

for i in fd:
  print i
  
# TODO: write test for each method. - LL