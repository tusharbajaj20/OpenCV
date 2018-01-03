import numpy as np
import cv2
img=cv2.imread('oc.jpg',cv2.IMREAD_COLOR)
img[55,55]=[255,255,255]
px=img[55,55]
img[100:150,100:150]=[255,255,255]
pic=img[150:400, 250:550]
img[0:250,0:300]=pic
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('a.jpg',img)
