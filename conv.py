import cv2
import numpy as np

img = cv2.imread('zebra.png', 0)

targer_size = (500,400)
img_small = cv2.resize(img,targer_size)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

sobelx_abs = cv2.convertScaleAbs(sobelx)
sobely_abs = cv2.convertScaleAbs(sobely) # Görüntü değeri 0-255
sobelx_small = cv2.resize(sobelx_abs, targer_size)
sobely_small = cv2.resize(sobely_abs, targer_size)
cv2.imshow('Original', img_small)
cv2.imshow('Sobel X', sobelx_small)
cv2.imshow('Sobel Y', sobely_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
