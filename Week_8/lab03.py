from random import randint
import string as s

dictionary = {
    randint(-100, 100): "".join(
        [
            s.ascii_letters[randint(0, len(s.ascii_letters) - 1)]
            for __ in range(1, i + 2)
        ]
    )
    for i in range(20)
}


dictKeys = list(dictionary.keys())
dictVals = list(dictionary.values())
dictLen = len(dictionary)
# print(dictionary)

# # a) Prints all keys and values.
# for dictCount in range(0,dictLen):
#     print(f"{dictKeys[dictCount]} : {dictVals[dictCount]}")
    
# b) Prints all keys and values, each pair in a separate line, but this time format keys such
# that they occupy 4 spaces and are aligned to the right. 
# Output should look something like this:
# __39 --> kwmIUHDWaHfDEv
# (again, “_” stands for white space)

# for dictCount in range(0,dictLen):
#     print(f"{dictKeys[dictCount]:>4} --> {dictVals[dictCount]}")

# c) Prints all keys and values, each pair in a separate line, but this time align both keys
# and values to the right. Assume that keys occupy up to 4 spaces and values up to 25 spaces.
# for dictCount in range(0,dictLen):
#     print(f"{dictKeys[dictCount]:>4} --> {dictVals[dictCount]:>25}")

# d) Prints keys and values (in the same format as in b) 
# but only if the length of the value is less than 6.

dictKeys.sort()
for dictCount in range(0,dictLen):
    if ( len(dictVals[dictCount]) > 6):
        print(f"{dictKeys[dictCount]:>4} --> {dictVals[dictCount]}")

# Same as d) but this time sort keys.