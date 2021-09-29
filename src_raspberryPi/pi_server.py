# Made by Jeff DeGraw for the DeafDoorbell project
# 2020-01-15

# Code for a simple flask server that will receive 
# commands from the ESP8266 and blink lights

from flask import Flask
import blink

app = Flask(__name__)

"""
This function will respond to 
"""
@app.route('/ring')
def ring():
    blink.start_blink()
    return "Hello from the raspberry Pi\n"

app.run(host='0.0.0.0', port=8090)
