#!/usr/bin/python

import cv2, json
import numpy as np
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from time import sleep
import random as rand

def capture_vid():
    try:
        #cvid = cv2.VideoCapture(0)
        cap_handle = cv2.VideoCapture('v4l2src ! video/x-raw,width=640,height=480 ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
        ret, frame = cap_handle.read()
        return frame, cap_handle
    except Exception as e:
        print("Video capture error, " + str(e))  

def process_frame(newframe):
    #grim = cv2.cvtColor(newframe, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('rawim.png', newframe)
    code_id = 0
    log_data = {"Code ID" : "", "Decoded Data" : ""} 
    for code in decode(newframe):
        try:
            print("received code")
            code_id = rand.randint(1, 255)
            data = decode(newframe, symbols=[ZBarSymbol.QRCODE])
            (x,y,w,h) = code.rect
            cv2.rectangle(newframe,(x,y),(x+w,y+h),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(newframe, 'QR Code', (x,y), font, 1, (0,255,0), 2, cv2.LINE_AA)
            code_im = 'qrcode_id_' + str(code_id) + '.png'
            cv2.imwrite(code_im, newframe) 
            log_data['Code ID'] = str(code_id)
            log_data['Decoded Data'] = str(code)
            with open("log.txt", "a+") as logging_dat:
                json_str = json.dumps(log_data)
                logging_dat.write(json_str + '\n')
            #keyint = c2.waitKey(1)
        except Exception as e:
            print("Frame processing error, " + str(e))  

#could use generator to go through frames
def main():
    chandle = None
    frame_post = lambda frame : process_frame(frame)
    try:
        while True:    
            nframe, chandle = capture_vid() 
            frame_post(nframe)
            chandle.release()
            sleep(5)
    except KeyboardInterrupt:
        if chandle != None:
            chandle.release()
            print("Video capture released")
        print("QR service terminating")
    except Exception as e:
        if chandle != None:
            chandle.release()
            print("Video capture released")
        print("Main posting error, " + str(e))

if __name__ == '__main__':
    main()  
