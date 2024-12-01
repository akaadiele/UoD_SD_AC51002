# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 9
Plot random point, joined with lines
@author: Hanhe Lin : Updated Iain Martin
"""

import numpy as np
import matplotlib.pyplot as plt

points = np.random.uniform(-5,5,(50,2))

plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.plot(points[:,0],points[:,1],'g-',linewidth=3)

plt.show()