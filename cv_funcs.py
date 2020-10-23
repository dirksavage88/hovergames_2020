import numpy as np
import cv2


#cv2.destroyAllWindows()
#cv2.waitKey(0)
#read in the image
rawim = cv2.imread('/home/root/source/qrcode1.jpeg')

#to grayscale
#cv2.imwrite('rawim_grey.png', rawim)
grim = cv2.cvtColor(rawim, cv2.COLOR_BGR2GRAY)

#simple threshold
#ret,thresh2 = cv2.threshold(grim, 127, 255, 0)
#cv2.imwrite('trshim2.png', thresh2)

#now use adaptive thresholds and contours to focus on image
thresh2 = cv2.adaptiveThreshold(grim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
#thresh3 = cv2.adaptiveThreshold(rawim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,11,2)

#find contours
#contours, hcry = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print("Num. of countours: " + str(len(contours)))

#draw contours
#cim = cv2.drawContours(rawim, contours, -1, (0, 255, 0), 3)

#processed images
#cv2.imwrite('cntr_im.png', cim) 
cv2.imwrite('adap_thrsh2.png', thresh2)

 
