# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 10
Plot a polygon from a series of (x, y) points, read in from file
@author: Hanhe Lin : Updated Iain Martin
"""

# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Read in the polygon data
poly = np.loadtxt('polygon.dat')

# This appends the first point to the end to enable the polygon
# to be closed
poly = np.append(poly,[poly[0]], axis=0)

# Seperate out the x and y coordinates 
x = poly[:,0]
y = poly[:,1]

# Polt the polygon points
plt.plot(x,y,'r-',linewidth=3)
plt.show()