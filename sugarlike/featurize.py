# -*- coding: utf-8 -*-

import tarfile, tempfile, os, codecs
import cPickle as pickle
from collections import defaultdict, Counter

from extractfeature import sentence2ngrams
from universalcorpus import odin, omniglot, udhr
from universalcorpus.miniethnologue import ISO2LANG

data_source = ['odin','omniglot','udhr']

datalost = set()
for src in data_source:
  charngrams = defaultdict(Counter)
  wordfreqs = defaultdict(Counter)
  for lang, sent in globals()[src].source_sents():
    print src, lang
    if lang in ISO2LANG:
      for n in range(1,5):        
        charngrams[lang]+= Counter(sentence2ngrams(sent, n, 'char', True))
      wordfreqs[lang]+=Counter(sent.split())
    else:
      datalost.add((src, lang))
'''
  with codecs.open(src+'-char.pk','wb') as fout:
    pickle.dump(charngrams, fout)
  with codecs.open(src+'-word.pk','wb') as fout:
    pickle.dump(charngrams, fout)
'''