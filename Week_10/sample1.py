import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 20)
# y = np.linspace(0, 200)

plt.xlabel('Word character count')
plt.ylabel('Occurences')
# plt.xticks([0,5,10,11,12,13,14,15])

# fig, ax = plt.subplots()
# ax.plot(x, y)


# x = [8, 5, 13, 7, 9, 6, 16, 2, 4, 15, 11, 12, 10]
# y = [20, 25, 65, 175, 155, 15, 15, 5, 5, 5, 5, 5, 5]

x = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16]
y = [5, 5, 5, 5, 5, 5, 15, 15, 20, 25, 65, 155, 175]
plt.plot(x,y)

plt.show()