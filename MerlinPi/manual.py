#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import time
import datetime
import sys, os


def clear():
    os.system("rm -v /home/pi/Downloads/*")

# Generate timestamp string generating name for photos
def timestamp():
    tstring = datetime.datetime.now()
    #print("Filename generated ...")
    return tstring.strftime("%Y%m%d_%H%M%S")
  
def stillimage():
    
    print("Raspistill starts")
    os.system("raspistill -o /home/pi/Downloads/" +str(capture_number) + "cam.jpg")
    print("done")

def videoclip():
    
    print("Raspivid starts")
    os.system("raspivid -t 15000 -o /home/pi/Downloads/" +str(capture_number) + "vid.h264")
    print("done")

capture_number = timestamp()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Receiver Switch

running = True

while running:
    
    if (GPIO.input(10) ==0):
        capture_number = timestamp()
        print ("Button 10")
        stillimage()
        time.sleep(1)

    elif (GPIO.input(11) ==0):
        capture_number = timestamp()
        print ("Button 11")
        videoclip()
        time.sleep(1)

    else:

        time.sleep(0.1)
    