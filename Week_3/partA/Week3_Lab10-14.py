# Week 3 Lab tasks 10 to 14

# Task 10
print('Task 10')
myCarParkDictionary = dict( [ ('Slot1', ('Mazda','Black')), ('Slot2', ('Benz','White')), ('Slot3', ('Toyota','Green')), \
                             ('Slot4', ('Bugatti','Red')), ('Slot5', ('Rolls Royce','Grey')) ])

print(myCarParkDictionary)
print(type(myCarParkDictionary))

print('')

#----------------------------------
# # Task 11
print('Task 11')

print(myCarParkDictionary.keys())
print(type(myCarParkDictionary.keys()))


print('')

#----------------------------------
# Task 12
print('Task 12')

print(myCarParkDictionary.values())
print(type(myCarParkDictionary.values()))

print('')

#----------------------------------
# Task 13
print('Task 13')

print(myCarParkDictionary.items())
print(type(myCarParkDictionary.items()))

print('')

#----------------------------------
# Task 14

for key in myCarParkDictionary.keys( ):
    print ('The values for: ', key, 'is', myCarParkDictionary[key])

print('')

#----------------------------------

print('Adding a new car - using "update" function ')
myCarParkDictionary.update([('Slot6', ('Lambo','Yellow'))])
myCarParkDictionary.update([('Slot7', ('Honda','cream'))])

print(myCarParkDictionary)

print('')

#----------------------------------
print('')
print('before: ',myCarParkDictionary)
print('Removing an existing car - using "pop" function ')

myCarParkDictionary.pop('Slot1')
print('after: ',myCarParkDictionary)
print('')

#----------------------------------
