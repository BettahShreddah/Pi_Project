# USED FOR REMOTE KEYBOARD INPUTS FROM PI

import pygame
import socket
from adafruit_motorkit import MotorKit


HOST = ''
PORT = 12345

MK = MotorKit()

# Motor 3 is LEFT wheel

# Motor 4 is RIGHT wheel

def no_motor():
	MK.motor3.throttle = 0
	MK.motor4.throttle = 0





with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print(f"Listening on port {PORT}")

	conn, addr = s.accept()

with conn:

	while True:

		command = conn.recv(1024).decode()

		if not command:
			print("No client recieved")
			break


		input = command.lower()


		try:
			if input == "forward":

				print("Moving Forwards")
				MK.motor3.throttle  = 0.8
				MK.motor4.throttle  = 0.8
			elif input == "backward":

				print("Moving Backwards")
				MK.motor3.throttle  = -0.8
				MK.motor4.throttle  = -0.8
			elif input == "turn right":
				print("turning right")
				MK.motor3.throttle = 0.4
				MK.motor4.throttle = 0.8
			elif input == "turn left":
				print("turning left")
				MK.motor3.throttle  = 0.8
				MK.motor4.throttle  = 0.4

			elif input == "nothing":
				no_motor()
			else:
				no_motor()
		except:
			print("No input currently")

