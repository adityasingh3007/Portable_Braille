# -*- coding: utf-8 -*-
"""
**************************************************************************************
*                              Actuator
*                           =============
*  This software is intended to convert english text into braille characters
*  MODULE: Actuator
*  Filename: Actuator.py
*  Version: 1.0.0  
*  Date: February 9, 2019
*  
*  Author: Aditya Kumar Singh
*  Team Name: Victorious Visionaries
*  Team Members: Aditya Kumar Singh, Raj Kumar Bhagat,
*                Ruphan S, Yash Patel
***************************************************************************************
"""

from time import sleep
import RPi.GPIO as GPIO

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    set_all_low()
    
def set_all_low():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    
def get_pin_number(pin):
    str_= -1
    # 12 11 13 15 16 18
    if(pin==0):
        str_=16
    elif(pin==1):
        str_=18
    elif(pin==2):
        str_=12
    elif(pin==3):
        str_=15
    elif(pin==4):
        str_=11
    elif(pin==5):
        str_=13
    return str_

def set_port_pin(pin,value):
    ret=get_pin_number(pin)
    if(value):
        #HIGH
        GPIO.output(ret, GPIO.HIGH)
    else:
        GPIO.output(ret, GPIO.LOW)
        #LOW
    
def actuate(brl):
    index=0
    for i in brl:
        set_port_pin(index,i)
        index+=1

def clean():
    GPIO.cleanup()
    
init()