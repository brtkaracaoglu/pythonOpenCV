"""
Eşik değerlerinin resimler üzerindeki etkisini öğreneceğiz.
"""

import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükleyin ve renk kanallarını düzeltin
img = cv2.imread("rgbsafi.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüyü yeniden boyutlandırın
img = cv2.resize(img, (600,600))
print(img.shape)

# Yeniden boyutlandırılmış görüntüyü gösterin
plt.figure()
plt.imshow(img, cmap="gray")

# Eşikleme işlemi
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img, cmap="gray")

# Uyarlamalı eşikleme işlemi
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")

# Tüm figürleri gösterin
plt.show()

