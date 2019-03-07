import cv2
import matplotlib.pyplot as plt
import time


def main():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    angle = 0
    scale = 1

    while ret:
        ret, frame = cap.read()
        if ret:
            rows, columns, channels = frame.shape
            R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, scale)
            output = cv2.warpAffine(frame, R, (columns, rows))
            cv2.imshow("Rotating window", output)
            time.sleep(0.001)
        angle += 1
        if angle == 360:
            angle = 0
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()