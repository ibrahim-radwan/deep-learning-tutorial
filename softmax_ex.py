# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:50:55 2017

@author: Ibrahim Radwan
"""

import numpy as np
from matplotlib import pyplot as plt

def softmax(x):
    s_x = np.exp(x) / np.sum(np.exp(x), axis=0)
    return s_x

scores = [4.0, 1.5, 0.5]

print(softmax(scores))

# plot softmax curves
x = np.arange(-2.0, 4.0, 0.1)

scores = np.vstack([x, np.ones_like(x), 0.4 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()


