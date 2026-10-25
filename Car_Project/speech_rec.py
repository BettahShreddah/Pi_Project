import pyaudio
import time
import sys
import datetime
import speech_recognition as sr
import socket

# Initialize recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)  # Replace 1 with your desired index
# Set which microphone to use


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('192.168.1.181', 13254))

while True:

	# Use the microphone as source
	with mic as source:
		print("Say something...")
		audio = recognizer.listen(source)

		try:
			text = recognizer.recognize_google(audio)
			print("You said:", text)
		except sr.UnknownValueError:
			print("Could not understand audio")
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))


	# Send the message
	client_socket.sendall(text.encode())





