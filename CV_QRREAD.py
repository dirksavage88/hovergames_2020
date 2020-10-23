#!/usr/bin/python

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol

def capture_vid():
    cvid = cv2.VideoCapture(0)
    ret, frame = cvid.read()
    
    #resize the frame
    #frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
    
    return frame

def process_frame(newframe):
    #grim = cv2.cvtColor(newframe, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('rawim.png', newframe) 
    for code in decode(newframe):
        print("got a code")
        decode(newframe, symbols=[ZBarSymbol.QRCODE])
        (x,y,w,h) = code.rect
        cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(newframe, 'QR Code', (x,y), font, 1, (0,255,0), 2, cv2.LINE_AA)
        print(code)
        cv2.imwrite('det_qrcode.png', newframe) 
        #keyint = c2.waitKey(1)
        #if key == 27:
        #    break
#could use generator to go through frames
#lambdas for quick functions
for i in range(50):    
    nframe = capture_vid()
    process_frame(nframe)
print("done")
  
