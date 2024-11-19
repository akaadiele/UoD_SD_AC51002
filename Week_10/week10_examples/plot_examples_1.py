import matplotlib.pyplot as plt
import numpy as np

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)

plt.subplot(2, 1, 1)
CS = plt.contour(X, Y, Z, 10)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Contour Plot')

plt.subplot(2, 1, 2)
t = np.arange(0,20,0.1)
x = t
y = np.sin(t)

vx = (x[1:]-x[:-1])/(t[1:]-t[:-1])
vy = (y[1:]-y[:-1])/(t[1:]-t[:-1])

plt.plot(x,y,'b-',linewidth=2)
plt.quiver(x[:-1],y[:-1],vx,vy,angles='xy',color='red')
plt.title('Quiver Plot')
plt.show()

plt.show()
