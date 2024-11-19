# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 19:12:25 2014

Lecture: 17
Example: 7
Plotting student numbers on xy graph

@author: Rastko Sknepnek
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from operator import itemgetter
import csv

def read_data(datafile):
    tags = []
    names = []
    majors = []
    with open(datafile,'r') as classfile:
        class_list = csv.reader(classfile)
        for row in class_list:
            tag, name, major = row
            tags.append(int(tag))
            names.append(name)
            majors.append(major)
    return [tags,names,majors]

def get_diff_majors(majors):
    diff_majors = [] 
    for major in majors:
        if not major in diff_majors: 
            diff_majors.append(major)  
    return diff_majors

def get_major_tags(tags, majors, major):
    if len(tags) != len(majors):
        print('tags and majors have to be same size.')
        sys.exit(1)
    return [tags[i] for i in range(len(tags)) if majors[i] == major]

tags, names, majors = read_data('class_list.csv')
diff_majors = get_diff_majors(majors)

maj_numbers = {}

for major in diff_majors:
    maj_numbers[major.lower()] = len(get_major_tags(tags, majors, major))

to_plot = sorted(list(maj_numbers.items()),key=itemgetter(1),reverse=True)
    
labels = [elem[0] for elem in to_plot]
sizes = [elem[1] for elem in to_plot]
    
explode = 0.1*np.ones(len(labels))
cs = cm.get_cmap('spring')
colors = [cs(i) for i in np.linspace(0,1,len(labels))]

plt.figure(figsize=(10,6))

patches, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, colors=None,
                       autopct='%1.1f%%', shadow=True, startangle=0)
for i in range(len(texts)):
    texts[i].set_fontsize(16)
    autotexts[i].set_fontsize(16)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
plt.savefig('test.svg',dpi=150)