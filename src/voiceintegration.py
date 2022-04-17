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
##if (1):
	recorded_text = ap.RecordAudio()
	
	#STEPS
	#detect if the word TRAVIS is said
	#if not detected, return and do nothing
	#if detected, detect if any commands are issued
	#if no commands issued, speak warning that detected TRAVIS but not any commands
	#if command issued, detect command arguments (name/number of show/channel)
	#once done, send proper lirc command and speak heard command
	
	# TEST CODE
	##recorded_text = "Travis chhhhhhhhhhhhhhhhhhhhhhhhh down"
	
	# Check for which command is triggered, if any
	split_text = recorded_text.split()
	# Check for 'Travis change...'
	if re.match('^(Travis ch[a-zA-Z]+) ((ch[a-zA-Z]+ (to )?([0-9]{1,4}|.+))|(s[a-zA-Z]+))$', recorded_text):
		print("Change success!")
		# Check for 'channel'
		if re.match('^ch[a-zA-Z]+$', split_text[2]):
			# Check for 'to' to determine which word is the channel number
			if split_text[3] == 'to':
				print("Changing channel to "+split_text[4])
			else:
				print("Changing channel to "+split_text[3])
		elif re.match('^s[a-zA-Z]+$', split_text[2]):
			print("Changing source")
		else:
			print("Regex Error!")
	
	# Check for 'Travis power...'
	elif re.match('^Travis p[a-zA-Z]+$', recorded_text):
		print("Power success!")
		print("Activating power button")
	
	# Check for 'Travis mute'
	elif re.match('^Travis m[a-zA-Z]+$', recorded_text):
		print("Mute success!")
		print("Activating mute button")
	
	# Check for 'Travis volume|channel...'
	elif re.match('^Travis (v[a-zA-Z]+|ch[a-zA-Z]+) (in[a-zA-Z]+|de[a-zA-Z]+|up|down|higher|lower)$', recorded_text):
		print("Adjust success!")
		# Check for 'volume'
		if re.match('^v[a-zA-Z]+$', split_text[1]):
			# Check for anything relating to going up
			if (re.match('^in[a-zA-Z]+$', split_text[2]) or (split_text[2] == 'up') or (split_text[2] == 'higher')):
				print("Volume adjusted up by 1")
			# Check for anything relating to going down
			elif (re.match('^de[a-zA-Z]+$', split_text[2]) or (split_text[2] == 'down') or (split_text[2] == 'lower')):
				print("Volume adjusted down by 1")
			else:
				print("Regex Error!")
		# Check for 'channel'
		elif re.match('^ch[a-zA-Z]+$', split_text[1]):
			# Check for anything relating to going up
			if (re.match('^in[a-zA-Z]+$', split_text[2]) or (split_text[2] == 'up') or (split_text[2] == 'higher')):
				print("Channel adjusted up by 1")
			# Check for anything relating to going down
			elif (re.match('^de[a-zA-Z]+$', split_text[2]) or (split_text[2] == 'down') or (split_text[2] == 'lower')):
				print("Channel adjusted down by 1")
			else:
				print("Regex Error!")
		else:
			print("Regex Error!")
	
	# Check for 'Travis assign...' (this one's annoying)
	elif re.match('^(Travis a[a-zA-Z]+) (.+?(?=[0-9]{1,4}|to))(to )?[0-9]{1,4}$', recorded_text):
		print("Assign success!")
	else:
		print("Failure.")
	
	return

