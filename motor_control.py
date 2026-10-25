from adafruit_motorkit import MotorKit
import time


print("i am running")
# Create Motorkit Instance
kit = MotorKit(0x60)


kit.motor4.throttle = 1.0
time.sleep(5)
kit.motor4.throttle = 0
print("done")



"""
# Run motor 4 at 80% speed for 2 seconds
kit.motor4.throttle = 0.8
print("motor speed is fine")
time.sleep(2)

#Stop motor
kit.motor4.throttle = 0
print("stopped motor")
#Reverse motor at 80% speed for 2 seconds
kit.motor4.throttle = -0.8
time.sleep(2)

#Stop motor
kit.motor4.throttle = 0
"""
