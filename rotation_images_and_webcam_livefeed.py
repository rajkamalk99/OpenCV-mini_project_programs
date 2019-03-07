import cv2
import matplotlib.pyplot as plt
import time


def main():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    angle = 0

    while True:
        if angle == 360:
            angle = 0
        rows, columns, channels = img.shape
        R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, 1)
        output = cv2.warpAffine(img, R, (columns, rows))
        angle += 1
        cv2.imshow("Rotating window", output)
        time.sleep(0.001)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()