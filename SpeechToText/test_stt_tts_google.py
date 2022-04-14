# Python program to translate
# speech to text and text to speech
# All code property of Geeks4Geeks
# https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init("sapi5", True) # Modified from Geeks4Geeks
	engine.say(command)
	engine.runAndWait()
	

# Print to show the program is running
print('Now running Google variant of Speech-to-Text testing protocol...\n');
	
# Loop infinitely for user to
# speak

while(1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
