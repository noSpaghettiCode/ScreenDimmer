from cv2 import cv2
import numpy as np
import screen_brightness_control as sbc

faceCascade = cv2.CascadeClassifier('C:\\Emil\\Proiecte\\Python\\Proiecte_Python\\OpenCV\\Resources\\haar-cascade-files-master\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
width = 640
heigth = 480

cap.set(3, width)
cap.set(4, heigth)
cap.set(10, 150)

myBrigthness = sbc.get_brightness()

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    myFace = faceCascade.detectMultiScale(imgGray, 1.1, 10)

    if len(myFace) == 0:
        sbc.set_brightness(0)
    else:
        sbc.set_brightness(myBrigthness)

    for (x, y, w, h) in myFace:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
    
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break