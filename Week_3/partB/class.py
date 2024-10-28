# Functions

import week4_functions

# Shadowing Global variables    <
my_score = 50

def score_function(prevScore):
    my_score = 20
    print('Local score: ', my_score)

    total_score = my_score +  prevScore
    print('My total score: ', total_score)


score_function(my_score)
print('Global score: ', my_score)

# Shadowing Global variables    >

print('')
print('Using the imported functions ...')
print('5 + 14 = ', week4_functions.add2(5,14))