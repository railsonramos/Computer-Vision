import cv2
import numpy as np

cap = cv2.VideoCapture(0 ) #captura o vídeo da webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID') # salva um video
out = cv2.VideoWriter("output.avi", fourcc)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
