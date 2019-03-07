import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"

img = cv2.imread(imgpath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

titles = ["Original Image", "RED", "GREEN", "BLUE"]
images = [cv2.merge((r,g,b)), r, g, b]

plt.subplot(2, 2, 1)
plt.title(titles[0])
plt.imshow(images[0])
plt.xticks([])
plt.yticks([])

# range doesnot include the given upper bound

for i in range(3):
    plt.subplot(2, 2, i+2)
    plt.title(titles[i+1])
    plt.imshow(images[i+1], cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()

