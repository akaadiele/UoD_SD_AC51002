# Lab class

# Loops

#----------------------------------
# # Task 7
print('Nested Loop with "for loop" ')

#7

# Define the number of rows for the triangle
num_rows = 5
# Outer loop for each row
for i in range(1, num_rows + 1):
    # Inner loop to print stars in each row
    for j in range(i):
        print("*", end="")
    # Move to the next line after each row
    print()

print('')

#----------------------------------
# # TASK
# The reverse

num_rows = 5
for i in range(num_rows, 0,-1):
    # Inner loop to print stars in each row
    for j in range(i):
        print("*", end="")
    # Move to the next line after each row
    print()


print('')

#----------------------------------
