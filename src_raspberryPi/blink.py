# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# Code for a routine that blinks the tpLink smart plugs

from tplink_smartplug import SmartPlug
import time

# Set up plugs
livingroom  = SmartPlug('192.168.1.140')
bedroom     = SmartPlug('192.168.1.139')
kitchen     = SmartPlug('192.168.1.136')
desk        = SmartPlug('192.168.1.110')
bathroom    = SmartPlug('192.168.1.125')
twinklies   = SmartPlug('192.168.1.122')

# Get initial states of plugs
livingroom_on_init  = livingroom.is_on
bedroom_on_init     = bedroom.is_on
kitchen_on_init     = kitchen.is_on
desk_on_init        = desk.is_on
bathroom_on_init    = bathroom.is_on
twinklies_on_init   = twinklies.is_on


def reset_light(plug, is_on_init):
    if plug.is_on and not is_on_init:
        plug.turn_off()
    elif not plug.is_on and is_on_init:
        plug.turn_on()


def reset_lights():
    # Make sure lights end how they started
    reset_light(livingroom, livingroom_on_init)
    reset_light(bedroom, bedroom_on_init)
    reset_light(kitchen, kitchen_on_init)
    reset_light(desk, desk_on_init)
    reset_light(bathroom, bathroom_on_init)
    reset_light(twinklies, twinklies_on_init)


def blink_light(plug):
    if plug.is_on:
        plug.turn_off()
    else:
        plug.turn_on()


"""
This function will blink the two smart plugs at
0.5 second intervals
"""
def start_blink():
    # Keep track of number of blinks
    num_blinks = 0

    try:
        # num_blinks < #: # should be even
        while (num_blinks < 8):
            # Blink lights
            blink_light(bedroom)
            blink_light(livingroom)
            blink_light(kitchen)
            blink_light(desk)
            blink_light(bathroom)
            blink_light(twinklies)

            # Pause for 1 second, then increment time
            time.sleep(1)
            num_blinks += 1

        reset_lights()
        
    except:
        # Make sure lights end how they started
        reset_lights()
