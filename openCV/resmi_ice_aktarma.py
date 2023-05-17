import cv2

##resim içe aktarma
img = cv2.imread("safi.JPG",0) #0 grey skcala 1 rgb olarak import etmemizi sağlar
cv2.imshow("ilk Resim", img) #görsellestir
cv2.imwrite("safi_gray.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


