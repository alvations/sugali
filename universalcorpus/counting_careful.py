# -*- coding: utf-8 -*-
from collections import defaultdict

from crawlandclean import udhr, omniglot, odin, ethnologue
from miniethnologue import ISO2LANG #, MACRO2LANG, RETIRED2ISO
from convert import constructed, dead, macro_split, retired_convert

language_families = ethnologue.language_families()

all_sources = {'odin':odin, 'omniglot':omniglot, 'udhr':udhr}

all_languages     = {x:set() for x in all_sources}
not_in_iso = []

for source_name, source in all_sources.items():
	orig_codes = source.languages()
	for lang in orig_codes:
		if not lang in ISO2LANG:
			not_in_iso.append((source_name, lang))
		elif lang in retired_convert:
			all_languages[source_name].add(retired_convert[lang])
		else:
			all_languages[source_name].add(lang)

natural_languages = {source: all_langs - set(constructed) for source, all_langs in all_languages.items()}
living_languages  = {source: nat_langs - set(dead)        for source, nat_langs in natural_languages.items()}


"""
for source in all_sources:
	print(source)
	print(len(all_languages[source]))
	print(len(natural_languages[source]))
	print(len(living_languages[source]))
"""
families = {source:set() for source in all_sources}
endangerment = {source:defaultdict(set) for source in all_sources} 

for source in all_sources:
	for lang in living_languages[source]:
		try:
			families[source].add(language_families[lang][0][0])
		except IndexError:
			print("IndexError (families): {}, {}".format(source, lang))
	for lang in living_languages[source]:
		try:
			level = language_families[lang][0][-1].split()[0]
		except IndexError:
			print("IndexError (endangerment): {}, {}".format(source, lang))
		endangerment[source][level].add(lang)

print(endangerment)