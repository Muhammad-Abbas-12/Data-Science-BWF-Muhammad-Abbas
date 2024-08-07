# Basic indexing and sclicing of ndarrays

import numpy as np

# 1d array

## arange used for creating arrays of specific range

a1d = np.arange(10)
a1d

## slicing array

a1d[3:6]

## Assigning values to specific range of numbers

a1d[6:10] = 11
a1d

# 2d array

a2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
a2d

a2d.shape

# 3d array

a3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1.1,2.2,3.3],[4.4,5.5,6.6],[7.7,8.8,9.9]]])
a3d
a3d.shape

## accessing a3d elements

a3d[0]
a3d[1]

# a3d slicing

a3d[ :2, :3, :2]

a1d = a1d[:3]


a1d + a2d
a1d + a3d
a2d + a3d

a1d * a2d

# Arrays agregation

sum(a1d)  # python method solwer

np.sum(a2d)  # numpy method faster
np.min(a2d)
np.max(a2d)

# statistical mean , variation and standard deviation

np.mean(a1d)
np.var(a1d)
np.sqrt(np.var(a1d))   # manually
np.std(a1d)

# Matrix or 2d array dot product

a2d

a1d.dot(a2d)

# reshape and transpose of matrix

a1d.shape

a1d.T
a1d.reshape(3,1)
a1d









