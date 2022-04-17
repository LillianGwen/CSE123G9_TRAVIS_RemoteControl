#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/16/2022

#This file handles constant values used in TRAVIS
#mostly used for GPIO integration

#used for Raspberry Pi integration
import RPi.GPIO as GPIO

#enum not strictly required but useful for organization
#used to handle state machine enum
import enum

#find gpio mode
gpioMode = GPIO.getmode()

#if gpio mode is unset, set it to board
if(gpioMode == GPIO.UNSET):
	GPIO.setmode(GPIO.BOARD)

#if gpio mode is using board numbering
#assign pins based on that numbering
if(gpioMode == GPIO.BOARD):

	#BOARD STYLE (using pin nums from board)
	GPIO_BTN_POWER = 15
	GPIO_BTN_INPUT = 13
	GPIO_BTN_VOL_UP = 16
	GPIO_BTN_VOL_DOWN = 18
	GPIO_BTN_MUTE = 22
	GPIO_BTN_CH_UP = 29
	GPIO_BTN_CH_DOWN = 31
	GPIO_BTN_TRAVIS = 37

	#travis status LED
	GPIO_LED = 36

	#other pins used:
	#I2S Mic/Audio Input BCLK = BOARD 8/GPIO 14 (UART TX)
	#I2S Mic/Audio Input DOUT = BOARD 7/GPIO 4 (GPCLK0)
	#I2S Mic/Audio Input LRCL = BOARD 10/GPIO 15 (UART RX)

	#IR LED Input = BOARD 11/GPIO 17

#otherwise, gpio mode has been set to use GPIO numbering
#as provided by the manufacturer
#due to some import preset that cannot be overridden
else:
	
	#GPIO STYLE (using GPIO/BCM numbering)
	GPIO_BTN_POWER = 22
	GPIO_BTN_INPUT = 27
	GPIO_BTN_VOL_UP = 23
	GPIO_BTN_VOL_DOWN = 24
	GPIO_BTN_MUTE = 25
	GPIO_BTN_CH_UP = 5
	GPIO_BTN_CH_DOWN = 6
	GPIO_BTN_TRAVIS = 26

	#travis status LED
	GPIO_LED = 16

	#other pins used:
	#I2S Mic/Audio Input BCLK = BOARD 8/GPIO 14 (UART TX)
	#I2S Mic/Audio Input DOUT = BOARD 7/GPIO 4 (GPCLK0)
	#I2S Mic/Audio Input LRCL = BOARD 10/GPIO 15 (UART RX)

	#IR LED Input = BOARD 11/GPIO 17

#initializing button input channels
#input is gathered with
#GPIO.input(channel)
#and can potentially use edge detection
#as explained here: https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

#button setup -
#all buttons set up as inputs
#with pull up resistors to ensure they are not floating
GPIO.setup(channel = GPIO_BTN_POWER,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_INPUT,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_VOL_UP,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_VOL_DOWN,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_MUTE,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_CH_UP,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_CH_DOWN,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

GPIO.setup(channel = GPIO_BTN_TRAVIS,
			direction = GPIO.IN,
			pull_up_down = GPIO.PUD_UP)

#initializing output pins
#channels driven by saying
#GPIO.output(channel, GPIO.LOW/GPIO.HIGH)
#0, 1, True, False can also be used
GPIO.setup(channel = GPIO_LED,
			direction = GPIO.OUT,
			pull_up_down = GPIO.PUD_OFF,
			initial = GPIO.LOW)

#100 ms bounce ignorance constant used for event detection
GPIO_BUTTON_EVENT_BOUNCETIME = 100

#states used for TRAVIS state machine
class TRAVIS_STATE(enum.Enum):
	ERROR = -1
	INIT = 0
	IDLE = 1
	ACTIVE = 2

#Period after which to resample input
SAMPLE_INTERVAL = 0.2

