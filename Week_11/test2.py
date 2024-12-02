# # print(passwordWordLogVals)
# print()
# for i in sorted(passwordWordLogKeys):
#     for j in passwordWordLog[i]:
#         print(j)


def checkForNumber(passwordToCheck):
    # hasNumber = any(char.isdigit() for char in passwordToCheck)
    hasNumber = False
    for char in passwordToCheck:
        if ( char.isdigit() ):
            hasNumber = True
            break
        else:
            pass

    return hasNumber

a = checkForNumber('yk7xCR8hXEvmXJNy')
b = checkForNumber('xanjJDryTwrNZ')


print(a)
print(b)