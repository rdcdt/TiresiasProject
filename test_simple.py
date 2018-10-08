# coding=utf-8
 
import RPi.GPIO as GPIO
import datetime


cmd_pin = 4 
#or 7

def config(): 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(cmd_pin, GPIO.OUT)
	

def main() : 
	config()
	GPIO.output(cmd_pin, GPIO.HIGH)
	return 0


if __name__ == "__name__" :
	main() 
 




