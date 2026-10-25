import keyboard
import sys


while True:
	if keyboard.is_pressed("w"):
		print("W is being pressed")
	if keyboard.is_pressed("x"):
		sys.exit()