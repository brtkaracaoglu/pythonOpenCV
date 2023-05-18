import cv2
import matplotlib.pyplot as plt

img = cv2.imread("catdog.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.title("orijinal")
print(img.shape)
imResized = cv2.resize(img, (500,500))
print("Resized: ",imResized.shape)
cv2.putText(img, "Catdog", (250,250),cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0))
plt.figure(),plt.imshow(img),plt.title("catdog")

_, thresh_img = cv2.threshold(img, thresh = 50, maxval = 255, type = cv2.THRESH_BINARY)
plt.figure(),plt.imshow(thresh_img),plt.title("thresh_img")

gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure(),plt.imshow(gb),plt.title("GaussianBlur")

laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
plt.figure(),plt.imshow(laplacian),plt.title("laplacian")

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)






plt.show()

