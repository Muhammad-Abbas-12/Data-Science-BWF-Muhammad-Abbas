# This programe will show you how numpy is
# faster than python

import numpy as np

# numpy array of one million entries

my_array = np.arange(1000000)

%timeit my_array2 = my_array *2


# Python list of one million items

my_list = range(1000000)

%timeit my_list2 = [i * 2 for i in my_list]