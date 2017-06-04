import numpy
from sklearn.decomposition import NMF , ProjectedGradientNMF


R = numpy.genfromtxt('dense_mat.csv', delimiter=';', skip_header=1)

R = numpy.array(R)
nmf = NMF()
W = nmf.fit_transform(R)
H = nmf.components_
nR = numpy.dot(W,H)
# print(R)
print(list(nR))