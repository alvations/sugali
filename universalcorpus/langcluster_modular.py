from __future__ import print_function, division
from scipy.cluster.hierarchy import linkage
import cPickle as pickle
from collections import defaultdict
from miniethnologue import ISO2LANG
from crawlandclean.ethnologue import ISO2FAMILY, FAMILIES2ISO

def bcubed(induced, gold, verbose=False):
	"""
	Calculates the B-Cubed score for an induced clustering compared to a gold standard
	Both inputs should be dictionaries, mapping from items to sets of items
	"""
	
	if set(induced.keys()) ^ set(gold.keys()):
		if verbose:
			print(induced.keys())
			print(gold.keys())
		raise KeyError("The induced clusters and gold classes must be defined over the same set")
	
	N_items = len(induced.keys())
	sum_fscore = 0
	sum_precision = 0
	sum_recall = 0
	
	for key in induced.keys():
		cluster = induced[key]
		klass = gold[key]
		intersect = cluster & klass
		
		precision = len(intersect) / len(cluster)
		recall = len(intersect) / len(klass)
		fscore = 2 * len(intersect) / (len(cluster) + len(klass))
		
		sum_precision += precision
		sum_recall += recall
		sum_fscore += fscore
	
	av_precision = sum_precision/N_items
	av_recall = sum_recall/N_items
	av_fscore = sum_fscore/N_items
	
	if verbose:
		print('Precision: {}'.format(av_precision))
		print('Recall:    {}'.format(av_recall))
		print('F-score:   {}'.format(av_fscore))
	
	return (av_precision, av_recall, av_fscore)

def pairwise(induced, gold, verbose=False):
	"""
	Calculates pairwise precision, recall, and f-scores for an induced clustering compared to a gold standard
	Both inputs should be dictionaries, mapping from items to sets of items
	"""
	
	if set(induced.keys()) ^ set(gold.keys()):
		if verbose:
			print(induced.keys())
			print(gold.keys())
		raise KeyError("The induced clusters and gold classes must be defined over the same set")
	
	induced_pairs = {(x,y) for cluster in set(induced.values()) for x in cluster for y in cluster if x<y}
	gold_pairs    = {(x,y) for klass   in set(gold.values())    for x in klass   for y in klass if x<y}
	
	both = len(induced_pairs & gold_pairs)
	false_pos = len(induced_pairs) - both
	false_neg = len(gold_pairs)    - both
	
	precision = both / (both + false_pos)
	recall = both / (both + false_neg)
	fscore = 2 * both / (2 * both + false_pos + false_neg)
	
	if verbose:
		print('Precision: {}'.format(precision))
		print('Recall:    {}'.format(recall))
		print('F-score:   {}'.format(fscore))
	
	return (precision, recall, fscore)


def flatten(hierarchy, labels, N_clust=147):
	"""
	Takes a hierarchical clustering and flattens it.
	Returns a dictionary from items to the set of elements in the cluster
	Note that the scipy function fcluster does not let you fix the number of clusters
	"""
	N_items = len(labels)
	members = dict() # Map from the index for a cluster to its members
	for i in range(N_items):
		members[i] = frozenset({labels[i]})
	for n in range(N_items - N_clust):
		j = hierarchy[n,0]
		k = hierarchy[n,1]
		members[N_items + n] = members.pop(j) | members.pop(k)
	return {item:cluster for cluster in members.values() for item in cluster}

def flatten_scipy(hierarchy, labels, N_clust=147):
	"""
	Takes a hierarchical clustering and flattens it, using scipy.
	Returns a dictionary from items to the set of elements in the cluster
	Note that this does not let you precisely fix the number of clusters
	"""
	from scipy.cluster.hierarchy import fcluster
	members = defaultdict(set) # Map from the index for a cluster to its members
	flat = fcluster(hierarchy, t=N_clust, criterion='maxclust')
	for i in range(len(flat)):
		members[flat[i]].add(labels[i])
	frozen_members = {key:frozenset(value) for key, value in members.items()}
	return {item:cluster for cluster in frozen_members.values() for item in cluster}

def evaluate(filename='distance_condensed.pk', option='once', method='complete', N_clust=147, metric=bcubed, flat_func=flatten, verbose=True):
	if verbose: print("Loading data...")
	with open(filename,'rb') as f:
		condensed, labels = pickle.load(f)
	N_lang = len(labels)
	
	ISO2NAME = {iso:u'{} ({})'.format(ISO2LANG[iso][0].decode('utf-8'), iso) for iso in labels}
	
	FAM2ISO = {fam:frozenset([x for x in codes if x in labels]) for fam, codes in FAMILIES2ISO.items()}
	ISO2FAM = {iso:fam for iso, fam in ISO2FAMILY.items() if iso in labels}
	gold = {iso:FAM2ISO[ISO2FAM[iso]] for iso in labels}
	# After filtering like this, we should add Norwegian...
		
	if option == "baseline-separate":
		if verbose: print("Calculating baseline with all languages in separate clusters...\n")
		separate_clusters = {iso:{iso} for iso in labels}
		return metric(separate_clusters, gold, verbose=verbose)
	
	elif option == "baseline-same":
		if verbose: print("Calculating baseline with all languages in the same cluster...\n")
		same_cluster = {iso:set(labels) for iso in labels}
		return metric(same_cluster, gold, verbose=verbose)
	
	elif option[0:16] == "baseline-random-":  # e.g. 'baseline-random-12' to average over 12 runs
		from random import random
		runs = int(option[16:])
		if verbose: print("Calculating random clusterings, with {} runs...".format(runs))
		length = int(N_lang * (N_lang - 1) / 2)
		sum_precision = 0
		sum_recall = 0
		sum_fscore = 0
		for _ in range(runs):
			condensed = []
			for _ in range(length):
				condensed.append(random())
			hierarchy = linkage(condensed, method=method)
			flat = flat_func(hierarchy, labels, N_clust)
			p, r, f = metric(flat, gold)
			if verbose: print(p, r, f)
			sum_precision += p
			sum_recall += r
			sum_fscore += f
		av_precision = sum_precision / runs
		av_recall = sum_recall / runs
		av_fscore = sum_fscore / runs
		if verbose:
			print('\nPrecision: {}'.format(av_precision))
			print('Recall:    {}'.format(av_recall))
			print('F-score:   {}'.format(av_fscore))
		return (av_precision, av_recall, av_fscore)
	
	if verbose: print("Calculating hierarchical clustering...")
	hierarchy = linkage(condensed, method=method)
	
	if option == 'once':
		flat = flat_func(hierarchy, labels, N_clust)
		if verbose:
			size = defaultdict(int)
			print('\nClusters:')
			for cluster in set(flat.values()):
				print(', '.join([ISO2NAME[iso] for iso in cluster]))
				size[len(cluster)] += 1
			print('\nCluster size frequencies:')
			for x in sorted(size):
				print('{} - {}'.format(x, size[x]))
			print('')
		return (metric(flat, gold, verbose=verbose), flat, gold, ISO2NAME)
	
	if option[0:6] == 'range-':  # e.g. 'range-10-250-10' - numbers will be passed to range()
		clust_range = range(*[int(x) for x in option[6:].split('-')])
		precision = []
		recall = []
		fscore = []
		high_score = (None,None,None,0)
		for N_clust in clust_range:
			flat = flat_func(hierarchy, labels, N_clust)
			p, r, f = metric(flat, gold)
			precision.append(p)
			recall.append(r)
			fscore.append(f)
			if verbose:
				print(N_clust, p, r, f)
			if f > high_score[3]:
				high_score = (N_clust, p, r, f)
		if verbose:
			print("\nBest result for {} clusters:\n\nPrecision: {}\nRecall:    {}\nF-score:   {}".format(*high_score))
		return (clust_range, precision, recall, fscore)


if __name__ == '__main__':
	evaluate(N_clust = 105)
	#evaluate(N_clust = 105, metric = pairwise)
	#evaluate(option='range-1-301')
	#evaluate(option='range-1-301', metric=pairwise)
	#evaluate(N_clust=98)
	#evaluate(N_clust=99)
	#evaluate(N_clust=199)
	#evaluate(option='baseline-random-20')
	#evaluate(method='average')
	#evaluate(flat_func=flatten_scipy, N_clust=80)
	#evaluate(option='baseline-separate')
	#evaluate(option='baseline-same')
	"""
	scores, flat, gold, name = evaluate()
	print('\nGold class size frequencies:')
	size = defaultdict(int)
	for klass in set(gold.values()):
		size[len(klass)] += 1
	for x in sorted(size):
		print('{} - {}'.format(x, size[x]))
	print('\nSingleton clusters:\n')
	for lang in flat:
		if len(flat[lang]) == 1:
			print(u"{}, {}: {}".format(name[lang], len(gold[lang]), u', '.join([name[x] for x in gold[lang]])))
	"""