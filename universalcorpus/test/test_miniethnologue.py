# -*- coding: utf-8 -*-


import sys; sys.path.append('../')

import unittest
from miniethnologue import *



class TestMiniethnologue(unittest.TestCase):
  wikicode = {'en':'eng', 'de':'deu', 'zh-min-nan':'nan', 'xyz':None, 'war':'war'} 


  def test_wiki2iso(self):
    for wikicode in self.wikicode.keys():
      self.assertEquals(self.wikicode[wikicode], wikicode2iso(wikicode))
    


if __name__ == "__main__":
  unittest.main()