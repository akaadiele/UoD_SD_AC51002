# Lab class

# Loops

#----------------------------------
# # Task 6
print('Nested Loop with "while loop" ')

#6. a. 

num_rows = 5
i = 0

while i<num_rows:
    j = 0
    while j<=i:
        print("*", end="")
        j+=1
    print()
    i+=1

print('')

#----------------------------------
# # TASK
# The reverse

num_rows = 5
i = num_rows - 1

while i>=0:
    j = i
    while j>=0:
        print("*", end="")
        j-=1
    print()
    i-=1

print('')

#----------------------------------
