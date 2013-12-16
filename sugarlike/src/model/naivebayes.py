# -*- coding: utf-8 -*-
  
from nltk import NaiveBayesClassifier as nbc
from extractfeature import extract_features_from_tarfile, ISO2LANG, sentence2ngrams
import cPickle as pickle
import codecs, operator, math
from collections import Counter, defaultdict

def train_nbc():
  data_source = {'odin':'../../data/odin/odin-cleaner.tar',
                'udhr':'../../data/udhr/udhr-unicode.tar',
                'omniglotphrase':'../../data/omniglot/omniglotphrases.tar'}
  
  featuresets = []
  for s in data_source:
    for lang, sent in extract_features_from_tarfile(data_source[s]):
      if lang in ISO2LANG:
        featuresets += [({'3gram':i},lang) for i in sentence2ngrams(sent)]
        print len(featuresets)
  return nbc.train(featuresets)
      
def test(test_sentence, classifier, option='geometric'):
  classes = defaultdict(list)
  test_features = [{'3gram':i} for i in sentence2ngrams(test_sentence)]
  
  # Classify features from test_sentence.
  for i in test_features:
    result = classifier.prob_classify(i); best = result.max()
    classes[best].append(result.prob(best))
  
  answers = {}
  if option[:3] == 'geo': # geometric mean
    for i in classes:
      answers[i] = math.pow(reduce(operator.mul, classes[i], 1), \
                            1/float(len(classes[i])))
      
  elif option[:3] == 'ari': # arithmetic mean
    for i in classes:
      answers[i] = sum(classes[i])/len(classes[i])
      
  else: # use arithmetic-geometric mean
    for i in classes:
      pass
    
  print answers
  return max(answers.iteritems(), key=operator.itemgetter(1))[0]
  
    

#sugarlike = train_nbc()
#with codecs.open('3gram-sugarlike.pk','wb') as fout:
#  pickle.dump(sugarlike, fout)

with codecs.open('3gram-sugarlike.pk','rb') as fin2: 
  sugarlike = pickle.load(fin2)
  print test('Ich bin schwanger',sugarlike)
    