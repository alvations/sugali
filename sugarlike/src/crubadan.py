from collections import Counter
import cPickle as pickle
import os, tempfile, tarfile

OLD_DIR = "../data/crub-131119/"
NEW_DIR = "../data/crubadan/"

for featureType in ["chars","words"]:
  with tarfile.open("{}crubadan-{}.tar".format(NEW_DIR,featureType),"w:gz") as tarball:
    OLD_SUBDIR = OLD_DIR + featureType + "/"
    for filename in os.listdir(OLD_SUBDIR):
      featureSet = Counter()
      with tempfile.NamedTemporaryFile(delete=False, prefix="tmpCrubadan") as fout:
        with open(OLD_SUBDIR+filename,'r') as fin:
          for line in fin:
            (feature, value) = line.split()
            featureSet[feature] = int(value)  
        pickle.dump(featureSet, fout)
        tempFilename = fout.name
      tarball.add(tempFilename, arcname=filename)
      os.remove(tempFilename)