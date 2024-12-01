# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 7
plots function y(x)=e^(-x) sin⁡(x) for x∈[0,6π] computed at 100 equidistant points
@author: Hanhe Lin : Updated Iain Martin
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6*np.pi,100)
y = np.exp(-x)*np.sin(x)

plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.plot(x,y,'r--',linewidth=3)
plt.show()
