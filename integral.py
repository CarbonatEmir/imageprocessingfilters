import cv2
import numpy as np

img = cv2.imread('ızgara.jpg', 0)
integral_img = cv2.integral(img)
integral_log = np.log(integral_img[1:, 1:] + 1)
integral_norm = cv2.normalize(integral_log, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


alpha = 0.5
blend = cv2.addWeighted(img, alpha, integral_norm, 1 - alpha, 0)


color_map = cv2.applyColorMap(integral_norm, cv2.COLORMAP_JET)

cv2.imshow('Original', img)
cv2.imshow('Integral Image (Normalized)', integral_norm)
cv2.imshow('Blend Original & Integral', blend)
cv2.imshow('Integral Image Color Map', color_map)

cv2.waitKey(0)
cv2.destroyAllWindows()
