import os, time

baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/"
elfPasswords = "input.txt"
passwordWordLog = { }; passwordCountLog = {} ; passwordsPerWordLength = {}
minimumPasswordLength = 8
validPasswordCount = invalidPasswordCount = 0


def checkForNumber(passwordToCheck):
    hasNumber = any(char.isdigit() for char in passwordToCheck)
    return hasNumber


try:
    # ____________________________________________________
    # Reading file
    with open(baseDirectory + elfPasswords, "r", encoding="UTF-8") as openedFile:
        fileContent = openedFile.read()
        fileContent = fileContent.strip().split()

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

        # dict(sorted(passwordWordLog.items()))
        # sorted(passwordWordLog.items())
        
        passwordWordLogSorted = {}
        for countKey in sorted(passwordWordLog.keys()):
            passwordWordLogSorted[countKey] = sorted(passwordWordLog[countKey])
        passwordWordLog = passwordWordLogSorted
        
        passwordWordLogKeys = passwordWordLog.keys()        ; # Used in password analysis
        passwordWordLogVals = passwordWordLog.values()        ; # Used in password analysis
        print(passwordWordLogKeys)
        print(passwordWordLogVals)
        
        
        # dict(sorted(passwordCountLog.items()))
        # sorted(passwordCountLog.items())
        print()
        passwordCountLogKeys = passwordCountLog.keys()      ; # used in plotting graph (x axis)
        passwordCountLogVals = passwordCountLog.values()      ; # used in plotting graph (y axis)
        # print(passwordCountLogKeys)
        # print(passwordCountLogVals)
    
        passwordCountLogSorted = {}
        for countKey in sorted(passwordCountLog.keys()):
            passwordCountLogSorted[countKey] = passwordCountLog[countKey]
        passwordCountLog = passwordCountLogSorted
        # print(passwordCountLog)
        # print(passwordCountLogSorted)
        passwordCountLogKeys = passwordCountLog.keys()      ; # used in plotting graph (x axis)
        passwordCountLogVals = passwordCountLog.values()      ; # used in plotting graph (y axis)
        print(passwordCountLogKeys)
        print(passwordCountLogVals)
    
    # ____________________________________________________
    # Checking for valid passwords
        print("\n***Santa's new rules for valid passwords:")
        print(f"   > Each password must be at least '{minimumPasswordLength}' characters long")
        print(f"   > And contain at least one number")
        time.sleep(1)
        
        # passwordWordLogKeys
        # passwordWordLogVals

        print("\nAnalysis of the Elves passwords: ")
        print("____________________________________________________")
        print("__Word length___:___Count___:___With Number___")
        for key in passwordWordLogKeys:
            if key < minimumPasswordLength:
                # Invalid password - less than minimum length 
                # For all words in that word length
                invalidPasswordCount += int( len(passwordWordLog[key]) )
            else:
                for password in passwordWordLog[key]:
                    if ( checkForNumber(password) == False ):
                        # Invalid password - does not contain at least a number
                        invalidPasswordCount += 1
                    else:
                        # Valid password - meets minimum length and contains at least a number
                        validPasswordCount += 1
                    

        print("____________________________________________________\n")
        print(f"Total invalid passwords : {invalidPasswordCount}")
        print(f"Total valid passwords : {validPasswordCount}")

    # ____________________________________________________
    # # Plotting The Graph
    # import numpy as np
    # import matplotlib.pyplot as plt

    # if (passwordCountLogKeys != "") and (passwordCountLogVals != ""):
    #     plt.xlabel("Word Length")
    #     plt.ylabel("Count")

    #     xAxisValues = list(passwordCountLogKeys)
    #     yAxisValues = list(passwordCountLogVals)
    #     plt.plot(xAxisValues, yAxisValues)
    #     plt.title("Elves' Passwords Word Lengths\n(Prepared for Santa)")

    #     plt.show()

except FileNotFoundError:
    print("File for elves passwords not found")
