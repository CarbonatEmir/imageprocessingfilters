import cv2
import numpy as np
import matplotlib.pyplot as plt

def compute_fft_magnitude(gray_img):
    f = np.fft.fft2(gray_img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)  # sıfır log
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    return magnitude_spectrum.astype(np.uint8)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.convertScaleAbs(cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0))

    # FFT magnitüd spektrumu hız için
    small_gray = cv2.resize(gray, (128, 128))
    magnitude = compute_fft_magnitude(small_gray)
    magnitude_color = cv2.applyColorMap(magnitude, cv2.COLORMAP_JET)


    cv2.imshow('Original', gray)
    cv2.imshow('Sobel Edge', sobel)
    cv2.imshow('FFT Magnitude Spectrum (128x128)', magnitude_color)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
