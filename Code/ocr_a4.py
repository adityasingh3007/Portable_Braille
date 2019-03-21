# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

try:
    from PIL import Image
except ImportError:
    import Image
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
import pytesseract
global ctr
global flag
ctr=0
flag = 0
global cap
cap=False

def initiallise():
    #print("Initiallising.......")
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(22, GPIO.RISING, bouncetime = 300)
    GPIO.add_event_callback(22, ISR_EXT_INT)

def ISR_EXT_INT(self):
    global ctr
    #print("Button pressed..")
    # do the needful
    ctr=1
    i=0
    while(not GPIO.input(22)):
        i+=1
        
def start_ocr():
    global cap
    cap = cv2.VideoCapture(0)
    print("Camera on")
   
def get_string():
    global cap
    global ctr
    global flag
    ctr=0
    flag = 0
    while 1:
        ret,image = cap.read()
        if ret == False :
            return "Vibrate 2"
        else :
            rows,cols, x= image.shape
            M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
            image = cv2.warpAffine(image,M,(cols,rows))
            if ctr>=1:
                    print("Capturing Image.....")
                    orig = image.copy()
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    gray = cv2.GaussianBlur(gray, (5, 5), 0)
                    edged = cv2.Canny(gray, 75, 200)
                    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                    cnts = imutils.grab_contours(cnts)
                    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
                    for c in cnts:
                            peri = cv2.arcLength(c, True)
                            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                            if len(approx) == 4:
                                    screenCnt = approx
                                    break
                            else :
                                flag = 1
                                break
                    if flag == 1:
                        cv2.imwrite('capture.jpg',image)
                        return "Vibrate"
                    else :
                        #print(flag)
                        print("Getting OCR....")
                        warped = four_point_transform(orig, screenCnt.reshape(4, 2))
                        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
                        T = threshold_local(warped, 11, offset = 10, method = "gaussian")
                        #warped = (warped > T).astype("uint8") * 255
                        #cv2.imshow("Scanned", warped)
                        #cv2.imshow("pers", image)
                        cv2.imwrite('capture.jpg',image)
                        cv2.imwrite('text.jpg',warped)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        return pytesseract.image_to_string(warped)
def clean():
    GPIO.clenunp()