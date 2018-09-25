# External module imports
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import time
from numpy import array
from PIL import Image
GPIO.cleanup()
DS=21
STCP=20
SHCP=16


# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(DS, GPIO.OUT) 
GPIO.setup(STCP, GPIO.OUT) 
GPIO.setup(SHCP, GPIO.OUT) 


# Initial state :
GPIO.output(DS, GPIO.LOW)
GPIO.output(STCP, GPIO.LOW)
GPIO.output(SHCP, GPIO.LOW)

SHCPS=0
DSI=[0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
try:
    while(True):
        if(SHCPS==0):
            SHCPS=1
            GPIO.output(STCP, GPIO.LOW)
            GPIO.output(SHCP, GPIO.HIGH)
            if(DSI[i]==0):
                GPIO.output(DS, GPIO.LOW)
            else:
                GPIO.output(DS, GPIO.HIGH)
            i=i+1
            if(i==10):
                i=0
        else:
            SHCPS=0
            GPIO.output(STCP, GPIO.HIGH)
            GPIO.output(SHCP, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: # IF CTRL+C is pressed, exit cleany:
    GPIO.cleanup()
