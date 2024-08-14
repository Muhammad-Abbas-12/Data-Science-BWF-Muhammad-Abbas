# In this file we will practicing pandas series

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

num_series = pd.Series([1,2,3,4,5], index = [0,1,2,3,4])
num_series

np.exp(num_series)
0 in num_series
1 in num_series

# you can also make a series from dictionary 
# by passing it in series(dic)

Salary_dic = {"ali": 3990 , "Amjad" : 4400, "Sadam" : 2500}
Salary_series = pd.Series(Salary_dic)
Salary_series

# and you can also make a dictionary from Series 
# by using to_dic()

Salary_series.to_dict()

Names = ["Haisam", 'ali','Amjad','Sadam']

bonus_series = pd.Series(Salary_dic, index = Names)
pd.isna(bonus_series)
pd.notna(bonus_series)
Salary_series.index.name = 'Name'
Salary_series
