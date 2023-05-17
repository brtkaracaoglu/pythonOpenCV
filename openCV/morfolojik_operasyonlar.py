"""
Erozyon, genişleme, açma, kapatma ve morfolojik
gradyan gibi morfolojik operasyonların ne olduklarını öğreneceğiz
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("neden.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.title("Orjinal"), plt.axis("off")

#Erozyon: temel fikri sadece topral erozyonu gibidir, ön plandaki nesnenin sınırlarını aşındırır
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.title("Erozyon"), plt.axis("off")

#Genişleme: erozyonun tam tersdir. Görüntüdeli beyaz bölgeyi artırır. dilation
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.title("Genisleme"), plt.axis("off")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.title("whiteNoise"), plt.axis("off")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.title("noise_img"), plt.axis("off")

#Açılma: erozyonun + genişlemedir. gürültünün giderilmesinde faydalıdır.
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.title("Acılma"), plt.axis("off")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = whiteNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.title("blackNoise"), plt.axis("off")

black_noise_img = noise_img + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.title("black_noise_img"), plt.axis("off")

#Kapatma: açmanın tersidir genişleme + erozyon. Ön plandaki nesnelerin içindeki küçük
#delikleri veya nesne  üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.title("Kapama"), plt.axis("off")

#Morfalojik Gradyan: görüntünün genişlemesi ve erozyonu arasındaki farktır  ortanın boşalması gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.title("Gradyan"), plt.axis("off")




plt.show()
