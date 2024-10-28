# Lab class

# Functions

#----------------------------------
# # TASK 11, 12
print('TASK 11, 12')

#A function with a return value

my_text = 'I love Monday mornings \n This might not be true for all'
def my_days(some_test):
    print('Welcome to Functions in Python')

# my_days()   ; # TypeError: my_days() missing 1 required positional argument: 'some_test'
my_days(my_text)

# 
print('****')
#----------------------------------
# # TASK 13
print('TASK 13')


def nameRev():
    nameInput = input('Enter a name to be reversed: ')
    nameReversed = nameInput[::-1]
    
    return nameReversed

#@# 
print('Your name in reverse is : ', nameRev())

# 
print('****')
#----------------------------------
# # TASK 14
print('TASK 14')

# A function with multiple return values

number1 = 6; number2 = 15.3; divisor = 3.2

def some_operation(num1, num2, divd):
    division1 = num1/divd
    division2 = num2/divd
    summ = division1 + division2
    return division1, division2, summ

div1, div2, sm = some_operation(number1, number2, divisor)
print('Division of the first number is ', div1)
print('Division of the first number is ', div2)
print('The sum of both numbers is ', sm)


# Global variables - number1; number2; divisor 
# Local variables - division1, num1, num1, divd, division2 summ

# 1.875     4.78125     6.65625
# 
print('*****')
#----------------------------------
# # TASK -
print('TASK -')

# 
print('')
#----------------------------------
# # TASK -
print('TASK -')

# 
print('')
#----------------------------------
# # TASK -
print('TASK -')

# 
print('')
#----------------------------------

