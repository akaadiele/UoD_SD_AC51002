# Task 1

from random import uniform

numbers = [uniform(0,200) for i in range(50)]
numbersLen = len(numbers)

print('\n')

# a) Prints all numbers in one line, separating them with comma (do not worry about
# comma after the last element)
# for numberCount in range(0,numbersLen):
#     print(numbers[numberCount], end=',')
    
# print('\n')

# b) Prints all numbers, each in a separate line, but this time keep only 3 digits after the
# decimal point.
# for numberCount in range(0,numbersLen):
#     print(f"{numbers[numberCount]:.3f}", end='\n')
    
# print('\n')

# c) Prints all numbers, each in a separate line, but such that each number is right
# aligned, occupies a total 7 characters, with 3 digits after the decimal point.
# ---------
# for numberCount in range(0,numbersLen):
#     print(f"{numbers[numberCount]:>7.3f}", end='\n')

# print('\n')

# d) Prints all numbers, each in a separate line, but such that each number is centered,
# occupies a total of 10 characters with 4 digits after the decimal point.
# for numberCount in range(0,numbersLen):
#     print(f"{numbers[numberCount]:^10.4f}", end='\n')

# print('\n')
# e) Sorts all numbers in the ascending order, prints each of them in a separate line such
# that each number occupies total of 8 characters with 3 digits after the decimal point.
for numberCount in range(0,numbersLen):
    print(f"{numbers[numberCount]:8.3f}", end='\n')


# print('\n')