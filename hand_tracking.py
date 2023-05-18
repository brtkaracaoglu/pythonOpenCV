import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

# mediapipe'nin elleri tespit etmek için kullanılacak olan sınıfını tanımla
mpHand = mp.solutions.hands

# Elleri tespit etmek için hands sınıfının bir örneğini oluştur
hands = mpHand.Hands()

# Eller üzerinde çizim yapmak için mediapipe'nin drawing_utils sınıfını kullan
mpDraw = mp.solutions.drawing_utils

# FPS hesaplama için kullanılacak değişkenler
pTime = 0
cTime = 0

while True:
    # Kameradan bir kare al
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Elleri tespit et
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Tespit edilen ellerin üzerine çizgileri çiz
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
            
            for id, lm in enumerate(handLms.landmark):
                # Her bir el noktasının (landmark) sıra numarasını (id) ve konumunu (lm) al
                # lm.x, lm.y, lm.z değerleri oranlar olduğundan görüntünün boyutlarına (w, h) göre hesaplanır
                h, w, c = img.shape
                
                cx, cy = int(lm.x*w), int(lm.y*h) 
                
                # Bileği temsil eden noktayı çiz
                if id == 4:
                    cv2.circle(img, (cx,cy), 9, (255,0,0), cv2.FILLED)
    
    # FPS hesaplama
    cTime = time.time()
    fps = 1 / (cTime- pTime)
    pTime = cTime
    
    # FPS değerini ekrana yazdır
    cv2.putText(img, "FPS: "+str(int(fps)), (10,75), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5)
    
    # Görüntüyü ekranda göster
    cv2.imshow("img", img)
    cv2.waitKey(1)
