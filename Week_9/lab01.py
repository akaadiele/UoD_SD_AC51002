# Task 1


# Write a program that asks the user to enter a positive integer N. 
# The program then computes and prints the sum of all numbers between 1 and N (inclusive).

inputN = int(input('Enter a positive integer: '))
accumulate = 0

# a) Do this using standard (iterative) technique (a for loop and an accumulator variable)
print()
# def sum1toN(intN):
#     for count in range(1, inputN+1):
#         # accumulate = count + 1
#         accumulate += count
#     return accumulate

# print(f"The sum of all numbers between 1 and {inputN} is: {sum1toN(inputN)}")
    
# b) Now repeat the same task, but this time by defining a recursive function summe(N). 
# Hint: The factorial example above should be a good starting point.
def sum1toN_Recursive(intN):
    if (intN == 0):
        accumulate = 0
    else:
        accumulate = intN + sum1toN(intN-1)

    return accumulate

print(f"The sum of all numbers between 1 and {inputN} is: {sum1toN_Recursive(inputN)}")

# c) Try both solutions for a large number, say N=500