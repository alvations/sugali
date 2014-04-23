# -*- coding: utf-8 -*-

import cPickle as pickle
import time, os, ast, random, codecs

from math import sqrt, acos
from collections import Counter, defaultdict
from itertools import chain, product
from operator import itemgetter
from threading import Thread
from Queue import Queue

import numpy as np
import pandas as pd
##from sklearn import cluster; import milk
import scipy
import scipy.spatial
import scipy.cluster
import matplotlib.pylab as plt

from crawlandclean import odin, omniglot, udhr, ethnologue
from miniethnologue import ISO2LANG, MACRO2LANG, RETIRED2ISO
from evaluate import normalise

random.seed(0)

def word2ngrams(text, n=3):
  """ Convert word into character ngrams. """
  return [text[i:i+n] for i in range(len(text)-n+1)]

def sent2ngrams(text, n=3):
  """ Convert sentence into character ngrams. """
  return list(chain(*[word2ngrams(i,n) for i in text.lower().split()]))


dead = {"osp":"Old Spanish", "odt":"Old Dutch", "goh": "Old High German",
        "got":"Gothic","wlm":"Middle Welsh","oge":"Old Georgian",
        "tpn":"Tupinamba","ojp":"Old Japanese","sga":"Old Irish",
        "hit":"Hittite","tkm":"Takelma","dum":"Middle Dutch",
        "fro":"Old French","nci":"Classical Nahuatl","gmh":"Middle High German",
        "mxi":"Mozarabic"}
macro_split = {"nob":"Norwegian, Bokmaal","nno":"Norwegian Nynorsk"} # nor.
constructed = {"ido":"Ido","tlh":"Klingon","tzl":"Talossan","jbo":"Lojban",
               "ina":"Interlingua"}

living_languages = set(ISO2LANG.keys()) - set(RETIRED2ISO.keys()) \
- set(dead.keys()) - set(constructed.keys()) \
- set(MACRO2LANG.keys()) - set(macro_split.keys())

### Note: We should not just ignore Norwegian!

def generate_ngrams(data_source):
  twograms = defaultdict(Counter) 
  threegrams = defaultdict(Counter)
  unigrams = defaultdict(Counter)
  for lang, sent in globals()[data_source].source_sents():
    if lang not in living_languages:
      continue
    if lang not in living_languages: continue;
    twograms[lang].update(Counter(sent2ngrams(sent,2))) 
    threegrams[lang].update(Counter(sent2ngrams(sent,3)))
    unigrams[lang].update(Counter(["<word>"+i+"</word>" for i in sent.split()]))
  return [twograms, threegrams, unigrams]

def wrapper(func, arg, queue):
  """" Wrapper class for multi-threaded functions """
  queue.put(func(arg))

def load_ngram_array():
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
  unigrams = defaultdict(Counter)
  for k,v in chain(odin_ngrams[2].iteritems(), omniglot_ngrams[2].iteritems(), 
                   udhr_ngrams[2].iteritems()):
    unigrams[k].update(v)
  
  twograms = defaultdict(Counter)
  for k,v in chain(odin_ngrams[0].iteritems(), omniglot_ngrams[0].iteritems(), 
                   udhr_ngrams[0].iteritems()):
    twograms[k].update(v)
  
  threegrams = defaultdict(Counter)
  for k,v in chain(odin_ngrams[1].iteritems(), omniglot_ngrams[1].iteritems(), 
                   udhr_ngrams[1].iteritems()):
    threegrams[k].update(v)
  
  for lang in twograms:
    normalise(twograms[lang], 1/sqrt(3))
    normalise(threegrams[lang], 1/sqrt(3))
    normalise(unigrams[lang], 1/sqrt(3))
    
  allgrams = defaultdict(Counter)
  for k,v in chain(twograms.iteritems(), threegrams.iteritems(), unigrams.iteritems()):
    allgrams[k].update(v)
  
  return allgrams
    
def distance(c1, c2):
  dimsum = sum(c1[i]*c2[i] for i in set(c1.keys()).intersection(c2.keys()))
  if dimsum >= 1.0: 
    ##print dimsum
    return 0
  return acos(dimsum)

def avg(l): return sum(l)/float(len(l));

###########################################################################

# Access subcorpora, extracts ngrams features, normalise counts of ngrams. 
if not os.path.exists('ngram.data'):
  data = load_ngram_array()
  with open('ngram.data','wb') as ngramout:
    pickle.dump(data, ngramout)
else:
  with open('ngram.data','rb') as fin:
    data = pickle.load(fin)

# Calculates distance matrix.
print "Calculating/Loading distance matrix ..."
dmatrix = []
if not os.path.exists('distance.out'):    
  fout = open('distance.out','w')
  for l1,l2 in product(data.keys(), data.keys()):
    dist = distance(data[l1],data[l2])
    dmatrix.append((l1,l2,dist))
    print>>fout, "\t".join([l1, l2, str(dist)])
else:
  for line in open('distance.out','r'):
    l1, l2, dist = line.strip().split('\t')
    dist = float(dist)
    dmatrix.append((l1,l2,dist))

def plot_tree(P, pos=None):
  icoord = scipy.array(P['icoord'])
  dcoord = scipy.array(P['dcoord'])
  color_list = scipy.array(P['color_list'])
  xmin, xmax = icoord.min(), icoord.max()
  ymin, ymax = dcoord.min(), dcoord.max()
  if pos:
    icoord = icoord[pos]
    dcoord = dcoord[pos]
    color_list = color_list[pos]
    
  for xs, ys, color in zip(icoord, dcoord, color_list):
    plt.plot(xs, ys, color)
  plt.xlim(xmin, xmax+0.1*abs(xmax))
  plt.ylim(ymin, ymax+0.1*abs(ymax))
  plt.show()

'''
matrix = {}
labels = []
for l1, l2, dist in dmatrix:
  if l2 == l1:
    continue
  if l1 in living_languages and l2 in living_languages:
    if l2 not in labels: labels.append(l2)
    matrix.setdefault(l1, {})[l2] = dist


matrix = [v.values() for k,v in matrix.iteritems()]
matrix = pd.lib.to_object_array(matrix).astype(float) 
'''

condensed_file = 'distance_condensed.pk'
if not os.path.exists(condensed_file):
  labels = []
  index = {}
  for l1, l2, dist in dmatrix:
    if l1 not in labels:
      index[l1] = len(labels)
      labels.append(l1)
      
  
  matrix = np.zeros((len(labels),len(labels)))
  
  for l1, l2, dist in dmatrix:
    index1 = index[l1]
    index2 = index[l2]
    if l1 == l2:
      continue
    matrix[index1,index2] = dist
    matrix[index1,index2] = dist
  
  condensed = scipy.spatial.distance.squareform(matrix)
  with open(condensed_file,'wb') as f:
    pickle.dump((condensed, labels), f)
  
else:
  with open(condensed_file,'rb') as f:
    condensed, labels = pickle.load(f)

methods = 'single complete average weighted'.split()
criterion = 'inconsistent distance maxclust'.split()

output_file = 'cluster2.eval.outputs'
if os.path.exists(output_file):
  print('Output file already exists! Exiting.')
  exit()

print('Calculating clustering...')
fouteval = open(output_file,'w')
numclust = [150] # [10,20,30,40,50,60,70,80,90,100,110,120,130,147,148]

gold = {}
for lang in labels:
  gold[lang] = ethnologue.FAMILIES2ISO[ethnologue.ISO2FAMILY[lang]]
  gold[lang] = set([g for g in gold[lang] if g in living_languages])

for me, cr, nc  in product(methods, criterion, numclust):
  ##print me, cr, nc
  x = scipy.cluster.hierarchy.linkage(condensed, method=me)
  y = scipy.cluster.hierarchy.dendrogram(x)
  plt.savefig('tree.png')
  
  z = scipy.cluster.hierarchy.fcluster(x,nc,cr)
  
  lang2clusters = {}
  cluster2langs = defaultdict(set)
  for cluster_num, lang_labels in zip(z.tolist(), labels):
    lang2clusters[lang_labels] = cluster_num
    cluster2langs[cluster_num].add(lang_labels)
    
  ##fouti = open('induce-clusters','w')
  precisions, recalls, fscores = [], [], []
  #maxoverlap = 0
  for i in labels:
    induced_cluster = cluster2langs[lang2clusters[i]]
    gold_class = gold[i]
    ##print>>fouti, i
    ##print>>fouti, induced_cluster
    ##print>>fouti, gold_class
    ##print>>fouti, "\n"
    overlap = len(induced_cluster.intersection(gold_class))
    ##print overlap, len(gold_class)
    rec = overlap /float(len(gold_class))
    prec = overlap /float(len(induced_cluster))
    
    #maxoverlap = overlap if overlap > maxoverlap else maxoverlap
    
    precisions.append(prec)
    recalls.append(rec)
    fscores.append((2*prec*rec)/float(prec+rec))
  
  print>>fouteval, "\t".join([str(nc), me, cr, "{0:.5f}".format(avg(precisions)), \
                              "{0:.5f}".format(avg(recalls)), \
                              "{0:.5f}".format(avg(fscores))])
  

''' # Kmeans using sklearn.
k_means = cluster.KMeans(n_clusters=20)
k_means.fit(data)
print k_means.labels_.tolist()
'''
'''
# Kmeans using milk.
cluster_ids, centroids = milk.kmeans(data, 20)

clusters = cluster_ids.tolist()
print set(clusters), len(set(clusters))
print clusters
print languages
print all_features
'''
