#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/17/2022

#This file handles the voice integrated functions in TRAVIS
#notably handling command integration

import audioprocessing as ap
import televisioncommunication as tvcomm
import re


def ProcessAudio():	
	recorded_text = ap.RecordAudio()
	
	#STEPS
	#detect if the word TRAVIS is said
	#if not detected, return and do nothing
	#if detected, detect if any commands are issued
	#if no commands issued, speak warning that detected TRAVIS but not any commands
	#if command issued, detect command arguments (name/number of show/channel)
	#once done, send proper lirc command and speak heard command
	
	# Patterns w/ regex to compare string to
	pattern_change = '^(Travis ch[a-zA-Z]+) ((ch[a-zA-Z]+ (to )?([0-9]{1,4}|.+))|(s[a-zA-Z]+))$'
	pattern_power = '^Travis p[a-zA-Z]+ (on|off)$'
	pattern_mute = '^Travis m[a-zA-Z]+$'
	pattern_adjust = '^Travis (v[a-zA-Z]+|ch[a-zA-Z]+) (in[a-zA-Z]+|de[a-zA-Z]+|up|down|higher|lower)$'
	pattern_assign = '^(Travis a[a-zA-Z]+) (.+?(?=[0-9]{1,4}|to))(to )?[0-9]{1,4}$'
	
	# Results of the regex
	result_change = re.match(pattern_change, recorded_text)
	result_power = re.match(pattern_power, recorded_text)
	result_mute = re.match(pattern_mute, recorded_text)
	result_adjust = re.match(pattern_adjust, recorded_text)
	result_assign = re.match(pattern_assign, recorded_text)
	
	# Check for which command is triggered, if any
	if result_change:
		print("Change success!")
	elif result_power:
		print("Power success!")
	elif result_mute:
		print("Mute success!")
	elif result_adjust:
		print("Adjust success!")
	elif result_assign:
		print("Assign success!")
	else:
		print("Failure.")
	
	return

