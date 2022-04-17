#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#03/16/2022

#This file handles the state machine of TRAVIS

# import lirc
# import time

# power = False
# client = lirc.Client()

# if power button pressed, turn remote on and set power = true
    # client.send_once(remote_style, POWER)

    # * assign button that was pressed below *
    # button_pressed = 

    # * change all case statements to mapped buttons later *
    # match button_pressed:
        # case VOLUMEUP: # if remote on (power = True) and vol up pressed turn up vol
            # client.send_start(remote_style, VOLUMEUP)
            # while vol up button pressed
                # time.sleep(1)
            # client.send_stop(remote_style, VOLUMEUP)

        # case VOLUMEDOWN: 
            # client.send_start(remote_style, VOLUMEDOWN)
            # while vol down button pressed
                # time.sleep(1)
            # client.send_stop(remote_style, VOLUMEDOWN)

        # case CHANNELUP:
            # client.send_start(remote_style, CHANNELUP)
            # while channel up button pressed
                # time.sleep(1)
            # client.send_stop(remote_style, CHANNELUP)

        # case CHANNELDOWN:
            # client.send_start(remote_style, CHANNELDOWN)
            # while channel up button pressed
                # time.sleep(1)
            # client.send_stop(remote_style, CHANNELDOWN)

        # case MUTE: # need to add unmute, is it the same button again? (lirc and on TRAVIS)
            # client.send_once(remote_style, MUTE)
        
        # case POWER: # not sure if this is how to turn off again
            # client.send_once(remote_style, POWER)
            # break

        # add case statement for TRAVIS button and handle those separately based on what is
        # asked to be done






# OLD (NOT SURE IF REPEAT_COUNT AUTO FILLS OR IF IT HAS TO BE SPECIFIED)
# if remote on (power = True) and vol up pressed turn up vol
    # continue going up while button pressed
    # client.send_once(remote_style, VOLUMEUP, repeat_count)

# if remote on (power = True) and vol down pressed turn down vol
    # client.send_once(remote_style, VOLUMEDOWN, repeat_count)

# if remote on (power = True) and channel up pressed go up a channel #
    # client.send_once(remote_style, CHANNELUP, repeat_count)

# if remote on (power = True) and channel down pressed go down a channel #
    # client.send_once(remote_style, CHANNELDOWN, repeat_count)
