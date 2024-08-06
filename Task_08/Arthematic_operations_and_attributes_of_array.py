# Arthematic operations on a simple array

import numpy as np

a1 = np.array([1, 2, 4, 6, 3, 7, 3])

# shape an array
a1.shape

# data type of an array
a1.dtype

# sum of arrays
sum_of_a1 = a1 + a1
sum_of_a1

# product of an array
a1 * a1

# you can also perform division power same as product 

# we can also change data type of an array lets see

a1_float = a1.astype(float)
a1_float

# changing shape of an array

a1.reshape(7,1)

