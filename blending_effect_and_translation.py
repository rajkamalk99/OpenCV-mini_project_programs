import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    path = "/home/raj/Documents/AI/OpenCV/standard_test_images/"

    img1_path = str(path) + "cameraman.tif"
    img2_path = str(path) + "house.tif"

    img1 = cv2.imread(img1_path, 1)
    img2 = cv2.imread(img2_path, 1)


# linspace(lower_limit, upper_limit, n_of_units_to_be_devided)
# adjust the no of units to be divided and sleep time for better results

    for i in np.linspace(0,1,100):
        alpha = i
        beta = 1 - i
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow("Transilation", output)
        time.sleep(0.05)
        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()

    # for a good blending effect the sum of alpha and beta shoud be equal to 1
    # output = img1 * alpha + img2 * beta + gamma

    
if __name__=="__main__":
    main()
