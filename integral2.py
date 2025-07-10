import cv2
import numpy as np

img = cv2.imread('ızgara.jpg', 0)
integral_img = cv2.integral(img)

print('Original shape:', img.shape)
print('Integral image shape:', integral_img.shape) #+1 satır/sutün

cv2.imshow('Original', img)
cv2.imshow('Integral Image', integral_img[1:,1:].astype(np.uint8))  ,
cv2.waitKey(0)
cv2.destroyAllWindows()