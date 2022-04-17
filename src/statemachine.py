#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/16/2022

#This file handles the state machine of TRAVIS

#TODO:
#create file to read from to bypass INIT state
#fill out INIT state
#track voice command in active state

#used for Raspberry Pi integration
import RPi.GPIO as GPIO

#used for GPIO setup and assorted general constants
import constants as constants

#used for communication with the associated television via IR
import televisioncommunication as TVCOMM

#used for voice command handling
import voiceintegration as voice

#enum for state
currState = constants.TRAVIS_STATE.INIT

#error state, should never be entered
def RunState_ERROR():
	return

#state used upon fresh start to gather remote data
#can be entered by asking TRAVIS to be reinitialized
#but otherwise bypassed after first startup
def RunState_INIT():
	#ignore state for right now, focus on later
	global currState

	#when init finished:
	#add event detection and callbacks for all button events
	#events have a bounce-ignoring duration of constants.GPIO_BUTTON_EVENT_BOUNCETIME
	GPIO.add_event_detect(constants.GPIO_BTN_POWER, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_INPUT, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_VOL_UP, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_VOL_DOWN, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_MUTE, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_CH_UP, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)
	GPIO.add_event_detect(constants.GPIO_BTN_CH_DOWN, GPIO.RISING, callback = TVCOMM.ButtonCallback, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)

	#no callback for travis button event
	#as it does not correspond to any tv feature
	#and instead is state-dependent
	GPIO.add_event_detect(constants.GPIO_BTN_TRAVIS, GPIO.RISING, bouncetime = constants.GPIO_BUTTON_EVENT_BOUNCETIME)

	#setup TRAVIS microphone status as active, and enable the associated status LED
	GPIO.output(constants.GPIO_LED, GPIO.HIGH)
	currState = constants.TRAVIS_STATE.ACTIVE
	return

#state used when TRAVIS is not listening via voice
#only handles button input
def RunState_IDLE():
	global currState

	#idle and handle already initialized events

	#if travis button is reenabled then handle that as well
	#and as such, move to active state
	if(GPIO.event_detected(constants.GPIO_BTN_TRAVIS)):
		#setup TRAVIS microphone status as active, and enable the associated status LED
		GPIO.output(constants.GPIO_LED, GPIO.HIGH)
		currState = constants.TRAVIS_STATE.ACTIVE
	
	return

#state used when TRAVIS is listening via voice and button input
def RunState_ACTIVE():

	global currState

	#handle already initialized events

	#handle voice commands TODO
	voice.ProcessAudio()

	#if voice command is to reinitialize then move back to init state

	#if travis button is disabled then handle that as well
	#and as such, move to idle state
	if(GPIO.event_detected(constants.GPIO_BTN_TRAVIS)):
		#setup TRAVIS microphone status as active, and enable the associated status LED
		GPIO.output(constants.GPIO_LED, GPIO.LOW)
		currState = constants.TRAVIS_STATE.IDLE
	
	return

#python doesnt have built in switch case statements
#so instead we switch with a dictionary of functions
TRAVIS_SM = {
	constants.TRAVIS_STATE.ERROR: RunState_ERROR,
	constants.TRAVIS_STATE.INIT: RunState_INIT,
	constants.TRAVIS_STATE.IDLE: RunState_IDLE,
	constants.TRAVIS_STATE.ACTIVE: RunState_ACTIVE,
}
