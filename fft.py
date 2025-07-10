import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('agack.jpg', 0)

f = np.fft.fft2(img) #2d
fshift = np.fft.fftshift(f)  # sıfır frekansını->merkeze / karmaşık  sayıdan
magnitude_spectrum = 20*np.log(np.abs(fshift)) # dengeli
# 1 satır 2 sütun -> 1
plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum')
plt.show()
