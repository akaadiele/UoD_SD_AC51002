# -*- coding: utf-8 -*-
"""
DI21008  Introduction to programming
Title: Formating ints
@author: Rastko Sknepnek - Updated Iain Martin
September 2023
"""

knights = {'gallahad': 'the pure', 'robin': 'not-quite-so-brave-as-sir-lancelot', 
          'arthur': 'the king', 'lancelot': 'the brave' }
         
# get all keys
keys = list(knights.keys())
print('Keys are: ', keys)
print()

#get values
vals = list(knights.values())
print('Values  are : ', vals)


# We can print the entire dictionary as a list of pairs
items = list(knights.items())
print('Dictionary as a list : ', items)

print()
#Here's how to iterate over a dictionary
for key in knights.keys():
    print(key,' --> ',knights[key])

print()  
##  Here's another way to iterate over a dictionary
for (key,val) in knights.items():
    if val == 'the pure':    
      print(key)

   
    