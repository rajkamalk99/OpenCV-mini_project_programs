import cv2 
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread("/home/raj/Downloads/pixil-frame-0.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask = cv2.imread("/home/raj/Downloads/mask.png", 0)

    output1 = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)
    output2 = cv2.inpaint(img, mask, 5, cv2.INPAINT_NS)

    images = [img, output1, output2]
    titles = ["Original Image", "TELEA", "NS"]
    for i in range(len(titles)):
        plt.subplot(1,3,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
    
    plt.show()


if __name__=="__main__":
    main()