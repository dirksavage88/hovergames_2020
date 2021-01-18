import numpy as np
import cv2

#read in the image
rawim = cv2.imread('/home/root/source/qrcode1.jpeg')

#to grayscale
grim = cv2.cvtColor(rawim, cv2.COLOR_BGR2GRAY)

#now use adaptive thresholds and contours to focus on image
thresh2 = cv2.adaptiveThreshold(grim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

#processed images
#cv2.imwrite('cntr_im.png', cim) 
cv2.imwrite('adap_thrsh2.png', thresh2)

 
