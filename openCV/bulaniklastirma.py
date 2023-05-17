"""
Görüntü bulanıklığı, görüntünün düşük geçişli filtre uygulanmasıyla elde edilir
Gürültüyü gidermek için kullnışlıdır
OpenCV de 3 ana tür bulanıklaştırma vardır
ortalama, Gauss, medyan bulanıklaştırma
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#blurring (detayı azaltır, gürültüyü engeller)
#içe aktar normalize et
img = cv2.imread("rgbsafi.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.title("Orjinal")

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss

    return noisy

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.title("Gauss noisy")


"""
Ortalama Blur
"""
dst2 = cv2.blur(gaussianNoisyImage, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.title("Ortalama Blur")

"""
Gaussian Blur
"""
gb = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.title("Gaussian Blur")


def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    #salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    # pepper siyah
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0

    return noisy

sqImage = saltPepperNoise(img)
plt.figure(), plt.imshow(sqImage), plt.title("SP Image")

"""
Medyan Blur
"""
mb = cv2.medianBlur(sqImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb), plt.title("Medyan Blur"), plt.show()


