# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# Code for a routine that blinks the tpLink smart plugs

from tplink_smartplug import SmartPlug
import time

"""
This function will blink the two smart plugs at
0.5 second intervals
"""
def start_blink():
    # Set up plugs
    livingroom = SmartPlug('192.168.1.140')
    bedroom    = SmartPlug('192.168.1.139')

    # Get initial states of plugs
    livingroom_on_init = livingroom.is_on
    bedroom_on_init = bedroom.is_on
    # Copy initial states of plugs. This will make blinking much faster
    livingroom_on = livingroom_on_init
    bedroom_on = bedroom_on_init

    # We need to keep track of time
    old_time = time.time()
    new_time = time.time()
    while (new_time - old_time < 15):
        # Pause for 1 seconds, then increment time
        time.sleep(0.5)
        new_time = time.time()

        # Blink lights
        if bedroom_on:
            bedroom.turn_off()
            bedroom_on = False
        else:
            bedroom.turn_on()
            bedroom_on = True
        # if livingroom_on:
        #     livingroom.turn_off()
        #     livingroom_on = False
        # else:
        #     livingroom.turn_on()
        #     livingroom_on = True
        
    # Make sure lights end how they started
    if livingroom_on_init:
        livingroom.turn_on()
    else:
        livingroom.turn_off()
    if bedroom_on_init:
        bedroom.turn_on()
    else:
        bedroom.turn_off()
