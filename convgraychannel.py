import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ret,img=cam.read()
    
    b=np.copy(img)
    b[:,:,2]=0
    b[:,:,1]=0
    cv2.imshow("B",b)    

    g=np.copy(img)
    g[:,:,0]=0
    g[:,:,2]=0
    cv2.imshow("g",g)  

    r=np.copy(img)
    r[:,:,0]=0
    r[:,:,1]=0
    cv2.imshow("r",r)  






    if cv2.waitKey(1)==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()