import os
import string as s

baseDirectory = os.path.dirname(os.path.abspath(__file__))
novel_words = []

def clean_word(word):
    new_word = ""
    for char in word:
        if (char in s.ascii_letters):
            new_word += char
        else:
            new_word += ' '
    return new_word.split()

print('\n\n')
# c) Write a function called words_of_len(words, n) that takes exactly two arguments
# called words and n, where words is a list of words and n is a positive integer. 
# The function returns a list of all words of length n. Test this function with:
# words_of_len(novel_words,16) should return
# ['indiscriminately', 'impracticability', 'perpendicularity',
# 'inextinguishable'].
def words_of_len(words, n):
    wordList = []
    for word in words:
        if (len(word) == n):
            wordList.append(word)
            # print(word)
    wordSet = set(wordList)
    wordList = list(wordSet)
    # print(wordSet)
    return wordList

print('\n\n')
# d) Write a function called unique_words(words) that takes exactly one positional
# argument called words, where words is a list of words. The function returns a list of
# unique words in the list words. 
def unique_words(words):
    wordsUnique = set(words)
    return list(wordsUnique)

with open(baseDirectory + "/frankenstein.txt", "r", encoding="UTF-8") as openedFile:
    # fileContent = openedFile.read()
    # print(fileContent)
    for line in openedFile:
        # print(line)
        cleaned_line = line.strip() # Remove trailing line breaks
        words = cleaned_line.split() # Split the line
        # print(words)
        cleaned_words = []
        for i in range(len(words)):
            word = words[i].lower()
            cleaned_words.extend(clean_word(word))
        # print(cleaned_words)
        novel_words.extend(cleaned_words)
    

# print(novel_words)
words4 = words_of_len(novel_words, 4)
words5 = words_of_len(novel_words, 5)
words6 = words_of_len(novel_words, 6)
words7 = words_of_len(novel_words, 7)


# print(f"{len(words4)} , {len(words5)} , {len(words6)} , {len(words7)}")

# Use this function to find the total number of words in the novel with lengths between
# 4 and 7 letters (inclusive) and print this number. The output should be:
# There are [NUM_WORDS] words with lengths between 4 and 7 (inclusive).
NUM_WORDS = len(words4) + len(words5) + len(words6) + len(words7)
print(f"There are {NUM_WORDS} words with lengths between 4 and 7 (inclusive).")



print()

# For example:
# unique_words([‘papaya’,’papaya’,’mango’])
# should return [‘papaya’,’mango’]
print(unique_words(['papaya','papaya','mango',]))


# e) Use your function unique_words to count the number of unique words of length 4 in the novel:
# The output should be:
# There are [NUM_WORDS] words of length 4 in the text.
# Where [NUM_WORDS] is the result of your calculation of the unique words with 4 letters.