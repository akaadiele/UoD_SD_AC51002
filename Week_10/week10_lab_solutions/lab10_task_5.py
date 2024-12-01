# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 5
Find indices of non-zero elements from [1,2,0,0,4,0,1,18,0,0,2,5,0,7]. 
Print those non-zero elements.
@author: Rastko Sknepnek : Updated Iain Martin
"""

import numpy as np

a = np.array([1,2,0,0,4,0,1,18,0,0,2,5,0,7])
idx = np.nonzero(a)
print(idx)
print(a[idx])
