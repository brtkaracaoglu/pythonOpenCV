import cv2
import time

#video ismi
video_name = "MOT17.mp4"
#video içe aktar: capture, cap

cap = cv2.VideoCapture(video_name)
print("Genişlik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))
if cap.isOpened() == False:
    print("HATA")

while True:

    ret, frame = cap.read()
    if ret == True:
        time.sleep(0.01)# uyarı kullanmazsak çok hızlı oynar
        cv2.imshow("Video", frame)# görsellestirme
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release() # stop capture
cv2.destroyAllWindows()

