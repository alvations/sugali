# -*- coding: utf-8 -*-

try:
  from nltk.tokenize import word_tokenize
except ImportError:
  from string import punctuation
  def word_tokenize(text):
    """ Stripped down version of NTLK's word_tokenize. """ 
    for ch in text:
      if ch in punctuation:
        text = text.replace(ch, " "+ch+" ")
    return text.split()

try:
  from nltk.probability import FreqDist
  pass
except:
  from collections import Counter
  from itertools import chain
  class FreqDist(Counter):
    """ Strip down version of NLTK's FreqDist. """
    def __init__(self, corpus=None):
      if corpus != None:
        if all(isinstance(i, list) for i in corpus):
          # Flatten lists of lists into a single list.
          _corpus = list(chain(*corpus))
        else:
          _corpus = corpus
        self.update(_corpus)
      
      def __iter__(self):
        """ Iterator function: Returns keys of dict. """
        return iter(self.keys())
      
      def __str__(self):
        """ Descriptor function. """
        items = ['%r: %r' % (s, self[s]) for s in self] 
        return '<FreqDist: %s>' % ', '.join(items)
  
def make_tarfile(output_filename, source_dir):
  """ Compress all files into a single tarfile. """
  import os, tarfile
  with tarfile.open(output_filename, "w") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))
    
def remove_tags(text):
  """ Removes <tags> in angled brackets from text. """
  import re
  tags = {i:" " for i in re.findall("(<[^>\n]*>)",text.strip())}
  no_tag_text = reduce(lambda x, kv:x.replace(*kv), tags.iteritems(), text)
  return " ".join(no_tag_text.split())
