from collections import Counter
from itertools import chain
from string import punctuation

try:
  from nltk.tokenize import word_tokenize
except ImportError:
  def word_tokenize(text):
    """ Stripped down version of NTLK's word_tokenize. """ 
    for ch in text:
      if ch in punctuation:
        text = text.replace(ch, " "+ch+" ")
    return text.split()

try:
  from nltk.probability import FreqDist
except ImportError:
  class FreqDist(Counter):
    """ Strip down version of NLTK's FreqDist. """
    def __init__(self,corpus):
      if all(isinstance(i, list) for i in corpus):
        _corpus = list(chain(*corpus))# Flatten lists of lists into a single list.
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
