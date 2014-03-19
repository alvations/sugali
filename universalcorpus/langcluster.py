# -*- coding: utf-8 -*-

from collections import Counter, defaultdict
from itertools import chain, product
from operator import itemgetter
from threading import Thread
from Queue import Queue
import time, os, ast, random,codecs

import numpy as np
import pandas as pd
import h5py
from sklearn import cluster
import milk
from math import sqrt, acos
import cPickle as pickle

from crawlandclean import odin, omniglot, udhr, ethnologue
from miniethnologue import ISO2LANG, MACRO2LANG, RETIRED2ISO

random.seed(0)

def word2ngrams(text, n=3):
  """ Convert word into character ngrams. """
  return [text[i:i+n] for i in range(len(text)-n+1)]

def sent2ngrams(text, n=3):
  """ Convert sentence into character ngrams. """
  return list(chain(*[word2ngrams(i,n) for i in text.lower().split()]))
    
def normalize(featurevector, length=1):
  """
  Normalises a feature vector to a specific length.
  Zero vectors are left zero.
  NOTE: featurevector will be updated with normalized count.
  """
  from math import sqrt
  try:
    ##print length, type(length)
    ##print featurevector.values()
    norm = length / sqrt(sum([x*x for x in featurevector.values()]))
  except ZeroDivisionError:
    return featurevector
  for feat in featurevector:
    featurevector[feat] *= norm
  return featurevector

def generate_ngrams(data_source):
  twograms = defaultdict(Counter) 
  threegrams = defaultdict(Counter)
  unigrams = defaultdict(Counter)
  for lang, sent in globals()[data_source].source_sents():
    twograms[lang].update(Counter(sent2ngrams(sent,2))) ## TODO: normalize all ngrams in the 
    threegrams[lang].update(Counter(sent2ngrams(sent,3)))
    unigrams[lang].update(Counter(["<word>"+i+"</word>" for i in sent.split()]))

  return [twograms, threegrams, unigrams]

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
      twograms[lang] = normalize(twograms[lang], 1/sqrt(3))
      threegrams[lang] = normalize(threegrams[lang], 1/sqrt(3))
      unigrams[lang] = normalize(unigrams[lang], 1/sqrt(3))
    allgrams = defaultdict(Counter)
    for k,v in chain(twograms.iteritems(), threegrams.iteritems(), unigrams.iteritems()):
      allgrams[k].update(v)
    
    return allgrams
    
    '''
    fout = codecs.open('tocluto.data','w','utf8')
    for lang, ng in allngrams.iteritems():
      print>>fout, lang+" "+" ".join(list(chain(*[[feature]*count for feature, count in ng.iteritems()])))
    '''
    '''
    # Casting inputs into numpy arrays.
    print "casting to numpy arrays"
    start = time.time()
    all_features = sorted(set(chain(*[allngrams[i].keys() for i in allngrams])))
    languages = []; data = []
    for lang, ng in sorted(allngrams.iteritems()):
      ##print lang, ng
      languages.append(lang)
      x = [ng[i] for i in all_features]
      data.append(x)
    ##print len(data), len(all_features)
    print "converting to numpy arrays"
    ##data = pd.lib.to_object_array(data).astype(float) # converts counters to array.
    ##data = np.array(data)
    ##np.save('tocluster.data',data)
    ##filearray = h5py.File('sugali.data','w')
    ##data = filearray.create_dataset('tocluster',(len(data),len(data[0])),dtype='f')
    ##data[...] = data
    
    print>>open('language.tag','w'), languages
    print>>codecs.open('all_features','w'), " ".join(all_features)
    print time.time() - start
    '''
    return data, languages, all_features

def distance(c1, c2):
  dimsum = sum(c1[i]*c2[i] for i in set(c1.keys()).intersection(c2.keys()))
  if dimsum >= 1.0: 
    print dimsum
    return 0
  return acos(dimsum)



if not os.path.exists('ngram.data'):
  data = load_ngram_array()
  with open('ngram.data','wb') as ngramout:
    pickle.dump(data, ngramout)
else:
  with open('ngram.data','rb') as fin:
    data = pickle.load(fin)

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
  import matplotlib.pylab as plt
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
    plt.plot(xs, xy, color)
  plt.xlim(xmin010, xmax+0.1*abs(xmax))
  plt.ylim(ymin, ymax+01.*abs(ymaxs))
  plt.show()


dead = {"osp":"Old Spanish", "odt":"Old Dutch", "goh": "Old High German",
        "got":"Gothic","wlm":"Middle Welsh","oge":"Old Georgian",
        "tpn":"Tupinamba","ojp":"Old Japanese","sga":"Old Irish",
        "hit":"Hittite","tkm":"Takelma","dum":"Middle Dutch",
        "fro":"Old French","nci":"Classical Nahuatl","gmh":"Middle High German",
        "mxi":"Mozarabic"}
macro_split = {"nob":"Norwegian, Bokmaal","nno":"Norwegian Nynorsk"} # nor.
constructed = {"ido":"Ido","tlh":"Klingon","tzl":"Talossan","jbo":"Lojban",
               "ina":"Interlingua"}

living_languages = set(ISO2LANG.keys()) - set(RETIRED2ISO.keys()) - set(dead.keys()) - set(constructed.keys()) - set(MACRO2LANG.keys()) - set(macro_split.keys())

matrix = {}
labels = []
for l1, l2, dist in dmatrix:
  if l1 in living_languages and l2 in living_languages:
    if l2 not in labels: labels.append(l2)
    matrix.setdefault(l1, {})[l2] = dist

matrix = [v.values() for k,v in matrix.iteritems()]
matrix = pd.lib.to_object_array(matrix).astype(float) 

import scipy
import matplotlib.pylab as plt
x = scipy.cluster.hierarchy.linkage(matrix, method='weighted')
y = scipy.cluster.hierarchy.dendrogram(x)
plt.savefig('tree.png')

z = scipy.cluster.hierarchy.fcluster(x,148,'maxclust')


lang2clusters = {}
cluster2langs = defaultdict(list)
for i,j in zip(z.tolist(), labels):
  lang2clusters[j] = i
  cluster2langs[i].append(j)

fouti = open('induce-clusters','w')
precisions, recalls, fscores = [], [], []
for i in labels:
  gold_class = ethnologue.FAMILIES2ISO[ethnologue.ISO2FAMILY[i]]
  induced_cluster = set(cluster2langs[lang2clusters[i]])
  print>>fouti, i
  print>>fouti, induced_cluster
  print>>fouti, gold_class
  print>>fouti, "\n"
  overlap = len(induced_cluster.intersection(gold_class))
  rec = overlap /float(len(gold_class))
  prec = overlap /float(len(induced_cluster))
  precisions.append(prec)
  recalls.append(rec)
  fscores.append(2*prec*rec/float(prec/rec))
  
def avg(l):
  return sum(l)/float(len(l))

print avg(precisions), avg(recalls), avg(fscores)
  



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
