#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/03/2022

#This file handles the television communication of TRAVIS

#TV Comms handled by https://www.lirc.org/
#supported IR devices http://lirc-remotes.sourceforge.net/remotes-table.html

import lirc
import lirc.exceptions

from enum import Enum

#for simple command input
#matches name with text in remote config files
class RemoteInput(Enum):
	POWER = "KEY_POWER"
	STOP = "KEY_STOP"
	REWIND = "KEY_REWIND"
	FASTFORWARD = "KEY_FASTFORWARD"
	TIME = "KEY_TIME"
	VOLUMEUP = "KEY_VOLUMEUP"
	VOLUMEDOWN = "KEY_VOLUMEDOWN"
	PLAY = "KEY_PLAY"
	UP = "KEY_UP"
	DOWN = "KEY_DOWN"
	SAVE = "KEY_SAVE"
	SHUFFLE = "KEY_SHUFFLE"
	SLEEP = "KEY_SLEEP"
	PAUSE = "KEY_PAUSE"
	SLOW = "KEY_SLOW"
	RECORD = "KEY_RECORD"
	CHANNELUP = "KEY_CHANNELUP"
	CHANNELDOWN = "KEY_CHANNELDOWN"
	ONE = "KEY_1"
	TWO = "KEY_2"
	THREE = "KEY_3"
	FOUR = "KEY_4"
	FIVE = "KEY_5"
	SIX = "KEY_6"
	SEVEN = "KEY_7"
	EIGHT = "KEY_8"
	NINE = "KEY_9"
	ZERO = "KEY_0"
	MUTE = "KEY_MUTE"
	PREVIOUS = "KEY_PREVIOUS"
	NEXT = "KEY_NEXT"
	A = "KEY_A"
	B = "KEY_B"
	C = "KEY_C"
	D = "KEY_D"
	E = "KEY_E"
	F = "KEY_F"
	G = "KEY_G"
	H = "KEY_H"
	I = "KEY_I"
	J = "KEY_J"
	K = "KEY_K"
	L = "KEY_L"
	M = "KEY_M"
	N = "KEY_N"
	O = "KEY_O"
	P = "KEY_P"
	Q = "KEY_Q"
	R = "KEY_R"
	S = "KEY_S"
	T = "KEY_T"
	U = "KEY_U"
	V = "KEY_V"
	W = "KEY_W"
	X = "KEY_X"
	Y = "KEY_Y"
	Z = "KEY_Z"

#chosen remote config
remote_style = "default"

#initialize client/daemon connection
#https://lirc.readthedocs.io/en/latest/usage.html
lirc_client = lirc.Client()

#close lirc connection
def closeLIRC():
	return lirc_client.close()

#set remote style
def setstyle(input_style:str):
	global remote_style
	remote_style = input_style
	return

#send key across lirc connection
#sends to lirc daemon that handles driving the IR transceiver
def send(key:RemoteInput):
	return lirc_client.send_once(remote_style, key.value)
