import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import mediapipe
import pyautogui

cap = cv2.VideoCapture(1)
detector = HandDetector(detectionCon=0.8,maxHands=2)
tamanho = [480, 640]

while True:
    success, img = cap.read(0)
    
    # img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)#,flipType=False)
    
   

    #Hand = dict (lmList - bBox - center - type)
    if hands:
        # hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #list of 21 landmarks points
        bBox1 = hand1["bbox"] # Bounding box info x,y,w,h
        centerPoint1 = hand1["center"] # center of the hand cx, cy
        handType1 = hand1["type"]  #hand type left or right
        #print(len(lmList1),lmList1)
        #print(bBox1)
        #print(centerPoint1)
        #print(handType1)
        fingers1 = detector.fingersUp(hand1)

        

        #length, info, img = detector.findDistance(lmList1[8], lmList1[12], img)

        if len(hands)==2:
            
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # list of 21 landmarks points
            bBox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx, cy
            handType2 = hand2["type"]  # hand type left or right

            fingers2 = detector.fingersUp(hand2)
            # print(fingers1, fingers2)
           
            # print(f"\n\n{lmList1}\n{lmList2}")
            height1 = lmList1[0][1]
            height2 = lmList2[0][1]
            alturaTela = tamanho[0]
            distLastFingerR = abs(lmList1[4][2] - lmList1[20][2])
            distLastFingerL = abs(lmList2[4][2] - lmList2[20][2])

            prof1 = abs(lmList1[4][0] - lmList2[4][0])

            #length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # distance between tip of the fore finger of two hands

            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img) #distance between center of two hands

    
    
            if(height1>(50+height2)): #se a altura da mão direita for maior que a mão esquerda, e se a altura da mão esquerda for maior que a metade da tela, então:
                pyautogui.press('a') #pressiona a tecla 'a'
            if(height1<abs(height2-50)): #se a altura da mão direita for maior que a mão esquerda, e se a altura da mão esquerda for maior que a metade da tela, então:
                pyautogui.press('d') #pressiona a tecla 'a'

            if prof1>200:
                 pyautogui.press('w')
            elif prof1<15:
                 pyautogui.press('s')
            print(prof1)

            # if(distLastFingerR>15):
            #      pyautogui.press('w')
            # if(distLastFingerL>10):
            #      pyautogui.press('s')



    # if(abs(height1)>tamanho[0]/2) and (height1>tamanho[0]/2) and (width1>tamanho[0]/2) and (width2>tamanho[0]/2):
         

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break