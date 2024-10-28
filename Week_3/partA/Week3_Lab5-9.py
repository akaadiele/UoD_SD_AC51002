# Week 3 Lab tasks 1 to 4

# Task 5
print('Task 5')

# 5a
my_number = 1.3
# print(my_ number < 1)   ;   #'my_ number' is invalid variable
# print(my_ number > 1)   ;   #'my_ number' is invalid variable
# print(my_ number == 1)   ;   #'my_ number' is invalid variable


# 5b
second_number = my_number/0.5+10
some_value = 5

print(second_number > 2.5*some_value)
print(second_number < 2.5*some_value)
# print(second_number = 2.5*some_value)   ;   # Fails as '=' mathematical operand is used instead of '==' comparison operand
print(second_number != 2.5*some_value)

print('')

#----------------------------------
# # Task 6
print('Task 6') ; print('') 
my_bool1 = True
my_bool2 = False
print(my_bool1 or my_bool2)     # returns True
print(my_bool1 and my_bool2)    # returns False
new_bool = my_bool1 or my_bool2    # returns False
print(not(new_bool))

print('')

#----------------------------------
# Task 7
print('Task 7') ; print('')
my_bool1 = True
my_bool2 = False

print(my_bool1 + my_bool2)
print(my_bool1 - my_bool2)
print(my_bool1 * my_bool2)
# print(my_bool1 / my_bool2)  ;   # my_bool2 is equal to 0, and you can not divide by 0

print('')

#----------------------------------
# Task 8
print('Task 8') ; print('')

my_dictionary = {'key_1': 'val_1', 'key_2': 'val2'}
print(my_dictionary)
print(type(my_dictionary))

print('')

#----------------------------------
# Task 9
print('Task 9') ; print('')

my_dictionary = dict([('key_1', 'val_1'), ('key_2', 'val2')])
print(my_dictionary)
print(type(my_dictionary))

print('')

#----------------------------------
