import os, time
import numpy as np
import matplotlib.pyplot as plt

elfPasswordsFileName = "input.txt"
baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/"
passwordWordLog = { }; passwordCountLog = {} ; passwordsPerWordLength = {}
minimumPasswordLength = 8 ; validPasswordCount = 0 ; invalidPasswordCount = 0


def checkForNumber(passwordToCheck):
    hasNumber = False
    # hasNumber = any(char.isdigit() for char in passwordToCheck)
    
    for char in passwordToCheck:
    # Loop through each charater checking if it is a digit
        if ( char.isdigit() ):
            # A digit has been found
            hasNumber = True
            break
        else:
            # Character is not a digit
            pass

    return hasNumber

try:
    # Reading file
    with open(baseDirectory + elfPasswordsFileName, "r", encoding="UTF-8") as openedFile:
        fileContent = openedFile.read()
        fileContent = fileContent.strip().split()
        fileContentCount = len(fileContent)

        for password in fileContent:
            passwordLen = len(password)
            
            try:
                passwordsPerWordLength = passwordWordLog[passwordLen]
                passwordLenCount = passwordCountLog[passwordLen]
                if ( (passwordsPerWordLength != "") or (passwordsPerWordLength != []) ):
                    passwordsPerWordLength.append(password)
                    passwordWordLog.update( {passwordLen: passwordsPerWordLength} )
                    
                    passwordCountLog.update({passwordLen: passwordLenCount + 1})
            except KeyError:
                passwordWordLog[passwordLen] = password.split()     ; # Keep track of all words for each word length
                passwordCountLog[passwordLen] = 1       ; # Keep track of the number of words for each word length

        
        # Sorting the dictionary by keys
        passwordWordLogSorted = {}
        for countKey in sorted(passwordWordLog.keys()):
            passwordWordLogSorted[countKey] = sorted(passwordWordLog[countKey])
        
        passwordWordLog = passwordWordLogSorted
        passwordWordLogKeys = passwordWordLog.keys()        ; # Used in password analysis
        passwordWordLogVals = passwordWordLog.values()        ; # Used in password analysis
        
        
        # Sorting the dictionary by keys
        passwordCountLogSorted = {}
        for countKey in sorted(passwordCountLog.keys()):
            passwordCountLogSorted[countKey] = passwordCountLog[countKey]
        
        passwordCountLog = passwordCountLogSorted
        passwordCountLogKeys = passwordCountLog.keys()      ; # used in plotting graph (x axis)
        passwordCountLogVals = passwordCountLog.values()      ; # used in plotting graph (y axis)
        
    # ____________________________________________________
    # Checking for valid passwords based on Santa's new rules
        print("____________________________________________________\n")
        print("***Santa's new rules for valid passwords:")
        print(f"   > Each password must be at least {minimumPasswordLength} characters long")
        print(f"   > And contain at least one number")
        time.sleep(1)
        
        
        print("____________________________________________________\n")
        print("Analysis of the Elves passwords: \n")
        
        # For each word length, loop through each set of words and check against santa's rules
        for key in passwordWordLogKeys:
            if key < minimumPasswordLength:
                # Invalid password - less than minimum length 
                # For all words in that word length
                invalidPasswordCount += int( len(passwordWordLog[key]) )
            else:
                for passwordWord in passwordWordLog[key]:
                    hasNumber = checkForNumber(passwordWord)
                    if ( hasNumber == False ):
                        # Invalid password - does not contain at least a number
                        invalidPasswordCount += 1
                    else:
                        # Valid password - meets minimum length and contains at least a number
                        validPasswordCount += 1

        print(f"Total elves passwords checked : {fileContentCount}")
        print(f"Total valid passwords : {validPasswordCount}")
        print(f"Total invalid passwords : {invalidPasswordCount}")
        print("____________________________________________________\n")

    # ____________________________________________________
    # # Plotting The Graph

    if (passwordCountLogKeys != "") and (passwordCountLogVals != ""):
        plt.xlabel("Word Length")
        plt.ylabel("Count")

        xAxisValues = list(passwordCountLogKeys)
        yAxisValues = list(passwordCountLogVals)
        plt.plot(xAxisValues, yAxisValues)
        plt.title("Elves' Passwords Word Lengths\n(Prepared for Santa)")
        
        plt.show()

except FileNotFoundError:
    print("File for elves passwords not found")
