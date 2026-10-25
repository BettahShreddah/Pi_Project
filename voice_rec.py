import time
import pyaudio
import speech_recognition as sr
import datetime
import sys

from word2number import w2n



# Get Current time
local_time = datetime.datetime.now()


# Set up for recognizer (Enabling)
recognizer = sr.Recognizer()



# Set up calculator


def calc_run():


	def addition(x,y):

		number = x + y
		return number

	def subtraction (x,y):

		number = x - y
		return number

	def multiplication(x,y):

		number = x * y
		return number

	def division(x,y):

		if y == 0:
			print("Invalid command")
		else:
			number = x / y
			return number


	with sr.Microphone() as source:

		print("Number X:")

		recognizer.adjust_for_ambient_noise(source)
		speechX = recognizer.listen(source)

	x  =	w2n.word_to_num(speechX)






#	if speechX:
#		x = int(speechX)


	time.sleep(5)

	with sr.Microphone() as source:

		print("Number Y:")

		recognizer.adjust_for_ambient_noise(source)
		speechY  = recognizer.listen(source)

	y  =	w2n.word_to_num(speechY)

#	speechY  = recognizer.recognize_google(audio).lower() #Convert to lowercase"


#	if speechY.isdigit():
#		y = int(phrase)

	with sr.Microphone() as source:

		print("Operation:")

		recognizer.adjust_for_ambient_noise(source)
		speechOP = recognizer.listen(source)

#	speechOP  = recognizer.recognize_google(audio).lower() #Convert to lowercase


	if "addition" in speechOP:
		addition(x,y)
	if "substraction" in speechOP:
		subtraction(x,y)
	if "multiplication" in speechOP:
		multiplication(x,y)
	if "division" in speechOP:
		division(x,y)











def recognize_phrase():

	with sr.Microphone() as source:
		print ("Please say something...")
		# Adjust for ambient noise
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)


	phrase = recognizer.recognize_google(audio).lower() #Convert to lowercase

	# Recognize speech
	try:
		print("You said: " + recognizer.recognize_google(audio))
	except sr.UnknownValueError:
		print("Sorry, I could not understand the audio.")
	except sr.RequestError as e:
		print("Sorry, there was an issue with the speech recognition service:{e}")


	# Check for specific phrases

	if "what time is it" in phrase:
		print(local_time)

	if "come here" in phrase:
		print("Coming!")

	if "set speed 25" in phrase:
		print("Speed is set at 25")

	if "how are you" in phrase:
		print("I'm good, how are you?")

	if "stop" in phrase:
		print("Goodbye")
		sys.exit()

	if "calculator" in phrase:
		calc_run()






	# Pauses program for certain amount of time
	time.sleep(3)

	print("Press Enter to continue")
	input()



while True:
	recognize_phrase()

