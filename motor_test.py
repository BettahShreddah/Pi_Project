from adafruit_motorkit import MotorKit
import time

MK = MotorKit()

MK.motor3.throttle = 1
MK.motor4.throttle = 1

time.sleep(5)

MK.motor3.throttle = -1
MK.motor4.throttle = -1

time.sleep(5)

MK.motor3.throttle = 0.5
MK.motor4.throttle = 1

time.sleep(5)

MK.motor3.throttle = 1
MK.motor4.throttle = 0.5

time.sleep(5)

MK.motor3.throttle = 0
MK.motor4.throttle = 0
