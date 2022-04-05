#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#03/16/2022

#This file handles the initialization of TRAVIS

#time used for delaying current thread to create sampling interval
from time import sleep
#sys used for exiting and throwing errors
from sys import exit
#traceback used to print the current traceback when any exception happens
from traceback import print_exc

#used for RPI GPIO pins
import RPi.GPIO as GPIO

import constants as constants
import statemachine as SM

try:
	#task loop
	#runs state machine every tick
	while True:
		#task loop
		#runs state machine every tick
		SM.RP_SM[SM.currState]()
		sleep(constants.SAMPLE_INTERVAL)

#happens if interrupted by ctrl c on terminal
except KeyboardInterrupt:
	#prints the exception and stack
	print("exited by ctrl c keyboard interrupt exception")
	print_exc()

#happens if any other error occurs
except:
	#prints the exception and stack
	print("exited by non keyboard exception")
	print_exc()

#happens if exception occurs or main somehow finishes
finally:
	#resets used gpio pins
	GPIO.cleanup()
	#empty means exit success / return 0
	exit()