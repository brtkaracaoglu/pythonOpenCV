"""
görüntülerin perspektifini ayarlamayı öğreneceğiz
"""

import cv2
import numpy as np

img = cv2.imread("iskambil.jpg")
cv2.imshow("Orijinal", img)


width = 400
height = 500
pts1 = np.float32([[230,1], [1,472], [540,150], [338,617]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#dönüştürülmüş hali resmin
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Nihai Resim", imgOutput)


cv2.waitKey(0)
cv2.destroyAllWindows()