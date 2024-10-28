# A program to implement Heron's formula

import math

halfVal = 1 / 2

sideA = 9
sideB = 11
sideC = 16

sVal = halfVal * (sideA + sideB + sideC)

sCalc = (sVal * (sVal - sideA) * (sVal - sideB) * (sVal - sideC) )
print(sCalc)

print('The area of the Triangle is: ', math.sqrt(sCalc))
