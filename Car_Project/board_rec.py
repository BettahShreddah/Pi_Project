import pyaudio
import time
import sys
import datetime
import socket
import keyboard




# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.168.1.181', 12345))

print("Ready for input:")
while True:
	
	if keyboard.is_pressed("w"):
		print("w - forward")
		input = "forward"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif keyboard.is_pressed("a"):
		print("a - turn left")
		input = "turn left"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif keyboard.is_pressed("d"):
		print("d - turn right")
		input = "turn right"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif keyboard.is_pressed("s"):
		print("s - backward")
		input = "backward"
		time.sleep(0.1)
		client_socket.sendall(input.encode())
	elif keyboard.is_pressed("x"):
		print("exit")
		sys.exit()
	else:
		input = "nothing"
		client_socket.sendall(input.encode())
		









