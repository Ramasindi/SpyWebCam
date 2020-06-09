from cv2 import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('GrEeNmAgNeT_SpY_CaM_PS: IT WONT CLOSE',frame)
    if cv2.waitKey(1) & 0xFF == ord('*'):
        break
cap.release()
cv2.destroyAllWindows()