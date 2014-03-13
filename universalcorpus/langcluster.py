# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from itertools import chain
from threading import Thread
from Queue import Queue

import numpy as np
from sklearn import cluster

from crawlandclean import odin, omniglot, udhr

def word2ngrams(text, n=3, exact=True):
  """ Convert text into character ngrams. """
  return [text[i:i+n] for i in range(0, len(text)+1-n)]

def generate_ngrams(data_source):
  ngrams = defaultdict(Counter)
  for lang, sent in globals()[data_source].source_sents():
    ngrams[lang].update(list(chain(*[word2ngrams(i) 
                                     for i in sent.lower().split()])))
  return ngrams

data_sources = ['odin','omniglot','udhr']


# Parallel processing hocus-pocus. 
def wrapper(func, arg, queue):
  """" Wrapper class for multi-threaded functions """
  queue.put(func(arg))

q1, q2, q3 = Queue(), Queue(), Queue()
Thread(target=wrapper, args=(generate_ngrams, data_sources[0], q1)).start() 
Thread(target=wrapper, args=(generate_ngrams, data_sources[1], q2)).start() 
Thread(target=wrapper, args=(generate_ngrams, data_sources[2], q2)).start()
odin_ngrams = q1.get(); omniglot_ngrams = q2.get(); udhr_ngrams = q3.get()

# Combining the ngrams.
allngrams = defaultdict(Counter)
for k,v in chain(odin_ngrams.iteritems(), omniglot_ngrams.iteritems(), 
                 udhr_ngrams.iteritems()):
  allngrams[k].update(v)

# Casting inputs into numpy arrays.
all_features = list(set(chain(*[allngrams[i].keys() for i in allngrams])))
languages = []; data = []
for lang, ng in sorted(allngrams.iteritems()):
  languages.append(lang)
  data.append([ng[i] for i in all_features])
langauges = np.array(languages)
train = np.array(data)
# Feeding arrays to sklearn.
k_means = cluster.KMeans(n_clusters=20)
k_means.fit(data)

fout = codecs.open('cluster.out','w','utf8')
fout2 = codecs.open('cluster-tag.out','w','utf8')
print>>fout, k_means.labels_.tolist()
print>>fout2, languages.tolist()
