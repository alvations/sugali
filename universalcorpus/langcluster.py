# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from itertools import chain
from operator import itemgetter
from threading import Thread
from Queue import Queue
import time, os, ast, random

import numpy as np
import pandas as pd
from sklearn import cluster
import milk

from crawlandclean import odin, omniglot, udhr
from utils import normalize

random.seed(0)

def word2ngrams(text, n=3):
  """ Convert word into character ngrams. """
  return [text[i:i+n] for i in range(len(text)-n+1)]

def sent2ngrams(text, n=3):
  """ Convert sentence into character ngrams. """
  return list(chain(*[word2ngrams(i,n) for i in text.lower().split()]))

def generate_ngrams(data_source):
  ngrams = defaultdict(Counter)
  for num in range(2,4):
    for lang, sent in globals()[data_source].source_sents():
      _counter = normalize(Counter(sent2ngrams(sent,num))) ## TODO: normalize all ngrams in the 
      if _counter:
        ##print data_source, num, _counter
        ngrams[lang]+= _counter
    x = normalize(Counter(sent.split()))
    if x: ngrams[lang]+=x
  print data_source
  return ngrams

def wrapper(func, arg, queue):
  """" Wrapper class for multi-threaded functions """
  queue.put(func(arg))

def load_ngram_array():
  if os.path.exists('language.tag') and \
  os.path.exists('tocluster.data.npy') and \
  os.path.exists('all_features'):
    data = np.load('tocluster.data.npy')
    languages = ast.literal_eval(open('language.tag','r').read())
    all_features = codecs.open('all_features','r','utf8').read().split()
    return data, languages, all_features
  else:
    print "Accessing data..."
    data_sources = ['odin','omniglot','udhr']
    # Parallel processing hocus-pocus.     
    q1, q2, q3 = Queue(), Queue(), Queue()
    Thread(target=wrapper, args=(generate_ngrams, data_sources[0], q1)).start() 
    Thread(target=wrapper, args=(generate_ngrams, data_sources[1], q2)).start() 
    Thread(target=wrapper, args=(generate_ngrams, data_sources[2], q3)).start()
    odin_ngrams = q1.get(); omniglot_ngrams = q2.get(); udhr_ngrams = q3.get()
    
    # Combining the ngrams.
    print "combining ngrams..."
    allngrams = defaultdict(Counter)
    for k,v in chain(odin_ngrams.iteritems(), omniglot_ngrams.iteritems(), 
                     udhr_ngrams.iteritems()):
      allngrams[k].update(v)
    
    # Casting inputs into numpy arrays.
    print "casting to numpy arrays",
    start = time.time()
    all_features = sorted(set(chain(*[allngrams[i].keys() for i in allngrams])))
    languages = []; data = []
    for lang, ng in sorted(allngrams.iteritems()):
      languages.append(lang)
      x = [ng[i] for i in all_features]
      data.append(x)
    
    data = pd.lib.to_object_array(data).astype(float) # converts counters to array.
    print>>open('language.tag','w'), languages
    np.save('tocluster.data',data)
    print>>codecs.open('all_features','w'), " ".join(all_features)
    print time.time() - start
    return data, languages, all_features

# TODO: combine ngrams counts 1-5 + words.
data, languages, all_features = load_ngram_array()

print "clustering..."

''' # Kmeans using sklearn.
k_means = cluster.KMeans(n_clusters=20)
k_means.fit(data)
print k_means.labels_.tolist()
'''

# Kmeans using milk.
cluster_ids, centroids = milk.kmeans(data, 20)

clusters = cluster_ids.tolist()
print set(clusters), len(set(clusters))
print clusters
print languages
print all_features


def distance(counter1, counter2):
  """
  Calculates the dot product, assuming NORMALIZED.
  """
  dp = 0
  for x in counter1.keys().intersection(counter2.keys()):
    dp += counter1[x]*counter2[x]
  return dp

