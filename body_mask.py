import cv2
import numpy as np

cap = cv2.VideoCapture(1)

def nothing(x):
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 500, 500)

cv2.createTrackbar("Lower - H", "TrackBar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "TrackBar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "TrackBar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "TrackBar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "TrackBar", 0, 255, nothing)

cv2.setTrackbarPos("Upper - H", "TrackBar", 180)
cv2.setTrackbarPos("Upper - S", "TrackBar", 255)
cv2.setTrackbarPos("Upper - V", "TrackBar", 255)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H", "TrackBar")
    lower_s = cv2.getTrackbarPos("Lower - S", "TrackBar")
    lower_v = cv2.getTrackbarPos("Lower - V", "TrackBar")

    Upper_h = cv2.getTrackbarPos("Upper - H", "TrackBar")
    Upper_s = cv2.getTrackbarPos("Upper - S", "TrackBar")
    Upper_v = cv2.getTrackbarPos("Upper - V", "TrackBar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    Upper_color = np.array([Upper_h, Upper_s, Upper_v])

    mask = cv2.inRange(frame_hsv, lower_color, Upper_color)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
