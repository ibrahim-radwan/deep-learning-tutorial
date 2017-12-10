# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:13:14 2017

@author: ibrahim radwan
"""

# pandas tutorial

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.DataFrame([[2,4,6], [10, 20, 30]])

df1 = pd.DataFrame([[2,4,6], [10, 20, 30]], columns=["price", "age", "value"])

print(df1.price)
print(df1["price"])
print(df1["price"][1])
print(df1["price"].max)

# plot series
df2 = pd.DataFrame(np.random.randn(1000, 4), columns=list('ABCD'))

df2 = df2.cumsum()

#plt.figure(); 
df2.plot(); 
plt.legend(loc='best')
