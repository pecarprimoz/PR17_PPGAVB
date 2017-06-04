from csv import DictReader

from sklearn.cluster import *
import numpy as np

N_CLUSTERS = 15

k_means = KMeans(n_clusters=N_CLUSTERS).fit(np.genfromtxt('mat_sole_izbirci.csv', delimiter=';', skip_header=1)[:,1:])

# sole = []

with open("imena_sol.csv") as f:
    sole = f.readlines()



sole = list(map(lambda x: x.strip(), sole))

# print(sole)

best = None


for _ in range(10000):

    clusters = list(map(lambda x: list(), range(N_CLUSTERS)))

    for i, cluster in enumerate(k_means.labels_):
        sola = sole[i]
        clusters[cluster] += [sola]
    maxCluster = max(list(map(len, clusters)))
    if best is None or maxCluster < min:
        best = clusters[:]
        min = maxCluster

print(list(map(len,best)))

for cluster in best:
    print(cluster)