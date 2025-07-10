import cv2

img = cv2.imread('kizkulesi.jpeg')
downsampled = cv2.pyrDown(img)

cv2.imshow('Original', img)
cv2.imshow('Downsampled', downsampled)
cv2.waitKey(0)
cv2.destroyAllWindows()
