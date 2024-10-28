# Week 3 Lab tasks 1 to 3

#----------------------------------
# Task 1
print('Task 1')

a = 1; b = 3.333333333
print(a, ' data type : ', type(a))
print(b, ' data type : ', type(b))
print('')

c = -9884; d = 3.552E+04
print(c, ' data type : ', type(c))
print(d, ' data type : ', type(d))
print('')

c = a + b; d = [1,3,5,7]
print(c, ' data type : ', type(c))
print(d, ' data type : ', type(d))
print('')

e = (1,3,5,7)
print(e, ' data type : ', type(e))

print('')
print('')

#----------------------------------
# Task 2
print('Task 2')

print('minimum is :', min(1,2,3,423,1234,23,6,2324,543))
print('maximum is :', max(1,2,3,423,1234,23,6,2324,543))

print('')

print('minimum is :', min(12.3423,1234.23,62324.543))
print('maximum is :', max(12.3423,1234.23,62324.543))
 

print('')

#----------------------------------
# Task 3
print('Task 3')

# a. a to float and string
print(a,' to float and string')
print(float(a))
print(str(a))
print('')

# b. b to integer and string
print(b, ' to integer and string')
print(int(b))
print(str(b))
print('')

# c. c to integer and string
print(c,' to integer and string')
print(int(c))
print(str(c))
print('')

# d. d to float and tuple
print(d,' to float and tuple')
# print(float(d))   ;   # TypeError: float() argument must be a string or a real number, not 'list'
print('tuple: ', tuple(d))

print('')

# e. e to float and list
print(e,' to float and list')
# print(float(e))   ;   # TypeError: float() argument must be a string or a real number, not 'tuple'
print('list : ', list(e))

print('')

print('')

#----------------------------------
