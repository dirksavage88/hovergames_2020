#!/usr/bin/python

from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
import cv2

#test program
barcode = decode(cv2.imread('/home/root/source/code128.png'))
print(barcode)

qrcode = decode(cv2.imread('/home/root/source/adap_thrsh1.png'), symbols=[ZBarSymbol.QRCODE])
print(qrcode)


