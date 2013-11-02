import firstweektask as fwt
import unittest as ut

class testfwt (ut.TestCase):
  testsentences = [("This is a foo bar sentence",
                    ["This", "is", "a", "foo", "bar", "sentence"]),                   
                   ("Ich bin schwanger?",
                    ["Ich","bin","schwanger","?"]),
                   ("Ya, das ist nicht fett.",
                    ["Ya",",","das","ist","nicht","fett","."]),
                   ("Das ist baby.",
                     ["Das","ist","baby","."])
                   ]
  
  def testMethod1(self):
    for sent,tokens in self.testsentences:
      result = fwt.method1(sent)
      self.assertEqual(tokens, result)
      
if __name__ == "__main__":
  ut.main()