# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 8
Add a legend to task 7
@author: Hanhe Lin : Updated Iain Martin
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6*np.pi,100)
y = np.exp(-x)*np.sin(x)

plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.xticks(np.pi*np.arange(0,7), [r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$',r'$5\pi$',r'$6\pi$'],fontsize=16)
plt.plot(x,y,'r--',linewidth=3,label='y(x)')
plt.legend(loc='upper right')
plt.show()