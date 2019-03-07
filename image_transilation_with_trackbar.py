import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

def empty_function():
    pass


def main():
    path = "/home/raj/Documents/AI/OpenCV/standard_test_images/"

    img1_path = str(path) + "cameraman.tif"
    img2_path = str(path) + "house.tif"

    img1 = cv2.imread(img1_path, 1)
    img2 = cv2.imread(img2_path, 1)


# linspace(lower_limit, upper_limit, n_of_units_to_be_devided)
# adjust the no of units to be divided and sleep time for better results

    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    windowname = "Tranilation Window"
    cv2.namedWindow(windowname)
    cv2.createTrackbar("Alpha", windowname, 0, 50, empty_function)

    
    while True:
        cv2.imshow(windowname, output)
        if cv2.waitKey(1) == 27:
            break
        alpha = cv2.getTrackbarPos("Alpha", windowname) / 10
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)


    cv2.destroyAllWindows()

    # for a good blending effect the sum of alpha and beta shoud be equal to 1
    # output = img1 * alpha + img2 * beta + gamma

    
if __name__=="__main__":
    main()
