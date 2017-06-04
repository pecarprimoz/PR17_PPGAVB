from csv import DictReader

import numpy as np

import fxs

data = np.genfromtxt('mat_sole_izbirci.csv', delimiter=';', skip_header=1)
data = np.delete(data,0,1)
# map(lambda x: )


cs = np.count_nonzero(data, 0)

min_is = []
max_is = []

for i, c in enumerate(cs):
    if c < 73: min_is += [i]
    else: max_is += [i]

min = np.delete(data, max_is, 1)
max = np.delete(data, min_is, 1)

print(np.shape(min))
print(np.shape(max))

fxs.write(
    "sparse_mat.csv",
    min,
    0,
    header=list(map(lambda x: "izb"+str(x),range(np.shape(min)[1]))),
    decimal_point=","
)

fxs.write(
    "dense_mat.csv",
    max,
    0,
    header=list(map(lambda x: "izb"+str(x),range(np.shape(min)[1]))),
)

# np.savetxt("sparse_mat.csv",min,"%1,f",";", header=";".join(list(map(lambda x: "izb"+str(x),range(np.shape(min)[0])))))