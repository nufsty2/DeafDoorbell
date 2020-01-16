#!/bin/sh

# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# This script starts the python flask server upon startup.
# Simply add the line:
#   /home/pi/DeafDoorbell/src_raspberryPi/start_server.sh &
# to the /etc/rc.local file to have this run upon boot

sleep 10
python3 pi_server.py