# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
def now():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    GPIO.cleanup()
    
def welcome_screen():
    print("\nInitiallising.......")
    print("==================================================================================================================")
    sleep(0.1)
    print(" _____   ____  _____ _______       ____  _      ______         ____  _____            _____ _      _      ______  ")
    sleep(0.1)
    print("|  __ \ / __ \|  __ \__   __|/\   |  _ \| |    |  ____|       |  _ \|  __ \     /\   |_   _| |    | |    |  ____| ")
    sleep(0.1)
    print("| |__) | |  | | |__) | | |  /  \  | |_) | |    | |__          | |_) | |__) |   /  \    | | | |    | |    | |__    ")
    sleep(0.1)
    print("|  ___/| |  | |  _  /  | | / /\ \ |  _ <| |    |  __|         |  _ <|  _  /   / /\ \   | | | |    | |    |  __|   ")
    sleep(0.1)
    print("| |    | |__| | | \ \  | |/ ____ \| |_) | |____| |____        | |_) | | \ \  / ____ \ _| |_| |____| |____| |____  ") 
    sleep(0.1)
    print("|_|     \____/|_|  \_\ |_/_/    \_\____/|______|______|       |____/|_|  \_\/_/    \_\_____|______|______|______| ")
    sleep(0.1)
    print("")
    print("==================================================================================================================")
    sleep(0.1)
                                                                                                                  
                                                                                                                  