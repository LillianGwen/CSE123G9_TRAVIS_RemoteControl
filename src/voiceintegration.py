#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/10/2022

#This file handles the voice integrated functions in TRAVIS
#notably handling audio input processing, speech processing,
#and command integration

#TODO:
#single always used microphone instance
#set up mic instance to use exact mic
#set up mic instance with https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancedynamic_energy_threshold--true---type-bool
#set up mic instance with https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#recognizer_instancelisten_in_backgroundsource-audiosource-callback-callablerecognizer-audiodata-any---callablebool-none
#make separate regex thing for travis voice commands

#code modified from geeks4geeks
#https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

#used for speech to text
import speech_recognition as sr

#used for text to speech
#https://pyttsx3.readthedocs.io/en/latest/engine.html
import pyttsx3

#used for organizing speech recognition styles for cleaner code
import enum

#enum class for voice engine used -
#sphinx is default
class AudioRecognitionStyle(enum):
	#sphinx is less accurate and more power-intensive
	#but does not require any wireless connection
	SPHINX = "Sphinx"
	
	#google is more accurate and should require less computation
	#but requires an internet connection
	GOOGLE = "Google"

#variable to track current recognition style
ARStyle = AudioRecognitionStyle.SPHINX

#function to set recognition style
def SetARStyle(style:AudioRecognitionStyle):
	global ARStyle
	ARStyle = style

# Initialize the recognizer
recognizer = sr.Recognizer()

#text to speech 
def SpeakText(command):
	
	#init tts engine
	#use espeak driver for generic platform usage
	#AKA useage on a Raspberry Pi
	#Second flag is to disable debug output
	engine = pyttsx3.init("espeak", False)

	#Queue engine to speak command through driver
	engine.say(command)

	#Run command through queue
	engine.runAndWait()
	
	
#command to record audio input 
#intended to be run in an infinite loop
def RecordAudio() -> str:
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as mic:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			
			#listens for the user's input
			audio_input = recognizer.listen(mic)
			
			#match current audio recognition style to choose which way to match
			if(ARStyle == AudioRecognitionStyle.SPHINX):
				recognized_audio = recognizer.recognize_sphinx(audio_input)
			elif(ARStyle == AudioRecognitionStyle.GOOGLE):
				recognized_audio = recognizer.recognize_google(audio_input)
			else:
				#error
				return
			
			#make audio text into lowercase
			recognized_audio = recognized_audio.lower()

			#return recognized audio
			return recognized_audio
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	#error generally occurs when no words detected
	except sr.UnknownValueError:
		print("unknown error occured")
