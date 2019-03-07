import cv2
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/peppers_color.tif"
img = cv2.imread(imgpath)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# computing negetive images

img3 = abs(255-img1)
img4 = abs(255-img2)

titles = ["Color Image", "Gray Image", "Color negetive", "Gray Negitive"]
images = [img1, img2, img3, img4]

plt.subplot(2,2,1)
plt.title(titles[0])
plt.imshow(images[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.title(titles[1])
plt.imshow(images[1], cmap='gray')
plt.xticks([])
plt.xticks([])


plt.subplot(2,2,3)
plt.title(titles[2])
plt.imshow(images[2])
plt.xticks([])
plt.yticks([])


plt.subplot(2,2,4)
plt.title(titles[3])
plt.imshow(images[3], cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()