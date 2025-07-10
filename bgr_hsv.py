import cv2

img = cv2.imread('kizkulesi.jpeg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #değiştiriyoruz bgr-> hsvye

cv2.imshow('BGR', img)
cv2.imshow('HSV', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
