import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 2304 x 1296 gets me 1280x720
cap.set(4, 2304.0)
cap.set(3, 1296.0)

print str(cap.get(3)),str(cap.get(4))

ret, frame = cap.read()

while(1):
    ret, frame = cap.read()
    cv2.imshow('frame.jpg', frame)
    cv2.imwrite('frame.jpg', frame)
    k = cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()
