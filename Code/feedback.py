# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

pin =40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin,GPIO.OUT, initial = GPIO.LOW)

def start():
    for i in range(0,3):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.2)

def image_error():
    for i in range(0,5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        
def camera_error():
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(0.5)

def camera_start():
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(pin,GPIO.LOW)

def clean():
    GPIO.cleanup()
    