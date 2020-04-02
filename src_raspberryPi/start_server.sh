#!/bin/bash

# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# This script starts the python flask server upon startup.
# Simply type "sudo crontab -e" add the line:
#   @reboot sh /home/pi/DeafDoorbell/src_raspberryPi/start_server.sh >/home/pi/logs/server.log 2>&1
# to cronjob file and ESC+:wq it.

sleep 10
su -c 'python3 /home/pi/DeafDoorbell/src_raspberryPi/pi_server.py >/home/pi/logs/server.log' pi
sleep 10
