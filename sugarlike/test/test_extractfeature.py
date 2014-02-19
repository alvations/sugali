# -*- coding: utf-8 -*-


#import sys; sys.path.append('../')
import os
parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
import sys; sys.path.append(parentddir)

import unittest
from extractfeature import *



class TestExtractfeature(unittest.TestCase):
  sentence = 'Dies ist ein Beispielsatz zum Extrahieren.'
  
  hallo_trigrams = ['Hal', 'all', 'llo']
  hallo_bigrams = ['Ha', 'al', 'll', 'lo']
  hallo_allgrams = hallo_trigrams + hallo_bigrams + ['H', 'a', 'l', 'l', 'o', 'Hall', 'allo', 'Hallo']
  
  zerograms = []
  trigrams = ['Die', 'ies', 'ist', 'ein', 'Bei', 'eis', 'isp', 'spi', 'pie',
            'iel', 'els', 'lsa', 'sat', 'atz', 'zum', 'Ext', 'xtr', 'tra',
            'rah', 'ahi', 'hie', 'ier', 'ere', 'ren', 'en.']
  onegrams = ['D', 'i', 'e', 's', 'i', 's', 't', 'e', 'i', 'n', 'B', 'e', 'i',
              's', 'p', 'i', 'e', 'l', 's', 'a', 't', 'z', 'z', 'u', 'm', 'E',
              'x', 't', 'r', 'a', 'h', 'i', 'e', 'r', 'e', 'n', '.']
  bigrams = ['Di', 'ie', 'es', 'is', 'st', 'ei', 'in', 'Be', 'ei', 'is', 'sp',
             'pi', 'ie', 'el', 'ls', 'sa', 'at', 'tz', 'zu', 'um', 'Ex', 'xt',
             'tr', 'ra', 'ah', 'hi', 'ie', 'er', 're', 'en', 'n.']
  fourgrams = ['Dies', 'Beis', 'eisp', 'ispi', 'spie', 'piel', 'iels', 'elsa',
               'lsat', 'satz', 'Extr', 'xtra', 'trah', 'rahi', 'ahie', 'hier',
               'iere', 'eren', 'ren.']
  fivegrams = ['Beisp', 'eispi', 'ispie', 'spiel', 'piels', 'ielsa', 'elsat',
               'lsatz', 'Extra', 'xtrah', 'trahi', 'rahie', 'ahier', 'hiere',
               'ieren', 'eren.']
  trigrams_bound = ['<Di', 'Die', 'ies', 'es>', '<is', 'ist', 'st>', '<ei',
                    'ein', 'in>', '<Be', 'Bei', 'eis', 'isp', 'spi', 'pie',
                    'iel', 'els', 'lsa', 'sat', 'atz', 'tz>', '<zu', 'zum',
                    'um>', '<Ex', 'Ext', 'xtr', 'tra', 'rah', 'ahi', 'hie',
                    'ier', 'ere', 'ren', 'en.', 'n.>']
  words = ['Dies', 'ist', 'ein', 'Beispielsatz', 'zum', 'Extrahieren.']
  words_bound = ['<Dies>', '<ist>', '<ein>', '<Beispielsatz>', '<zum>',
               '<Extrahieren.>']
             
               
  def test_word2ngrams(self):
    self.assertEquals(self.hallo_trigrams, word2ngrams('Hallo'))
    self.assertEquals(self.zerograms,      word2ngrams('Hallo', n=7))



  def test_sentence2ngrams(self):
    self.assertEquals(self.trigrams,  sentence2ngrams(self.sentence))
    self.assertEquals(self.onegrams,  sentence2ngrams(self.sentence, n=1))
    self.assertEquals(self.bigrams,   sentence2ngrams(self.sentence, n=2))
    self.assertEquals(self.trigrams,  sentence2ngrams(self.sentence, n=3))
    self.assertEquals(self.trigrams_bound, sentence2ngrams(self.sentence, 
                                                     with_word_boundary=True))
    self.assertEquals(self.trigrams_bound, sentence2ngrams(self.sentence, n=3,
                                                     with_word_boundary=True))
    self.assertEquals(self.words, sentence2ngrams(self.sentence, option='word',
                                                     with_word_boundary=False))

    self.assertEquals((self.onegrams + self.bigrams + self.trigrams + 
                      self.fourgrams + self.fivegrams).sort(), 
                      sentence2ngrams(self.sentence, option='allgrams').sort())
 
   
if __name__ == "__main__":
  unittest.main()
