# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 22:59:05 2014

Lab: 6
Task: 6
Description: Complex numbers function

@author: Rastko Sknepnek
         Updated Iain MArtin October 2024
"""

# Import square root function form the standard maths library
from math import sqrt

# Add two complex numbers and return the result
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

# Subtract two complex numbers and return the result
def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])

# Multiply two complex numbers and return the result
def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
 
# Divide two complex numbers and return the result 
def div(a,b):
    den = b[0]**2 + b[1]**2
    if den == 0: 
        print('Error! Divsion by zero.')
    re = a[0]*b[0] + a[1]*b[1]
    im = a[1]*b[0] - a[0]*b[1]
    return (re/den,im/den)
    
# Define a modulus (integer divisions remainder) function for complex numbers
def modulus(a):
    return sqrt(a[0]**2 + a[1]**2)

# Define two complex numbers, a= 1 + i, b = 3 -2i
a = (1,1)
b = (3,-2)

# Test the complex number functions
a_p_b = add(a,b)
print('a+b = {:9.7f}{:+9.7f}i'.format(a_p_b[0],a_p_b[1]))
a_m_b = sub(a,b)
print('a-b = {:9.7f}{:+9.7f}i'.format(a_m_b[0],a_m_b[1]))
a_t_b = mul(a,b)
print('a*b = {:9.7f}{:+9.7f}i'.format(a_t_b[0],a_t_b[1]))
a_d_b = div(a,b)
print('a/b = {:9.7f}{:+9.7f}i'.format(a_d_b[0],a_d_b[1]))
print('|a| = {:9.7f}'.format(modulus(a)))

