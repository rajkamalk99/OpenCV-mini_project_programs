import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # BLUE COLOR
        low = np.array([100,50,50])
        high = np.array([140,255,255])

# we can repete this for other colours such as green and red by specifing the low and high levels of the required color to be detected.

        image_mask = cv2.inRange(hsv, low, high)
        output = cv2.bitwise_and(frame, frame, mask=image_mask)
        cv2.imshow("Output Window", output)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
 