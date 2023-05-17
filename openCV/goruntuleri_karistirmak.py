"""
Birden fazla görüntüyü ansıl karıştıracağımızı öğreneneğiz
"""

import cv2
import matplotlib.pyplot as plt

# Görüntüleri yükleyin ve renk kanallarını düzeltin
img1 = cv2.imread("safi_gray.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread("safiresized.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# İlk görüntüyü gösterin
plt.figure()
plt.imshow(img1)

# İkinci görüntüyü gösterin
plt.figure()
plt.imshow(img2)

# Görüntü boyutlarını kontrol edin
print(img1.shape)
print(img2.shape)

# Görüntüleri yeniden boyutlandırın
img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2, (600,600))
print(img2.shape)

# Yeniden boyutlandırılmış görüntüleri gösterin
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# Karıştırılmış resmi hesaplayın ve gösterin
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0.0)
plt.figure()
plt.imshow(blended)

# Tüm figürleri gösterin
plt.show()
