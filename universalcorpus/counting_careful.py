# -*- coding: utf-8 -*-
from __future__ import division
from operator import or_

from crawlandclean import udhr, omniglot, odin, ethnologue
from miniethnologue import ISO2LANG #, MACRO2LANG, RETIRED2ISO
from convert import constructed, dead, macro_split, retired_convert

language_families = ethnologue.language_families()

all_sources = ['odin', 'omniglot', 'udhr', 'wikipedia']
other_sources = {'odin':odin, 'omniglot':omniglot, 'udhr':udhr}

all_languages = {x:set() for x in all_sources}
not_in_iso = []

for source_name, source in other_sources.items():
	orig_codes = source.languages()
	for lang in orig_codes:
		if not lang in ISO2LANG:
			not_in_iso.append((source_name, lang))
		elif lang in retired_convert:
			all_languages[source_name].add(retired_convert[lang])
		else:
			all_languages[source_name].add(lang)

all_languages['wikipedia'] = {'lat', 'gag', 'cor', 'cre', 'lit', 'ven', 'mri', 'nau', 'bos', 'arz', 'tha', 'yor', 'tet', 'yid', 'ssw', 'wln', 'diq', 'krc', 'nrm', 'ndo', 'urd', 'pnt', 'isl', 'ori', 'pan', 'kaz', 'kab', 'fra', 'bis', 'sin', 'msa', 'ces', 'cbk', 'mah', 'nor', 'mlt', 'smo', 'new', 'kik', 'frp', 'kor', 'ell', 'spa', 'vol', 'ibo', 'mya', 'ita', 'tsn', 'sah', 'mzn', 'tuk', 'hun', 'dzo', 'tel', 'sun', 'tah', 'lug', 'ile', 'est', 'bel', 'ido', 'vls', 'nso', 'lao', 'orm', 'vec', 'mlg', 'ltg', 'vie', 'iii', 'cos', 'mus', 'oci', 'heb', 'ton', 'deu', 'fur', 'zha', 'chu', 'tat', 'min', 'mkd', 'roh', 'amh', 'fry', 'nld', 'bug', 'gle', 'yue', 'pus', 'ace', 'bod', 'lmo', 'srp', 'chy', 'lbe', 'tyv', 'nep', 'pcd', 'lzh', 'jav', 'run', 'aze', 'grn', 'ben', 'mhr', 'jbo', 'kau', 'sgs', 'lez', 'ltz', 'hye', 'kur', 'slv', 'kas', 'tam', 'nov', 'dsb', 'kon', 'lav', 'koi', 'bul', 'nya', 'bxr', 'ina', 'kal', 'wol', 'wuu', 'sco', 'slk', 'nds', 'sag', 'pol', 'ava', 'nan', 'gsw', 'fin', 'dan', 'xho', 'pfl', 'mar', 'ukr', 'snd', 'nap', 'oss', 'vro', 'her', 'cdo', 'uzb', 'lin', 'ewe', 'nno', 'tgk', 'hat', 'xal', 'scn', 'kua', 'hif', 'hmo', 'kom', 'glv', 'mdf', 'uig', 'por', 'ang', 'lim', 'kbd', 'som', 'cho', 'che', 'sot', 'fas', 'cym', 'mon', 'tpi', 'myv', 'pih', 'xmf', 'srn', 'rus', 'pdc', 'rue', 'hak', 'eng', 'ext', 'hau', 'swa', 'got', 'bam', 'tum', 'kin', 'nav', 'fao', 'hrv', 'asm', 'aar', 'crh', 'fij', 'bpy', 'bar', 'ara', 'udm', 'bak', 'zul', 'pap', 'csb', 'aka', 'haw', 'sme', 'zea', 'gla', 'stq', 'tgl', 'mal', 'swe', 'tir', 'afr', 'ckb', 'ksh', 'vep', 'kir', 'rup', 'ful', 'pnb', 'jpn', 'bjn', 'zho', 'abk', 'frr', 'kaa', 'eus', 'ilo', 'bre', 'que', 'pms', 'cha', 'rmy', 'aym', 'szl', 'pam', 'arg', 'hbs', 'pag', 'iku', 'kat', 'cat', 'ron', 'khm', 'sqi', 'san', 'ipk', 'glk', 'jv', 'tur', 'lad', 'ceb', 'mwl', 'glg', 'twi', 'war', 'mrj', 'ast', 'epo', 'pli', 'div', 'kan', 'sna', 'tso', 'chr', 'hsb', 'srd', 'lij', 'bcl', 'chv', 'hin', 'arc', 'ind', 'guj', 'gan', 'lzh', 'got', 'ang'}
all_languages['combined'] = reduce(or_, all_languages.values())

natural_languages = {source: all_langs - set(constructed) for source, all_langs in all_languages.items()}
living_languages  = {source: nat_langs - set(dead)        for source, nat_langs in natural_languages.items()}

natural_nomacro = {source:set() for source in natural_languages}
for source in natural_languages:
	for lang in natural_languages[source]:
		if lang in macro_split:
			if len(natural_languages[source] & set(macro_split[lang].keys())) == 0:
				natural_nomacro[source].add(lang)
		else:
			natural_nomacro[source].add(lang)

for source in all_sources + ['combined']:
	print source
	print "all", len(all_languages[source])
	print "nat", len(natural_languages[source])
	print "-ma", len(natural_nomacro[source])
	print "liv", len(living_languages[source]), "\n"
"""
families = {source:set() for source in living_languages}
danger_levels = ['0', '1', '2', '3', '4', '5', '6a', '6b', '7', '8a', '8b', '9', '10']
endangerment = {source:{x:set() for x in danger_levels} for source in living_languages} 

family_IndexError = []
danger_IndexError = []

for source in living_languages:
	for lang in living_languages[source]:
		try:
			families[source].add(language_families[lang][0][0])
		except IndexError:
			family_IndexError.append((source, lang))
	for lang in living_languages[source]:
		#if source == 'odin' and lang == 'mbg':
		#	print "hello!", language_families[lang][0][-1].split()[0]
		try:
			level = language_families[lang][0][-1].split()[0]
		except IndexError:
			danger_IndexError.append((source, lang))
		endangerment[source][level].add(lang)

for level in danger_levels:
	for source in living_languages:
		print('{:2}, {}: {}'.format(level, source, len(endangerment[source][level])))

print(living_languages['odin'] - living_languages['combined'])
print(endangerment['odin']['10'] - endangerment['combined']['10'])
"""
"""
print(language_families)
print(language_families['eng'])
print(language_families['eng'][0])
print(language_families['eng'][0][-1])
print(language_families['eng'][0][-1].split()[0])
"""
"""
n = 0
for lang in language_families:
	try:
		level = language_families[lang][0][-1].split()[0]
		if level == '1':
			n += 1
	except IndexError:
		continue
print(n)
print(len(language_families))
"""
## Defaultdict is not safe for a user interface
## Why do we only have 1394 languages here?

number = {1:0, 2:0, 3:0, 4:0}

for lang in natural_languages['combined']:
	n = 0
	for source in all_sources:
		if lang in natural_languages[source]:
			n += 1
	number[n] += 1

print("number of sources")
print(number)
print "2+:", sum(number.values()) - number[1]

print(len(natural_nomacro['combined'] & living_languages['combined']) / 7105)