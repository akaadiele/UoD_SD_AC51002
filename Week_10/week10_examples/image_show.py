# importing required libraries 
import matplotlib.pyplot as plt 
import matplotlib.image as img 
  
# reading the image 
testImage = img.imread('lue0222a.034.png') 
  
print (testImage.shape)

# displaying the image 
plt.imshow(testImage)

cropped_image = testImage[50:200, 20:150]
plt.imshow(cropped_image)
