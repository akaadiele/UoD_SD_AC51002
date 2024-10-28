# Week 3 Lab tasks 4 to 7

#----------------------------------
# Task 4
print('Task 4')

""" totalScores = 0

for iScore in range(15):
    studentCount = iScore+1
    print('Enter the score for Student ',studentCount)
    eachScore = int(input('Score: '))
    totalScores += eachScore

print('The total scores for all {} students is {}'.format(studentCount, totalScores))

 """
print('')
#----------------------------------
# Task 5
print('Task 5')

totalScores = 0
studentCount = 0
scoresList = []

for iScore in range(15):
    studentCount += 1
    print('Enter the score for Student ',studentCount)
    eachScore = int(input('Score: '))
    
    scoresList.append(eachScore)
    totalScores += eachScore

print('The total scores for all {} students is {}'.format(studentCount, totalScores))
print('The list of scores are: ',scoresList)

print('')

#----------------------------------
# Task 6
print('Task 6')

print('The average score is: ', totalScores / studentCount)

print('')

#----------------------------------
# Task 7
print('Task 7')
scoresList1to8 = scoresList[0:8]
print(scoresList1to8.count(','))

print(scoresList1to8)

totalScores1to8 = 0
studentCount1to8 = 0

for ii in scoresList1to8:
    studentCount1to8 += 1
    eachScore1to8 = ii
    totalScores1to8 += eachScore1to8
    
print('The total scores for the first {} students is {}'.format(studentCount1to8, totalScores1to8))
print('The average score is: ', totalScores1to8 / studentCount1to8)


#----------------------------------
scoresList9to15 = scoresList[8:15]
print(scoresList9to15.count(','))
print(scoresList9to15)

totalScores9to15 = 0
studentCount9to15 = 0

for jj in scoresList9to15:
    studentCount9to15 += 1
    eachScore9to15 = jj
    totalScores9to15 += eachScore9to15
    
print('The total scores for the last {} students is {}'.format(studentCount9to15, totalScores9to15))
print('The average score is: ', totalScores9to15 / studentCount9to15)



print('')

#----------------------------------
