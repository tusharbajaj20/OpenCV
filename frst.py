import cv2
import numpy as np
import matplotlib as plt

img= cv2.imread('oc.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('my.jpg',img)
