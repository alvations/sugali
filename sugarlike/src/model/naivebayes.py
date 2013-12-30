# -*- coding: utf-8 -*-
  
from nltk import NaiveBayesClassifier as nbc
from extractfeature import extract_features_from_tarfile, ISO2LANG, sentence2ngrams
import cPickle as pickle
import codecs, operator, math
from collections import Counter, defaultdict
from probability import arithmetic_mean, geometric_mean, arigeo_mean

def train_nbc(train=True):
  '''
  data_source = {'odin':'../../data/odin/odin-cleaner.tar',
                'udhr':'../../data/udhr/udhr-unicode.tar',
                'omniglotphrase':'../../data/omniglot/omniglotphrases.tar'}
  '''
  data_source = {'udhr':'../../data/udhr/udhr-unicode.tar'}
  featuresets = []
  for s in data_source:
    for lang, sent in extract_features_from_tarfile(data_source[s]):
      if lang in ISO2LANG:
        featuresets += [({'3gram':i},lang) for i in sentence2ngrams(sent)]
        print len(featuresets)
  
  if train:
    return nbc.train(featuresets)
  else:
    with codecs.open('3grams-featuresets.pk','wb') as fout:
      pickle.dump(featuresets, fout)
    
#sugarlike = train_nbc()
#with codecs.open('3gram-udhr.pk','wb') as fout:
#  pickle.dump(sugarlike, fout)
  


#fs = train_nbc(train=False)

'''
with codecs.open('3grams-featuresets.pk','rb') as fin2: 
  fs = pickle.load(fin2)
  langfeat = Counter()
  for i in fs:
    lang = i[1]
    langfeat[lang]+=1
  for i in langfeat:
    print i, langfeat[i]
'''
    

    
def test(test_sentence, classifier, option=''):
  classes = defaultdict(list)
  test_features = [{'3gram':i} for i in sentence2ngrams(test_sentence)]
  
  # Classify features from test_sentence.
  for i in test_features:
    result = classifier.prob_classify(i); best = result.max()
    classes[best].append(result.prob(best))
  
  # Calculate the scores of the classified features from the test_sentence.
  answers = {}
  if option[:3] == 'geo': # geometric mean
    for i in classes:
      answers[i] = geometric_mean(classes[i])
  elif option[:3] == 'ari': # arithmetic mean
    for i in classes:
      answers[i] = arithmetic_mean(classes[i])
  else: # use arithmetic-geometric mean, see 
    for i in classes:
      answers[i] = arigeo_mean(classes[i])
  return max(answers.iteritems(), key=operator.itemgetter(1))[0], answers

# Informal train / test
''' 
# To train and dump tagger into pickle.
#sugarlike = train_nbc()
#with codecs.open('3gram-sugarlike.pk','wb') as fout:
#  pickle.dump(sugarlike, fout)

tester = ""
# To test and tag the tagger into pickle
with codecs.open('3gram-sugarlike.pk','rb') as fin2: 
  sugarlike = pickle.load(fin2)
  print test(tester, sugarlike)
  #print test('Ich bin schwanger',sugarlike)
  #print test('Ich bin schwanger',sugarlike, option='geo')
  #print test('Ich bin schwanger',sugarlike, option='ari')
  #print len(sugarlike.labels())
'''