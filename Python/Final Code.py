import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        center = (x+w//2, y+h//2)
        radius = (w+h)//4
        cv2.circle(image, center, radius, (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 1)

        
        
        
    # Display the output
    video = cv2.flip(image,1)
    cv2.imshow('image', video)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == 32:
        print("X Location:",x,"\nY Location:",y,"\n")
    if k == 115:
        a = x
        b = y
        print("User x profile = ",a,"\nUser y profile = ",b,'\n')
    if k == 103:
        X_Displacement = x - a
        Y_Displacement = y - b
        print("Motor to move:",X_Displacement,"units in x direction\n")
        print("Motor to move:",Y_Displacement,"units in y direction\n")
        
# Release the VideoCapture object
cap.release()
