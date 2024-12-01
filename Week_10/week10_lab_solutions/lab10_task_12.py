# -*- coding: utf-8 -*-
"""
AC51002: 2024_25
Week 10: Task: 12
Extended temperature data plot
@author: Hanhe Lin : Updated Iain Martin
"""

import numpy as np
import matplotlib.pyplot as plt
import calendar
from itertools import cycle

colors = ['b', 'g', 'r', 'c', 'm', 'y']
markers = ['o', 'v', '^', '>', '<', '8']
skip = 10

max_temp = np.loadtxt('max_temp.dat')
min_temp = np.loadtxt('min_temp.dat')

x = list(range(1,13))
xlab = [calendar.month_abbr[i] for i in range(1,13)]


plt.figure(figsize=(10, 6.5))
plt.subplots_adjust(hspace=.001)
ax = plt.subplot(2, 1, 1)
plt.margins(0.1)
plt.xticks(x, xlab, rotation='vertical')
plt.yticks(fontsize=12)
plt.ylabel(r'$T_{min}({}^\circ C)$',fontsize=18)
plt.ylim((1.1*np.min(min_temp[:,1:]),1.1*np.max(max_temp[:,1:])))
frame = plt.gca()
frame.axes.xaxis.set_ticklabels([])

for (yr,temp,marker,color) in zip(min_temp[::skip,0], min_temp[::skip,1:], cycle(markers), cycle(colors)):
    plt.plot(x, temp, color, label=str(int(yr)), marker=marker, ms=8, lw=1)

plt.subplot(2, 1, 2)
plt.margins(0.1)
plt.xticks(x, xlab, rotation='vertical',fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('month',fontsize=18)
plt.ylabel(r'$T_{max}({}^\circ C)$',fontsize=18)
plt.ylim((1.1*np.min(min_temp[:,1:]),1.1*np.max(max_temp[:,1:])))

for (yr,temp,marker,color) in zip(max_temp[::skip,0],max_temp[::skip,1:],cycle(markers),cycle(colors)):
    plt.plot(x,temp,color,label=str(int(yr)),marker=marker,ms=8,lw=1)
    
plt.legend(title='year', loc='center right', bbox_to_anchor=(1.13, 1))

plt.show()
