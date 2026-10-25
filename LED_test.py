import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(17, GPIO.HIGH)
print("it did somthin")
time.sleep(4)
print("it slept")
GPIO.output(17, GPIO.LOW)
print("it turned off")
time.sleep(4)

GPIO.cleanup()
