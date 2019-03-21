# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cv2
import numpy as np
import math

global flag
global ctr
global cap
global X
global Y
flag = 0
ctr = 0
cap = False
X = False
Y = False

def initiallise():
    #print("Initiallising.......")
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(22, GPIO.RISING, bouncetime = 300)
    GPIO.add_event_callback(22, ISR_EXT_INT)


def ISR_EXT_INT(self):
    global flag
    print("Button pressed..")
    # do the needful
    flag = 1
    print(ctr)
    i=0
    while(not GPIO.input(22)):
        i+=1

def dist(xa,ya,xb,yb) :
    dst = abs(math.sqrt((xa-xb)**2 + (ya-yb)**2))
    return dst

def start_ocr():
    global cap
    global X
    global Y
    cap = cv2.VideoCapture(0)
    X = np.array([0,0,0,0])
    Y = np.array([0,0,0,0])

def get_string():
    global cap
    global X
    global Y
    global flag
    global ctr

    while 1:
        ret,frame = cap.read()
        if ret == False :
            return "Vibrate 2"
        #ret = cap.set(3,1280)
        #ret = cap.set(4,720)
        #frame = cv2.imread('17.jpg')
        rows,cols, x= frame.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        frame = cv2.warpAffine(frame,M,(cols,rows))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     
        low = np.array([0, 0, 0])
        high = np.array([180, 25, 25])
        mask = cv2.inRange(hsv, low, high)
        if flag == 1 and ctr < 4 :
            image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            a=len(contours)
            count = 0
            for i in range (a) :
                x,y,w,h = cv2.boundingRect(contours[i])
                if cv2.contourArea(contours[i])>1000 and cv2.contourArea(contours[i])<10000:
                    contours[count] = contours[i]
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
                    count = count + 1
            contours = contours[0:count]
            if len(contours) ==  1 :
                x,y,w,h = cv2.boundingRect(contours[0])
                cy = y+h/2
                Y[ctr] = cy
                cx = x + w/2
                X[ctr] = cx
                ctr = ctr + 1
            else:
                return "Vibrate"
                #print(len(contours))
        flag = 0
        if ctr == 4:
            print(X,Y)
            b = int(dist(X[0],Y[0],X[1],Y[1]))
            l = int(dist(X[0],Y[0],X[2],Y[2]))
            pts1 = np.float32([[X[0],Y[0]],[X[1],Y[1]],[X[2],Y[2]],[X[3],Y[3]]])
            pts2 = np.float32([[0,0],[b,0],[0,l],[b,l]])
            M = cv2.getPerspectiveTransform(pts1,pts2)
            ocr = cv2.warpPerspective(frame,M,(b,l))
            cv2.imwrite('hi.jpg',ocr)
            break
        cv2.imshow("mask",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit(0)
    text=pytesseract.image_to_string(ocr)
    flag = 0
    ctr = 0
    cap.release()
    cv2.destroyAllWindows()
    X = False
    Y = False
    return text