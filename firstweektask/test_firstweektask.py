import firstweektask as fwt
import unittest as ut
import tempfile
import codecs
import os

class testfwt (ut.TestCase):
  testsentences = [("This is a foo bar sentence",
                    ["This", "is", "a", "foo", "bar", "sentence"],
                    ("Indo-European","English")),                   
                   ("Ich bin schwanger?",
                    ["Ich","bin","schwanger","?"],
                    ("Indo-European","German")),
                   ("Ja, das ist nicht fett.",
                    ["Ja",",","das","ist","nicht","fett","."],
                    ("Indo-European","German")),
                   ("Das ist ein Baby.",
                     ["Das","ist", "ein","Baby","."],
                    ("Indo-European","German"))
                   ]
  tokencounts = [("This", 1),
                 ("is", 1),
                 ("a", 1),
                 ("foo", 1),
                 ("bar", 1),
                 ("sentence", 1),
                 ("Ich", 1),
                 ("bin", 1),
                 ("schwanger", 1),
                 ("Ja", 1),
                 ("das", 1),
                 ("ist", 2),
                 ("nicht", 1),
                 ("fett", 1),
                 ("Das", 1),
                 ("ein", 1),
                 ("Baby", 1),
                 (".", 2),
                 ("?", 1),
                 (",", 1)
                 ]
  
  def testMethod1(self):
    for sentence, tokens, _ in self.testsentences:
      result = fwt.method1(sentence)
      self.assertEqual(tokens, result)
      
  def testMethod2(self):
    tmpoutfile = tempfile.mkstemp()[1]
    tmpinfile = tempfile.mkstemp()[1]

    with open(tmpinfile, 'w') as infile:
      for sentence, tokens, _ in self.testsentences:
        infile.write(sentence + '\n')
     
    expected_lines = []
    for token, num in self.tokencounts:
      expected_lines.append(token + "\t" + str(num))
                  
    fwt.method2(tmpinfile, tmpoutfile)
    lines = []
    with codecs.open(tmpoutfile, 'r') as out:
      for line in out:
        lines.append(line.strip('\n'))

    self.assertEqual(set(lines), set(expected_lines))
    os.remove(tmpinfile)
    os.remove(tmpoutfile)

  def testMethod3(self):  # We don't need to test if the language is correct, since the system will never be perfect. 
    for sentence, _, language in self.testsentences:
      prediction = fwt.method3(sentence)
      self.assertEqual(len(prediction),2)
      self.assertIsInstance(prediction[0],str)
      self.assertIsInstance(prediction[1],str)
      
if __name__ == "__main__":
  ut.main()