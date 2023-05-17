import cv2

#
img = cv2.imread("resim_video_kayitlari/safi.JPG",1)
print("Resim Boyutu: ", img.shape)
cv2.imshow("Orjinal", img)

#resized boyutlandırma
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("img Resized", imgResized)
cv2.imwrite("resim_video_kayitlari/rgbsafi.jpg", img)


#kırpma

imgCropped = img[:200,0:300] #height  width
cv2.imshow("Kirpik Resim", imgCropped)



cv2.waitKey(0)
cv2.destroyAllWindows()