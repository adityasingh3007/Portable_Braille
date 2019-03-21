# -*- coding: utf-8 -*-
import Braille_Dictionary_Grade_1 as GD1
import Braille_Dictionary_Grade_2 as GD2
import Actuator
import string
from time import sleep
import RPi.GPIO as GPIO

global priority
global def_priority
global speed

priority = 0
def_priority = 0
speed = 0.5
Actuator.init()

def ini():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    GPIO.setup(35,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    grade_left_stat = GPIO.input(35)
    grade_right_stat = GPIO.input(36)
    
    GPIO.add_event_detect(31, GPIO.RISING, bouncetime = 300)
    GPIO.add_event_callback(31, ISR_speed_up)
    
    GPIO.add_event_detect(32, GPIO.RISING, bouncetime = 300)
    GPIO.add_event_callback(32, ISR_speed_down)
    
    GPIO.add_event_detect(36, GPIO.RISING, bouncetime = 1000)
    GPIO.add_event_callback(36, ISR_grade_2)
    
    GPIO.add_event_detect(35, GPIO.RISING, bouncetime = 1000)
    GPIO.add_event_callback(35, ISR_grade_1)
    
    
    if(grade_left_stat and grade_right_stat):
        print("Error in grade switch....")
        print("Exiting....")
        exit(0)
    elif(grade_left_stat):
        set_priority(1)
        print("Grade 1")
    else:
        set_priority(2)
        print("Grade 2")
        
def ISR_grade_1(self):
    print("Switching to Grade 1")
    set_priority(1)
    
def ISR_grade_2(self):
    print("Switching to Grade 2")
    set_priority(2)
    
def ISR_speed_up(self):
     print("Increasing Speed...")
     set_speed(1)
     i=0
     while(not GPIO.input(31)):
        i+=1
     
def ISR_speed_down(self):
     print("Decreasing speed..")
     set_speed(0)
     i=0
     while(not GPIO.input(32)):
        i+=1

def set_speed(opr):
    global speed
    if(opr==1):
         speed+=0.1
         if(speed>=1):
             speed=1
    else:
         speed-=0.1
         if(speed<=0):
             speed=0
    print("Current speed is : "+str(speed))

def set_priority(val):#
    global priority
    global def_priority
    priority = val
    def_priority = val

"""
    This function prints the converted braille on the screen.
"""
def print_braille(braille):
    #print(braille)
    _len=len(braille)
    for i in range(0,3):
        m=""
        for x in braille:
            m+=str(x[i])+str(x[i+3])
            m+=" "
        print(m)

def get_braille(text):
    global priority
    global def_priority
    global speed
    
    if(priority==2):
        print("Decoding as per grade 2")
        braille=GD2.braille.process_word(text)
        if(braille==1):
            priority=1
    if(priority==1):
        print("Decoding as per grade 1")
        braille=GD1.braille.encode_braille(text)
    print("Given word: " + text)
    print("Braille converted text: ")
    print_braille(braille)
    for i in braille:
        Actuator.actuate(i)
        sleep(speed)
        Actuator.set_all_low()
        sleep(0.4*speed)
    print(" ")
    priority = def_priority

def clean():
    GPIO.cleanup()
ini()
"""
if __name__ == '__main__':
    ocr="'INSTRUCTIONS TO THE CANDIDATES\n\nDo not write your name anywhere in the answer book.\nBorrowing or lending of calculator, data book, etc. , will not be allowed.\n\nData books and tables which are permitted in the examination hall for reference\nshould be free from handwritten and unauthorized additions.\n\nDo not write on the question paper.\n\nRough works should be done only on the sheet provided at the end of the\n\nanswer booklet.\n\nUse both sides of the paper for answering questions.\n\nAnswers must be legibly written with blue or black ink pens only.\n\nThe answer book contains sufficient pages and no additional sheet will be given.\nMobile Phones, programmable calculators are not allowed inside the examination hall.\nMobile phones possessed by students inside the examination hall will be confiscated\nand shall not be retumed to students.\n\nStudy materials, memory aids, copies of notes or pages of books are not allowed\ninside the examination hall.\n\nStrict silence is expected inside the examination halls.\nCopying or any other malpractice may attract stringent penal'"
    ocr_=""
    for i in ocr:
        if i=='\n':
            i=" "
        ocr_+=i
    ocr_=ocr_[1:len(ocr_)-1]
    new_word=""
    for j in range(0,len(ocr_)):
        i=ocr_[j]
        if(j==len(ocr_)-1):
            #print(new_word)
            get_braille(new_word)
            new_word=""
        if(i.isalpha() or i in string.punctuation):
            new_word+=i
        elif(len(new_word)!=0):
            #print(new_word)
            get_braille(new_word)
            new_word=""
        else:
            new_word=""
        sleep(0.1)
"""   
        
        
