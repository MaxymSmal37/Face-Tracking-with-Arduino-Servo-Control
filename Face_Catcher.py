import cv2

import serial
import time
import serial, time
arduino = serial.Serial()
arduino.port="COM4"
arduino.baudrate=9600
arduino.open()
time.sleep(2)
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    #img = cv2.imread("IMG_20191012_145410_3.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

        
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)

        if x<= img.shape[0]//3:
            print("left")
            arduino.write(b'l')
            
            
        elif x>=2*(img.shape[0]//3):
            print("right")
            arduino.write(b'r')
            

        else:
           print("center")
           arduino.write(b'c')
           
 
    cv2.imshow('rez', img)
    #print(x)
   
    
    #cv2.waitKey()
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()







 

       




