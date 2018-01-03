import numpy as np
import cv2
img=cv2.imread('oc.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(200,300),(255,0,0),15)
cv2.rectangle(img,(50,200),(200,300),(0,255,0),10)
cv2.circle(img,(150,100),50,(0,0,255),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'brothers',(150,220),font,1,(255,255,255),5,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('mine.jpg',img)
