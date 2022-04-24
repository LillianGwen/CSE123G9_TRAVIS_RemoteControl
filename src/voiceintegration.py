#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/23/2022

#This file handles the voice integrated functions in TRAVIS
#notably handling command integration

import audioprocessing as ap
import televisioncommunication as tvcomm

#used for handling regex to match detected audio strings to commands
import re

#constant used for seeking the end of a file to append with
from io import SEEK_END

#constant channel registry file name
CHANNEL_REGISTRY_FILE_NAME = "TRAVIS_CHANNEL_REGISTRY.txt"

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
	#split up to a maximum of four times to not mess up channel names
	split_text = recorded_text.split(" ", 4)
	split_len = len(split_text)

	# Check for 'Travis change...'
	if re.match('^(Travis ch[a-zA-Z]+) ((ch[a-zA-Z]+ (to )?([0-9]{1,4}|.+))|((s[a-zA-Z]+)|(in[a-zA-Z]+)|(win[a-zA-Z]+)))$', recorded_text):
		
		# Check for 'channel'
		if re.match('^ch[a-zA-Z]+$', split_text[2]):

			# Check for 'to' to determine which word is the channel number
			#also check length first to avoid index out of bounds errors/segfaults
			if((split_len >= 4) and (split_text[3] == 'to')):

				#if theres 5 (max) splits that means the last piece is
				#either a channel name or a sequence of numbers
				if(split_len == 5):
					channel = split_text[4]
				
				else:
					#if theres no additional sequence past to,
					#assume they meant to say travis change channel 2
					channel = 2

			else:
				#resplit to capture possibilty of a channel name
				#by splitting of one size smaller
				split_text = recorded_text.split(" ", 3)

				#last piece is either a channel name or a sequence of numbers
				channel = split_text[3]
			
			#now that we have the channel,
			#find if its a name or number

			#if its a number, send the number out to the tv,
			#speak the response, and return
			if(channel.isnumeric()):

				tvcomm.sendnums(channel)

				#speak response to heard command
				ap.SpeakText("Changing television channel to channel %d." % (channel))
				return

			#if its a name, find the associated number
			#and then send out the number to the tv,
			#speak the response, and return
			else:
				#search for the name's channel entry
				channel_num = findChannelEntry(channel)

				#if the name is not registered to any number, throw an error
				if(channel_num == -1):
					#speak error response
					ap.SpeakText("Sorry, I do not have any channel number associated with %s, try asking me to assign it to one." % (channel))
					return
				
				#otherwise, send the number out to the tv,
				#speak the response, and return
				tvcomm.sendnums(channel_num)

				#speak response to heard command
				ap.SpeakText("Changing television channel to %s on channel %d." % (channel, channel_num))
				return
		
		#check for 'source' or 'input' or 'window'
		elif re.match('^(s[a-zA-Z]+)|(in[a-zA-Z]+)|(win[a-zA-Z]+)$', split_text[2]):
			#send source/input/cyclewindows signal to the tv
			tvcomm.send(tvcomm.RemoteInput.CYCLEWINDOWS)

			#speak response to heard command
			ap.SpeakText("Changing television input.")
		
		#no modifier heard, only travis change, so throw error
		else:
			#speak error response
			ap.SpeakText("Sorry, I only heard change, did you mean to change the channel or television input?")
	
	# Check for 'Travis (turn) power|television...'
	elif re.match('^Travis (turn )?(p[a-zA-Z]+|te[a-zA-Z]+)$', recorded_text):
		#send power signal to the tv
		tvcomm.send(tvcomm.RemoteInput.POWER)

		#speak response to heard command
		ap.SpeakText("Sending television power signal.")

		return
	
	# Check for 'Travis mute'
	elif re.match('^Travis m[a-zA-Z]+$', recorded_text):
		#send mute signal to the tv
		tvcomm.send(tvcomm.RemoteInput.MUTE)

		#speak response to heard command
		ap.SpeakText("Sending television mute signal")

		return
	
	# Check for 'Travis (turn) volume|channel...'
	elif re.match('^Travis (turn )?(v[a-zA-Z]+|ch[a-zA-Z]+) (in[a-zA-Z]+|de[a-zA-Z]+|up|dow[a-zA-Z]+|high[a-zA-Z]+|low[a-zA-Z]+)$', recorded_text):

		#remove 'turn' from split text list if it occurs
		if(split_text[1] == "turn"):
			split_text.pop(1)
		
		# Check for 'volume'
		if re.match('^v[a-zA-Z]+$', split_text[1]):

			# Check for anything relating to going up
			if re.match('^(in[a-zA-Z]+|up|high[a-zA-Z]+)$', split_text[2]):

				#send volume up signal to the tv
				tvcomm.send(tvcomm.RemoteInput.VOLUMEUP)

				#speak response to heard command
				ap.SpeakText("Raising television volume.")
				
				return

			# Check for anything relating to going down
			elif re.match('^(de[a-zA-Z]+|dow[a-zA-Z]+|low[a-zA-Z]+)$', split_text[2]):
				
				#send volume down signal to the tv
				tvcomm.send(tvcomm.RemoteInput.VOLUMEDOWN)

				#speak response to heard command
				ap.SpeakText("Lowering television volume.")

				return
			
			#no modifier heard, speak error
			else:

				#speak error response
				ap.SpeakText("Sorry, I only heard volume, did you mean to turn the volume up or down?")
				return

		# Check for 'channel'
		elif re.match('^ch[a-zA-Z]+$', split_text[1]):

			# Check for anything relating to going up
			if re.match('^(in[a-zA-Z]+|up|high[a-zA-Z]+)$', split_text[2]):

				#send channel up signal to the tv
				tvcomm.send(tvcomm.RemoteInput.CHANNELUP)

				#speak response to heard command
				ap.SpeakText("Incrementing television channel.")
				
				return
				
			# Check for anything relating to going down
			elif re.match('^(de[a-zA-Z]+|dow[a-zA-Z]+|low[a-zA-Z]+)$', split_text[2]):

				#send channel down signal to the tv
				tvcomm.send(tvcomm.RemoteInput.CHANNELDOWN)

				#speak response to heard command
				ap.SpeakText("Decrementing television channel.")

				return

			#no modifier heard, speak error
			else:

				#speak error response
				ap.SpeakText("Sorry, I only heard channel, did you mean to go a channel up or down?")
				return
		
		#no modifier heard, throw error
		else:
			print("Regex Error!")
	
	# Check for 'Travis assign...' (this one's annoying)
	elif re.match('^(Travis a[a-zA-Z]+) (.+?(?=[0-9]{1,4}|to))(to )?[0-9]{1,4}$', recorded_text):

		#split once from the right, separating the number from the rest of the string
		(channel_name, channel_num) = recorded_text.rsplit(" ", 1)

		#if the command was given with a 'to' then remove that
		#by slicing off the last three indeces of the string (space and 'to')
		if(channel_name.endswith(" to")):
			channel_name = channel_name[:-3]
		
		#split off the channel name into travis + a* + actual channel name
		channel_name = channel_name.split(" ", 2)
		#set channel name equal to that third component in the list,
		#aka the actual channel name
		channel_name = channel_name[2]

		#add the channel entry obtained from the above steps into the channel registry
		addChannelEntry(channel_name, channel_num)

		#speak response to heard command
		ap.SpeakText("Assigning %s to channel %d." % (channel_name, channel_num))

		return
	
	#no command heard, ignore
	else:
		pass
	
	return

#add channel entry to the channel registry
#if names match but nums dont, overwrite name
def addChannelEntry(channel_name:str, channel_num:int):

	#bind newentry to avoid computation on possible reuseage
	#because we always write with a \n, it will always be matched
	#as file.readlines() does not truncate off that newline char
	newentry = "%s,%d\n" % (channel_name, channel_num)

	#open file for reading and writing, opens at beginning of file
	#will not create file if it does not already exist,
	#so we need to use a try catch block if it errors because of that
	try:
		channelfile = open(CHANNEL_REGISTRY_FILE_NAME, "r+")
	except FileNotFoundError:
		channelfile = open(CHANNEL_REGISTRY_FILE_NAME, "x")
		channelfile.close()
		channelfile = open(CHANNEL_REGISTRY_FILE_NAME, "r+")

	#memory management can be improved with mmap usage
	#but should not be entirely necessary due to the relatively small file size

	#read entire file line by line
	#https://stackoverflow.com/questions/51741682/find-string-and-replace-line
	entries = channelfile.readlines()

	#search file line by line
	for line in range(len(entries)):

		#if channel name found already, rebind it
		#and by rebind it i mean rewrite the entire file with the line replaced
		if(channel_name in entries[line]):

			#check if we need to rewrite first
			#if the entries match, nothing is necessary
			#so close and return
			if(entries[line] == newentry):
				channelfile.close()
				return
			
			#otherwise, we do need to rewrite the file

			#replace line in buffer
			entries[line] = "%s,%d\n" % (channel_name, channel_num)
		
			#rewrite file to include new information
			channelfile.writelines(entries)

			#close file and return
			channelfile.close()
			return

	#after searching, we can confirm the name is not bound elsewhere
	#so we can safely append the entry, close the file, and return

	#seeking 0 bytes offset from the end of the file
	channelfile.seek(0, SEEK_END)
	
	#append new entry
	channelfile.write(newentry)

	#close file and return
	channelfile.close()
	return

#search for channel entry in the channel registry
#returns -1 if error, otherwise returns channel number associated with entry
def findChannelEntry(channel_name:str) -> int:

	#open file for reading only, opens at beginning of file
	#will not create file if it does not already exist,
	#will just return an error
	try:
		channelfile = open(CHANNEL_REGISTRY_FILE_NAME, "r")
	except FileNotFoundError:
		return -1

	#memory management can be improved with mmap usage
	#but should not be entirely necessary due to the relatively small file size

	#read entire file line by line
	#https://stackoverflow.com/questions/51741682/find-string-and-replace-line
	entries = channelfile.readlines()

	#search file line by line
	for line in range(len(entries)):

		#if channel name is found, return its associated number
		if(channel_name in entries[line]):

			#split entry into name and number
			#name at csv[0] and number at csv[1]
			csv = entries[line].split(",\n")

			#close file and return associated channel number
			channelfile.close()
			return csv[1]

	#close file and return error number to indicate entry not found
	channelfile.close()
	return -1
