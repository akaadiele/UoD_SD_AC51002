# 2. Palindromes with recursion

# A palindrome is a word, phrase, number, or other sequence of symbols or elements that reads the same forward or reversed.
# For example: “12321” is a palindrome, so is “aibohphobia” (fear of palindromes).
# Write a program that asks the user to enter a string and store it in a variable word.
# Test if word is a palindrome and write on the screen “True” if it is. Write “False” otherwise.
# Make all words lower case. You can use function lower() to do this.
# For example, “King Arthur”.lower() will return you “king arthur”.
# Note that all single letter words, e.g., “a” or “I” are by definition palindromes.
# Empty string is also a palindrome.
# The obvious solution would be to check if word == word[::-1]. However, you are asked here
# do a bit more work and practice your skills with for loops and recursion.

word = input('Enter a word to check if it is a palindrome: ')


# Therefore,
# a) Solve this problem iteratively (using a for loop).
# Hint: Remember that negative indices will return letters from the right end of a string.
# For example, if word is “papaya”, word[-2] will give you the second letter from the
# end, which is “y”.

def palindromeCheck(inputWord):
    wordLen = len(inputWord)
    isPalindrome = True
    wordMidPoint = (wordLen // 2)
    
    if ((wordLen <= 1)):
        pass
    else:
        for wordCount in range(0, wordMidPoint):
            leftWordChar = inputWord[wordCount]
            rightWordChar = inputWord[wordLen - wordCount - 1]
            if (leftWordChar != rightWordChar):
                isPalindrome = False
                break

    return isPalindrome

# b) Now solve this problem using recursions. That is write a recursive function that
# checks if a word is palindrome.

# Hint: word[1:-1] will return you all letter except for first and the last. For example if
# word is “raccoon”, word[1:-1] will return you “accoo"

def palindromeCheck_Recursive(inputWord):
    wordLen = len(inputWord)
    isPalindrome = True
    wordMidPoint = (wordLen // 2)
    
    if ((wordLen <= 1)):
        pass
    else:
        leftWordChar = inputWord[0]
        rightWordChar = inputWord[wordLen - 1]
        
        if (leftWordChar == rightWordChar):
            wordBetween = inputWord[1 : wordLen-1]
            palindromeCheck_Recursive(wordBetween)
        else:
            isPalindrome = False

    return isPalindrome



print()


# using iteration
# if (palindromeCheck(word)):
#     print(f"The word '{word}' is a palindrome")
# else:
#     print(f"The word '{word}' is not a palindrome")

# print()

# using recursion
if (palindromeCheck_Recursive(word)):
    print(f"The word '{word}' is a palindrome")
else:
    print(f"The word '{word}' is not a palindrome")

