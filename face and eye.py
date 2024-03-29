import cv2
import numpy as np
face=cv2.CascadeClassifier('face.xml')
eye=cv2.CascadeClassifier('eye.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    eyes = eye.detectMultiScale(gray,1.3,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30)&0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
