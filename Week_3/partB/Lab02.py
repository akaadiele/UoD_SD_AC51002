# Lab class

# 'if' statements

#----------------------------------
# TASK (Two-level if statement)
print('TASK (Two-level if statement)')

# 3 a. 
my_name = "Cole"
if my_name == "Helen":
    print('Yes, ', my_name, 'is the exact name')
else:
    print('Nice try')
    print('Not the correct name, try again')

print('')


# b. 

#my_score = input('Enter you score: ')   ; # input is collected as a string, needs to be  type casted 
my_score = int(input('Enter you score: '))

if my_score >= 50:
    print('Nice! That is a pass')
else:
    print('That is not a very good score.')
    print('You would have to retake the test')
#----------------------------------
# 