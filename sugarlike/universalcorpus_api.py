# -*- coding: utf-8 -*-

import sys; sys.path.append('../')
from universalcorpus import odin, omniglot, udhr

# Example to access ODIN IGTs.
for lang, igts in odin.igts():
  for igt in igts:
    src, eng, gloss, cite = igt
    print lang, src

# Example to access the ODIN source sentences.
for lang, sent in odin.source_sents():
  print lang, sent

# Example to access Omniglot phrases.
for lang, source, translation in omniglot.phrases():
  print lang, source, translation

# Example to access Omniglot source sentences.
for lang, sent in omniglot.source_sents():
  print lang, sent

# Example to access UDHR corpus by documents.
for lang, doc in udhr.documents():
  print lang, doc

# Example to acces UDHR corpus by sentences.
for lang, sent in udhr.source_sents():
  print lang, sent
  
