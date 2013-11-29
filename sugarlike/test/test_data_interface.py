import unittest
import os
from src.data_interface import *

class TestDataInterface(unittest.TestCase):
  wikicode = {'eng':'en','deu':'de'}
  nowikicode = ['aav','ban']
  notiso = ['blablabla']
  wikifiles = ['../data/wikipedia/de/de_1gram.tar']  # Can be changed later

  def test_specific_code(self):
    for iso in self.wikicode.keys():
      self.assertEquals(self.wikicode[iso],specific_code("wikipedia",iso))
    for iso in nowikicode:
      self.assertEquals('',specific_code("wikipedia",iso))
    for iso in notiso:
      self.assertEquals('',specific_code("wikipedia",iso))
  
  def test_get_data(self):
    for filename in self.wikifiles:
      self.assertTrue(os.path.exists(get_data("wikipedia","deu","1gram")))

if __name__ == "__main__":
  unittest.main()