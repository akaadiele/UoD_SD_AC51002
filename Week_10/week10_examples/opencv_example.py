

# importing required libraries of opencv
# pip install opencv-python (from VSCode Terminal)
from pickle import TRUE
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('lue0222a.034.png', 0)
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])

# show the plotting graph of an image in subplots with the image
f = plt.figure()
f.add_subplot(1,2, 1)
plt.imshow(image_rgb)
f.add_subplot(1,2, 2)
plt.plot(histr)
plt.xlim(0,255)
plt.ylim(0)
plt.show(block=TRUE)
