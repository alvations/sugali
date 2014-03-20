# -*- coding: utf-8 -*-

from collections import defaultdict

from crawlandclean import ethnologue
from miniethnologue import ISO2LANG, MACRO2LANG, RETIRED2ISO


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


x = defaultdict(list)
for line in open('distance.out'):
  l1,l2, dist = line.strip().split('\t')
  x[l1].append((dist,l2))
  
precisions, recalls, fscores = [], [], []
for lang in x:
  gold_class = ethnologue.FAMILIES2ISO[ethnologue.ISO2FAMILY[i]]
  gold_class = [g for g in gold_class if g in living_languages]
  induced_cluster = set([i for _,i in sorted(x['eng'][:21])])
  
  overlap = len(induced_cluster.intersection(gold_class))
  rec = overlap /float(len(gold_class))
  prec = overlap /float(len(induced_cluster))
  
  precisions.append(prec)
  recalls.append(rec)
  fscores.append((2*prec*rec)/float(prec+rec))

print "{0:.5f}".format(avg(precisions)), "{0:.5f}".format(avg(recalls)), "{0:.5f}".format(avg(fscores))
  
  