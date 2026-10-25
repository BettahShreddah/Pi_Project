import socket
import traffic
import os
import re
from word2number import w2n

# Motor Movement
def move_motor(dist_int):
	travel = dist_int/3
	kit.motor4.throttle=1.0
	kit.motor3.throttle=1.0
	time.sleep(travel)
	kit.motor4.throttle=0
	kit.motor3.throttle=0


# Motor Controller
from  adafruit_motorkit import MotorKit
kit = MotorKit()

# GPIO

import RPi.GPIO as GPIO
import time

# Set GPIO Mode (in this case the Board)
GPIO.setmode(GPIO.BCM)

"""
# Sets 27 as input
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
"""

HOST = '' #Listens to all interfaces
PORT = 13254 # Port (Must be above 1024)



#Creates socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT)) #Binds socket to specific  IP
	s.listen() #Tells the socket to listen for connections
	print(f"Listening on port {PORT}...")

	conn, addr = s.accept() #waits until client connects to socket

# conn = a new socket
# addr = client IP address and port






with conn:


# Works for Voice Inputs:
	
	while True:

		data = conn.recv(1024).decode()


		if not data:
			print("No client")
			break

		print("Received:", data)

	
		
	#	match = re.search(r"move forward (\d+)", data.lower())

		if "shut" in data.lower():
			os.system("sudo shutdown -h now")


		else:
			word  = data.split()
			if len(word) < 3:
				print("no distance")

			elif  word[2].isdigit():
				dist_int = int(word[2])
				move_motor(dist_int)

			else:
				
				try:
					dist_str  = w2n.word_to_num(word[2])
					print(f"{dist_str}")
					dist_int = int(dist_str)
					move_motor(dist_int)
				except:
					print("no distance")





		response = f"Server Received: {data}"
		conn.sendall(response.encode())


