# pandas DataFrame

import pandas as pd
import numpy as np
# Data frame from dictionary

data = {"Cities" : ["mardan","Peshawar","Islamabad","Lahore"], "Year" : [2002, 2004, 2006, 2022], "pop" : [3, 4, 6, 8]}
frame = pd.DataFrame(data)
frame.head()   # the head method shows first five elements
frame.tail()   # and similarly the tail method shows last five ones

# you can also change sequence of columns

frame = pd.DataFrame(data , columns = ["Year","Cities","Pop"] )
frame

# you can also show a sigle coumns of a dataframe

frame["Year"]

# you can also assigne new value to an element

frame["Cities"][0] = "Malakand"
frame

num_series = pd.Series(np.arange(10,100, step = 10), index = np.arange(9))
num_series

# index objects

obj = pd.Series(np.arange(3),index =['a','b','c'])

index = obj.index
index

# type error   index[1] = "d"

labels = pd.Index(np.arange(3))
labels

# Reindexing 

obj = pd.Series([2.4,5.7,2.4], index = ['a','b','c'])
obj

obj = obj.reindex(['a','b','c','d','e'])
obj

frame = pd.DataFrame(np.arange(9).reshape(3,3), index = ['a','b','c'], columns = ['ohio','Texas','Claifornia'])
frame
cities = ['ohio','Peshawar','Claifornia','Mingora','Kalam']
frame.reindex(columns = cities)


# droping entries from an axis

obj = pd.Series(np.arange(5.), index = ['a','b','c','d','e'])
obj

new_obj = obj.drop('c')
new_obj

obj.drop(['d','c'])

data = pd.DataFrame(np.arange(16).reshape((4,4)), index =['ohoi','colorado','utah','new york'], columns = ['one','two','three','four'])
data




