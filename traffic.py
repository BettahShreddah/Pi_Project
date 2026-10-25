#Create traffic light kidna i guess???

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def red_light():

	#Red is connected to GPIO 22
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(22, GPIO.HIGH)

	time.sleep(5)

	GPIO.output(22, GPIO.LOW)

#	GPIO.cleanup(22)

def yellow_light():

	#Yellow  is connected to GPIO 27
	GPIO.setup(27, GPIO.OUT)
	GPIO.output(27, GPIO.HIGH)

	time.sleep(5)

	GPIO.output(27, GPIO.LOW)

#	GPIO.cleanup(27)

def green_light():

	#Green is connected to GPIO 17
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, GPIO.HIGH)

	time.sleep(5)

	GPIO.output(17, GPIO.LOW)


def traffic_light(): 
	green_light()
#	time.sleep(2)
	yellow_light()
#	time.sleep(2)
	red_light()
#	time.sleep(2)
	print("traffic operation successful")





