"""
görüntü histogramı, dijital görüntüdeki ton dağılımının grefiksel bir temsili olarak işlev gören
bir histogram türüdür. Her bir ton değeri için piksel sayısını içerir.
belirli bir görüntü için histograma bakılarak, ton dağılımı anlaşılabilir.
"""
import cv2
import matplotlib.pyplot as plt
import  numpy as np

img = cv2.imread("turkbayragi.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis), plt.title("img_vis")
print(img.shape)
img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist), plt.title("img_hist")

color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color = c)

#maskeleme
mask = np.zeros(img_vis.shape[:2], np.uint8)
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("mask")

mask[150:500,100:500] = 255
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("mask")

masked_img_vid = cv2.bitwise_and(img_vis,img_vis, mask = mask)
plt.figure(), plt.imshow(masked_img_vid, cmap="gray"), plt.title("masked_img_vid")
masked_img_hist = cv2.calcHist([img_vis], channels = [0], mask = mask, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(masked_img_hist), plt.title("masked_img_hist")

#histogram eşitleme

img = cv2.imread("safi_gray.jpg",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.title("img")

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist), plt.title("img_hist")

eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray"), plt.title("eq_hist")

eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eq_img_hist), plt.title("eq_img_hist")

plt.show()

