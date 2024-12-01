import os

baseDirectory = os.path.dirname(os.path.abspath(__file__)) + '/'
passwordLog = {}
minimumPasswordLength = 8
unsecurePasswordCount = 0 

with open( baseDirectory+"input.txt", "r", encoding="UTF-8" ) as openedFile:
    fileContent = openedFile.read()
    fileContent = fileContent.strip().split()
    # print(fileContent)
    for password in fileContent:
        passwordLen = len(password)
        # print(f"{password} - {passwordLen}")
        
        try:
            passwordLenCount = passwordLog[passwordLen]
            if (passwordLenCount != ''):
                passwordLog.update({passwordLen: passwordLenCount+1})
        except KeyError:
            passwordLog[passwordLen] = 1


# passwordLogKeys = list(passwordLog.keys())
# passwordLogVals = list(passwordLog.values())
passwordLogKeys = sorted(passwordLog.keys())
passwordLogVals = sorted(passwordLog.values())

print("\nAnalysis of the Elves passwords: ")
print("____________________________________________________")
print("__Word-length___:___Count___:___Status__")
for key in passwordLogKeys:
    if (key < minimumPasswordLength):
        unsecurePasswordCount += int(passwordLog[key])
        status = "Unsecure"
    else:
        status = "Secure"
    
    print( f"> {key}-letters     -     {passwordLog[key]}    -    {status}" )
    
    
print("____________________________________________________")
print(f"\n\nSanta's new rule is a minimum of {minimumPasswordLength} characters for secure passwords")
print(f"\nWe have a total of {unsecurePasswordCount} unsecure passwords")


# ____________________________________________________
# Plotting The Graph

import numpy as np
import matplotlib.pyplot as plt

plt.xlabel('Word Lengths')
plt.ylabel('Counts')

x = list(passwordLogKeys)
y = list(passwordLogVals)
plt.plot(x,y)

plt.show()
