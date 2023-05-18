"""
Görüntü gradyanı görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir
Kenar algılamada kullanılır
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Sudoku.png",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.title("Orijinal"), plt.axis("off")

# x gradyan  ddepth parametresi outputun derinliğini gösterir
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 1, dy = 0, ksize= 5)
plt.figure(), plt.imshow(sobelx, cmap="gray"), plt.title("sobelx"), plt.axis("off")

# x gradyan  ddepth parametresi outputun derinliğini gösterir
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx = 0, dy = 1, ksize= 5)
plt.figure(), plt.imshow(sobely, cmap="gray"), plt.title("sobely"), plt.axis("off")

#Laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap="gray"), plt.title("Laplacian"), plt.axis("off")

plt.show()


