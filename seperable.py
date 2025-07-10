import cv2

img = cv2.imread('kizkulesi.jpeg', 0)
blur = cv2.GaussianBlur(img, (15,15), 0)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
