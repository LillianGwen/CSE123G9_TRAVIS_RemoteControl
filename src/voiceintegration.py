#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/12/2022

#This file handles the voice integrated functions in TRAVIS
#notably handling command integration

import audioprocessing as ap
import televisioncommunication as tvcomm

#TODO:
#make separate regex thing for travis voice commands

def ProcessAudio():
	
	recorded_text = ap.RecordAudio()

	#STEPS
	#detect if the word TRAVIS is said
	#if not detected, return and do nothing
	#if detected, detect if any commands are issued
	#if no commands issued, speak warning that detected TRAVIS but not any commands
	#if command issued, detect command arguments (name/number of show/channel)
	#once done, send proper lirc command and speak heard command

	return

