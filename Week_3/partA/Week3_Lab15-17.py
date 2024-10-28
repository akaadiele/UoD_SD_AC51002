# Week 3 Lab tasks 15 to 17

# Task 15
print('Task 15')

mySet = {1,2,3,4,5}
print(mySet)

# ,'old',[12,34,'qwerty']
mySet.add('new')
print(mySet)

mySet.update({31, 42}, {'old','in', 'between'})

print(mySet)

mySet.remove(3)
print(mySet)

mySet.discard('in')
print(mySet)
mySet.discard('in')

mySet.pop()
print(mySet)


print('')

#----------------------------------
# # Task 16
print('Task 16')

mySet.clear()
print(mySet)


print('')

#----------------------------------
# Task 17
print('Task 17')

newSet1 = {10,9,'qwerty',8,7,6}
print(newSet1)
newSet2 = {'qwerty',7,'asdfg',8}
print(newSet2)

print('')

# a. union( )
print('newSet1.union(newSet2): ', newSet1.union(newSet2))

# b. intersection( )
print('newSet1.intersection(newSet2): ', newSet1.intersection(newSet2))

# c. difference( )
print('newSet1.difference(newSet2)', newSet1.difference(newSet2))
print('newSet2.difference(newSet1)', newSet2.difference(newSet1))

# d. symmetric_difference( )
print('newSet1.symmetric_difference(newSet2): ', newSet1.symmetric_difference(newSet2))

# e. issubset( )
print('newSet1.issubset(newSet2) : ', newSet1.issubset(newSet2))

# f. issuperset( )
print('newSet1.issuperset(newSet2)', newSet1.issuperset(newSet2))


print('')

#----------------------------------
