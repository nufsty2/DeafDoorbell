# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# Code for a routine that blinks the tpLink smart plugs

from tplink_smartplug import SmartPlug
import time

# Set up plugs
hs100_kitchen = SmartPlug('192.168.1.140')
hs100_office = SmartPlug('192.168.1.139')
hs103_guestroom = SmartPlug('192.168.1.136')
hs103_livingroom = SmartPlug('192.168.1.110')
hs103_bedroom = SmartPlug('192.168.1.125')
hs103_basement = SmartPlug('192.168.1.122')
hs105_piano = SmartPlug('192.168.1.130')
hs105_porch = SmartPlug('192.168.1.121')

hs100_kitchen_on_init = False
hs100_office_on_init = False
hs103_guestroom_on_init = False
hs103_livingroom_on_init = False
hs103_bedroom_on_init = False
hs103_basement_on_init = False
hs105_piano_on_init = False
hs105_porch_on_init = False


def set_initial_states():
    global hs100_kitchen_on_init
    global hs100_office_on_init
    global hs103_guestroom_on_init
    global hs103_livingroom_on_init
    global hs103_bedroom_on_init
    global hs103_basement_on_init
    global hs105_piano_on_init
    global hs105_porch_on_init

    hs100_kitchen_on_init = hs100_kitchen.is_on
    hs100_office_on_init = hs100_office.is_on
    hs103_guestroom_on_init = hs103_guestroom.is_on
    hs103_livingroom_on_init = hs103_livingroom.is_on
    hs103_bedroom_on_init = hs103_bedroom.is_on
    hs103_basement_on_init = hs103_basement.is_on
    hs105_piano_on_init = hs105_piano.is_on
    hs105_porch_on_init = hs105_porch.is_on


def reset_light(plug, is_on_init):
    if plug.is_on and not is_on_init:
        plug.turn_off()
    elif not plug.is_on and is_on_init:
        plug.turn_on()


def reset_lights():
    # Make sure lights end how they started
    reset_light(hs100_kitchen, hs100_kitchen_on_init)
    reset_light(hs100_office, hs100_office_on_init)
    reset_light(hs103_guestroom, hs103_guestroom_on_init)
    reset_light(hs103_livingroom, hs103_livingroom_on_init)
    reset_light(hs103_bedroom, hs103_bedroom_on_init)
    reset_light(hs103_basement, hs103_basement_on_init)
    reset_light(hs105_piano, hs105_piano_on_init)
    reset_light(hs105_porch, hs105_porch_on_init)


def blink_light(plug):
    if plug.is_on:
        plug.turn_off()
    else:
        plug.turn_on()


"""
This function will blink the smart plugs at 1 second intervals
"""
def start_blink():
    # Keep track of number of blinks
    num_blinks = 0

    set_initial_states()

    try:
        # num_blinks < #: # should be even
        while (num_blinks < 8):
            # Blink lights
            blink_light(hs100_office)
            blink_light(hs100_kitchen)
            blink_light(hs103_guestroom)
            blink_light(hs103_livingroom)
            blink_light(hs103_bedroom)
            blink_light(hs103_basement)
            blink_light(hs105_piano)
            blink_light(hs105_porch)

            # Pause for 1 second, then increment time
            time.sleep(1)
            num_blinks += 1

        reset_lights()

    except:
        # Make sure lights end how they started
        reset_lights()
