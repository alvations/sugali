from __future__ import print_function, division
from scipy.cluster.hierarchy import linkage, fcluster
import cPickle as pickle
from collections import defaultdict
from miniethnologue import ISO2LANG, LANG2ISO
from crawlandclean.ethnologue import ISO2FAMILY, FAMILIES2ISO

def bcubed(induced, gold, verbose=False):
	"""
	Calculates the B-Cubed score for an induced clustering compared to a gold standard
	Both inputs should dictionaries, mapping from items to sets of items
	"""
	
	if set(induced.keys()) ^ set(gold.keys()):
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


def evaluate(filename='distance_condensed.pk', option='once', method='complete', N_clust=147, verbose=True):
	if verbose: print("Loading data...")
	with open(filename,'rb') as f:
		condensed, labels = pickle.load(f)
	N_lang = len(labels)
	
	ISO2NAME = {iso:u'{} ({})'.format(ISO2LANG[iso][0].decode('utf-8'), iso) for iso in labels}
	
	FAM2ISO = {fam:set([x for x in codes if x in labels]) for fam, codes in FAMILIES2ISO.items()}
	ISO2FAM = {iso:fam for iso, fam in ISO2FAMILY.items() if iso in labels}
	gold = {iso:FAM2ISO[ISO2FAM[iso]] for iso in labels}
	# After filtering like this, we should add Norwegian...
		
	if option == "baseline-separate":
		if verbose: print("Calculating baseline with all languages in separate clusters...\n")
		separate_clusters = {iso:{iso} for iso in labels}
		return bcubed(separate_clusters, gold, verbose=verbose)
	
	elif option == "baseline-same":
		if verbose: print("Calculating baseline with all languages in the same cluster...\n")
		same_cluster = {iso:set(labels) for iso in labels}
		return bcubed(same_cluster, gold, verbose=verbose)
	
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
			flat = flatten(hierarchy, labels, N_clust)
			p, r, f = bcubed(flat, gold)
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
	hierarchy = linkage(condensed, method='complete')
	
	if option == 'once':
		flat = flatten(hierarchy, labels, N_clust)
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
		return bcubed(flat, gold, verbose=verbose)
	
	if option[0:6] == 'range-':  # e.g. 'range-10-250-10' - numbers will be passed to range()
		numbers = [int(x) for x in option[6:].split('-')]
		precision = []
		recall = []
		fscore = []
		for N_clust in range(*numbers):
			flat = flatten(hierarchy, labels, N_clust)
			p, r, f = bcubed(flat, gold)
			precision.append(p)
			recall.append(r)
			fscore.append(f)
			if verbose:
				print(N_clust, p, r, f)
		return (precision, recall, fscore)


if __name__ == '__main__':
	evaluate(option='range-1-301')
	#evaluate(N_clust=98)
	#evaluate(N_clust=99)
	