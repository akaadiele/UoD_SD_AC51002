# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 11
Plot temperature data, read in from file
@author: Hanhe Lin : Updated Iain Martin
"""

import numpy as np
import matplotlib.pyplot as plt

max_temp = np.loadtxt('max_temp.dat')
min_temp = np.loadtxt('min_temp.dat')

avg_max = np.mean(max_temp[:,1:], axis=1)
avg_min = np.mean(min_temp[:,1:], axis=1)

bins = np.arange(0,20,1)

width = 0.8 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
hist, bins = np.histogram(avg_max, bins=bins)

plt.xlim((min(bins),max(bins)))
plt.ylim((0,1.25*max(hist)))
plt.xlabel('average max temperature (C)')
plt.ylabel('number of years')
plt.xticks([0,5,10,11,12,13,14,15])
plt.bar(center,hist,align='center',width=width)
plt.show()

hist, bins = np.histogram(avg_min, bins=bins)

plt.xlim((min(bins),max(bins)))
plt.ylim((0,1.25*max(hist)))
plt.xlabel('average min temperature (C)')
plt.ylabel('number of years')
plt.xticks([0,5,10,15])
plt.bar(center,hist,align='center',width=width)
plt.show()