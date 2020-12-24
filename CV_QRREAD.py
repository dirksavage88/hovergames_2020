#!/usr/bin/python

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import random as rand

def capture_vid():
    try:
        cvid = cv2.VideoCapture(0)
        ret, frame = cvid.read()
        #resize the frame
        #frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)
    
        return frame
    except Exception as e:
        print("Video capture error, " + str(e))  

def process_frame(newframe):
    #grim = cv2.cvtColor(newframe, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('rawim.png', newframe)
    code_id = 0 
    for code in decode(newframe):
        try:
            print("got a code")
            code_id = rand.randint(1, 255)
            data = decode(newframe, symbols=[ZBarSymbol.QRCODE])
            (x,y,w,h) = code.rect
            cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(newframe, 'QR Code', (x,y), font, 1, (0,255,0), 2, cv2.LINE_AA)
            print(code)
            #print(data)
            code_im = 'qrcode_id_' + str(code_id) + '.png'
            cv2.imwrite(code_im, newframe) 
            #keyint = c2.waitKey(1)
            #if key == 27:
            #    break
        except Exception as e:
            print("Frame processing error, " + str(e))  

#could use generator to go through frames
def main():
    frame_post = lambda frame : process_frame(frame)
    try:
        while True:    
            nframe = capture_vid() 
            frame_post(nframe)
            #for i in range(50):    
            #    nframe = capture_vid()
            #    process_frame(nframe)
    except KeyboardInterrupt:
        print("QR service terminating")
    except Exception as e:
        print("Frame posting error, " + str(e))

main()  
