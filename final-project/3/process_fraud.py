import itertools
import numpy as np
import os.path
import pandas as pd
import gc

from sklearn.feature_extraction.text import CountVectorizer

folder = os.getcwd()

print('reading')

outpatient_df = pd.read_csv(os.path.join(folder, "..", "DE1_0_2008_to_2010_Outpatient_Claims_Sample_1.csv"), low_memory=False)

def join_codes(row):
    return " ".join([str(v) for i, v in row.iteritems() if pd.notnull(v)])

colnames = [colname for colname in outpatient_df.columns if "_CD_" in colname]
codebag = outpatient_df.ix[:, colnames].apply(join_codes, axis=1)

print('tokenizing')

vec = CountVectorizer(min_df=1, binary=True)
X = vec.fit_transform(codebag)

print('calc similarities')

similarity = X.T * X

EPSILON = 0.001

print('calculating densities')

fileout = open(os.path.join(folder, "..", "clusters.txt"), 'wb')

for row in range(0, X.shape[0]):
    # manual garbage collection
    if row % 100 == 0:
        print("row " + str(row))
        gc.collect()
    # get non-zero codes in the row from our CountVectorizer matrix
    codes = [code for code in X[row, :].nonzero()][1]
    dists = []
    for i, j in itertools.product(codes, codes):
        # only take thhe upper triangle
        if i < j:
            sim_ij = similarity.getrow(i).todense()[:, j][0]
            if sim_ij == 0:
                sim_ij = EPSILON
            dists.append(1 / (sim_ij ** 2)) 
    fileout.write("%f\n" % (np.sqrt(sum(dists)) / len(dists)))

fileout.close()