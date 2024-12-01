import os, time
import numpy as np
import matplotlib.pyplot as plt

baseDirectory = os.path.dirname(os.path.abspath(__file__)) + "/"
elfPasswords = "input.txt"
passwordLog = {}
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
                passwordLenCount = passwordLog[passwordLen]
                if passwordLenCount != "":
                    passwordLog.update({passwordLen: passwordLenCount + 1})
            except KeyError:
                passwordLog[passwordLen] = 1

        passwordLogKeys = sorted(passwordLog.keys())
        passwordLogVals = sorted(passwordLog.values())
    
    # ____________________________________________________
    # Checking for valid passwords
        print("\n***Santa's new rules for valid passwords:")
        print(f"  > Each password must be at least '{minimumPasswordLength}' characters long")
        print(f"  > And contain at least one number")
        time.sleep(1)

        print("\nAnalysis of the Elves passwords: ")
        print("____________________________________________________")
        print("__Word-length___:___Count___:___Status__")
        for key in passwordLogKeys:
            if key < minimumPasswordLength:
                invalidPasswordCount += int(passwordLog[key])
                status = "Invalid"
            else:
                if ( checkForNumber(passwordLog[key]) == False ):
                    invalidPasswordCount += int(passwordLog[key])
                    status = "Invalid"
                else:
                    validPasswordCount += int(passwordLog[key])
                    status = "Valid"

            print(f"> {key}-letters     -     {passwordLog[key]}    -    {status}")

        print("____________________________________________________\n")
        print(f"Total invalid passwords : {invalidPasswordCount}")
        print(f"Total valid passwords : {validPasswordCount}")

    # ____________________________________________________
    # Plotting The Graph
    if (passwordLogKeys != "") and (passwordLogVals != ""):
        plt.xlabel("Word Length")
        plt.ylabel("Count")

        xAxisValues = list(passwordLogKeys)
        yAxisValues = list(passwordLogVals)
        plt.plot(xAxisValues, yAxisValues)
        plt.title("Elves' Passwords Word Lengths\n(Prepared for Santa)")

        plt.show()

except FileNotFoundError:
    print("File for elves passwords not found")
