#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/10/2022

#This file handles constant values used in TRAVIS

#used for Raspberry Pi integration
import RPi.GPIO as GPIO

#find gpio mode
gpioMode = GPIO.getmode()

#if gpio mode is unset, set it to board
if(gpioMode == GPIO.UNSET):
	GPIO.setmode(GPIO.BOARD)

#if gpio mode is using board numbering
#assign pins based on that numbering
if(gpioMode == GPIO.BOARD):

	#BOARD STYLE (using pin nums from board)
	GPIO_BUTTON_CH = [
		#CHANNELS
	]

#otherwise, gpio mode has been set to use GPIO numbering
#as provided by the manufacturer
#due to some import preset that cannot be overridden
else:
	
	#GPIO STYLE (using GPIO/BCM numbering)
	GPIO_BUTTON_CH = [
		#CHANNELS
	]

#initializing motor interaction channels
#channels driven by saying
#GPIO.output(channel, GPIO.LOW/GPIO.HIGH)
#0, 1, True, False can also be used

#setup list of channels to outputs w no pullup/pulldown
#initialized to produce GPIO.LOW voltage

# Channel Setup
GPIO.setup(channel = GPIO_BUTTON_CH,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_OFF,
			initial = GPIO.LOW)

