# -*- coding: utf-8 -*-
import shutdown
import converter
import ocr_book
import ocr_a4
import RPi.GPIO as GPIO
import time
import string
import cv2
import feedback

def initiallise():
    shutdown.welcome_screen()
    feedback.start()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(38,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    shut_left_status = GPIO.input(37)
    shut_right_status = GPIO.input(38)

    if(shut_left_status and shut_right_status):
        print("Error in shutdown switch....")
        print("Exiting....")
        exit(0)
    elif(shut_left_status):
        #print("Initial position is right, turn left to switch off")
        GPIO.add_event_detect(38, GPIO.RISING)
        GPIO.add_event_callback(38, ISR_shutdown)
    else:
        #print("Initial position is left turn right to switch off")
        GPIO.add_event_detect(37, GPIO.RISING)
        GPIO.add_event_callback(37, ISR_shutdown)

def ISR_shutdown(self):
    print("Turning off")
    shutdown.now()
    exit(0)

if __name__ == "__main__":
    initiallise()  
    print("\nTurning Camera On........")
    ocr_a4.initiallise()
    time.sleep(0.8)
    feedback.camera_start()
    ocr_a4.start_ocr()
    ocr=ocr_a4.get_string()
    while(1):
        if(ocr=="Vibrate 2"):
            print("Camera error")
            feedback.camera_error()
            ocr=ocr_a4.get_string()
        elif(ocr=="Vibrate"):
            print("Corner error")
            feedback.image_error()
            ocr=ocr_a4.get_string()
        elif(ocr==""):
            print("OCR error")
            feedback.image_error()
            ocr=ocr_a4.get_string()
        else:
            break    
    print("")
    print(ocr)
    print("")
    ocr_new=""
    for i in ocr:
        if i=='\n':
            i=" "
        ocr_new+=i
    ocr_new=ocr_new[0:len(ocr_new)-1]
    new_word=""
    for j in range(0,len(ocr_new)):
        i=ocr_new[j]
        if(j==len(ocr_new)-1):
            #print(len(new_word))
            converter.get_braille(new_word)
            new_word=""
        if(i.isalpha() or i in string.punctuation or i.isnumeric()):
            new_word+=i
        elif(len(new_word)!=0):
            #print(len(new_word))
            converter.get_braille(new_word)
            time.sleep(2)
            new_word=""
        else:
            new_word=""
    print("\nExiting......")
    coverter.clean()
    feedback.clean()
    ocr_a4.clean()
    GPIO.cleanup()