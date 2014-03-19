# -*- coding: utf-8 -*-

from crawlandclean import udhr, omniglot, odin, ethnologue
from collections import Counter, defaultdict
from miniethnologue import ISO2LANG, MACRO2LANG, RETIRED2ISO
##from crawlandclean import ethnologue

dead = {"osp":"Old Spanish", "odt":"Old Dutch", "goh": "Old High German",
        "got":"Gothic","wlm":"Middle Welsh","oge":"Old Georgian",
        "tpn":"Tupinamba","ojp":"Old Japanese","sga":"Old Irish",
        "hit":"Hittite","tkm":"Takelma","dum":"Middle Dutch",
        "fro":"Old French","nci":"Classical Nahuatl","gmh":"Middle High German",
        "mxi":"Mozarabic", "ang": "Old English"}
macro_split = {"nob":"Norwegian, Bokmaal","nno":"Norwegian Nynorsk"} # nor.
constructed = {"ido":"Ido","tlh":"Klingon","tzl":"Talossan","jbo":"Lojban",
               "ina":"Interlingua","nov":"Novial"}

alllangs = []
language_families = ethnologue.language_families()
for i in [odin, omniglot, udhr]:
  langs = [j for j in i.languages() if j in ISO2LANG]
  macros = {j:MACRO2LANG[j] for j in langs if j in MACRO2LANG}
  retired = {j:RETIRED2ISO[j] for j in langs if j in RETIRED2ISO}
  splits = [j for j in langs if j in macro_split.keys()] 
  died = [j for j in langs if j in dead.keys()]
  con = [j for j in langs if j in constructed.keys()]
  
  isolangs = list(set(langs)-set(macros.keys())-set(retired.keys())-\
                  set(dead.keys())-set(macro_split.keys())-\
                  set(constructed.keys()))
  alllangs+=isolangs
  
print alllangs
  
  
'''                
  families = list(set([language_families[j][0][0] for j in isolangs]))
  
  endangerment = defaultdict(list)
  for j in isolangs:
    ed = language_families[j][0][-1].split()[0]
    endangerment[ed].append(j)
'''  
  

  ##print len(langs), len(macros), len(retired), len(families)
  ##print len(splits), len(died), len(con)
  ##print splits
  ##print retired
  ##print died

'''for e in sorted(endangerment):
    for i in families:
      print e, len(endangerment[e])
  
  families2endanger = defaultdict(list)
  for j in isolangs:
    fam = language_families[j][0][0]
    ed = language_families[j][0][-1].split()[0]
    ##print language_families[j]
    ##print ed, fam

  x = list(set([v[0][0] for k,v in language_families.items()]))
  print x
  print len(x)
  '''