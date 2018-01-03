import numpy as np
import cv2
from PIL import Image
img=cv2.imread('crsr.jpg')
img2=cv2.imread('madrid.jpg')

rows,cols,channels=img.shape
img2=img2[0:rows,0:cols]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,250,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img_bg=cv2.bitwise_and(img2,img2,mask=mask_inv)

img2_fg=cv2.bitwise_and(img2,img2,mask=mask)
dst=cv2.add(img_bg,img2_fg)
img[0:rows,0:cols]=dst
cv2.imshow('Real',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Real.jpg',dst)
