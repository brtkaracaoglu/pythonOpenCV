"""2 ayrı görüntünün birleştirilmesi
"""

import cv2
import numpy as np
#resmi içe aktar
img = cv2.imread("safi_gray.jpg")
cv2.imshow("Orijinal resim",img)

#yatay
hor = np.hstack((img,img))
cv2.imshow("yatay", hor)

#dikey
ver = np.vstack((img,img))
cv2.imshow("dikey", ver)

cv2.waitKey(0)
cv2.destroyAllWindows()

