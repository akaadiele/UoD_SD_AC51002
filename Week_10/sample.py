# import matplotlib.pyplot as plt
# # The slices will be ordered and plotted counter-clockwise.
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=90)
# # Set aspect ratio to be equal so that pie is drawn as a circle.
# plt.axis('equal')
# plt.show()

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# delta = 0.025
# x = np.arange(-3.0, 3.0, delta)
# y = np.arange(-2.0, 2.0, delta)
# X, Y = np.meshgrid(x, y)
# Z = np.exp(-X**2 - Y**2)
# plt.subplot(2, 1, 1)
# CS = plt.contour(X, Y, Z, 10)
# plt.clabel(CS, inline=1, fontsize=10)
# plt.title('Contour Plot')
# plt.subplot(2, 1, 2)
# t = np.arange(0,20,0.1)
# x = t
# y = np.sin(t)
# vx = (x[1:]-x[:-1])/(t[1:]-t[:-1])
# vy = (y[1:]-y[:-1])/(t[1:]-t[:-1])
# plt.plot(x,y,'b-',linewidth=2)
# plt.quiver(x[:-1],y[:-1],vx,vy,angles='xy',color='red')
# plt.title('Quiver Plot')
# plt.show()
# plt.show()


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

import os

baseDirectory = os.path.dirname(os.path.abspath(__file__)) + '/'
passwordLog = {}
minimumPasswordLength = 8
unsecurePasswordCount = 0 

with open( baseDirectory+"input.txt", "r", encoding="UTF-8" ) as openedFile:
    fileContent = openedFile.read()
    fileContent = fileContent.strip().split()
    
    for password in fileContent:
        passwordLen = len(password)
        
        try:
            passwordLenCount = passwordLog[passwordLen]
            if (passwordLenCount != ''):
                passwordLog.update({passwordLen: passwordLenCount+1})
        except KeyError:
            passwordLog[passwordLen] = 1

# for key in sorted(passwordLog.keys()):
#     print( f"{key} letter password --- {passwordLog[key]} times" )
    
#     if (key < minimumPasswordLength):
#         unsecurePasswordCount += int(passwordLog[key])

# print(f"\n\nSanta's new rule is a minimum of {minimumPasswordLength} characters for secure passwords")
# print(f"\nWe have a total of {unsecurePasswordCount} unsecure passwords \n")

print( list( sorted(passwordLog.keys()) ) )
print( list( sorted(passwordLog.values()) ) )

# ____________________________________________________
# Graph

# import numpy as np
# import matplotlib.pyplot as plt
