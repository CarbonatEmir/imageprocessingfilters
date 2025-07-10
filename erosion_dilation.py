import cv2
import numpy as np

img = cv2.imread('kizkulesi.jpeg', 0)
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1) #bir kere uygula
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1) # Önce erode --> dilate
closing = cv2.bitwise_not(opening) # negatifi

cv2.imshow('Original', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
