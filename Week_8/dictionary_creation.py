# -*- coding: utf-8 -*-
"""
DI21008  Introduction to programming
Title: Formating ints
@author: Rastko Sknepnek - Updated Iain Martin
September 2023
"""

knights = {'gallahad': 'the pure', 'robin': 'not-quite-so-brave-as-sir-lancelot', 
          'arthur': 'the king', 'lancelot': 'the brave' }

list_of_knights = list(knights)
print(list_of_knights)

print()
# List all key:value pairs
key_val = list(knights.items())
print(key_val)

print()
# Making a dictionary out of a list of pairs
ages_list = [('John',25), ('Mike', 22), ('Jen', 24)]
ages = dict(ages_list)

print('ages dictionary : ', ages)

print()

# Dicionary comprehension
#my_dict = {2*i: [j for j in range(i) if j < 6] for i in range(1,10)}
#
##print('Dictionary : ', my_dict)
#
##A bit more on looping
#print()
#for key in my_dict.keys():
#    print(key,' --> ', end = ' ')
#    for i in my_dict[key]:
#        print(i,end=' ')
#    print()
#    
## A bit more on looping (with sort)
#print()
#for key in sorted(my_dict.keys()):
#    print(key,' --> ', end = ' ')
#    for i in my_dict[key]:
#        print(i,end=' ')
#    print()