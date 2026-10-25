import pyaudio
import time
import sys
import datetime
import socket
import pygame

pygame.init()
pygame.joystick.init()
event = pygame.event.get()
joystick = pygame.joystick.Joystick(0)
joystick.init()
pygame.display.set_mode((1,1))

R1 = 5

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.168.1.181', 12345))

print(f"Joystick name: {joystick.get_name()}")
print("Ready for input:")



while True:

	Xaxis = joystick.get_axis(0)
	Yaxis = joystick.get_axis(1)

	if Yaxis == 1:
		print("forward")
		input = "forward"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif Xaxis == -1:
		print("a - turn left")
		input = "turn left"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif Xaxis == 1:
		print("d - turn right")
		input = "turn right"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif Yaxis == -1:
		print("s - backward")
		input = "backward"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif joystick.get_button(R1):
		print("exit")
		sys.exit()
	else:
		input = "nothing"
		client_socket.sendall(input.encode())
		









