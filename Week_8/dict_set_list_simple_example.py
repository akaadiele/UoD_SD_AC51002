"""
DI21008
Simple example to show dictionary, set and list objects
Iain Martin September 2023
"""
from random import randint

#d = dict([(1,"milk"), (3, "bread"), (8, "apple")])
#print ("Dictionary = ", d)
#print ("Key=3, value = ", d.get(3));
#print ("Key=4, value = ", d.get(4));
#
## Show Set and List difference with duplicates
#s = set([1, 3, 4, 2, 3, "hello", "surprise", 2, 3, "hello"])
#l = list([1, 3, 4, 2, 3, "hello", "surprise", 2, 3, "hello"])
#print ("Set = ", s)
#print ("List = ", l)

# Create 6 unique random numbers and add to a set
dice = set()
while (len(dice) < 6):
        dice.add(randint(1,6))

print ("Six unique dice rolls in set = ", dice)
#
# Create 6 unique dice rolls and add to a list
#dice_list = []
#while (len(dice_list) < 6):
#        roll = randint(1,6)
#        if (not roll in dice_list):
#            dice_list.append(roll)
#
#print ("Six unique dice rolls in list = ", dice_list)