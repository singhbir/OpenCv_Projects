import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_a=np.array([110,50,50])
    u_a=np.array([213,108,255])
    mask=cv2.inRange(hsv,l_a,u_a)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("color frame",res)
    cv2.imshow("mask",mask)
    cv2.imshow("original",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
