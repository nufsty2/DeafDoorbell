# Deaf Doorbell
![Final Product](https://github.com/nufsty2/DeafDoorbell/blob/master/Demos/InUse.jpg)

What you will need:
* ESP8266 MicroController
* Raspberry Pi (I have a 3B+)
* TP-Link Smart Plug(s)

## Why?
My wife has severe hearing loss and uses hearing aids. Around the house, she will frequently take them out for comfort. Occasionally, this leads to communication confusion, but they are usually quite minor. *Usually*. One time, I left to put our laundry in and forgot my key. My wife was taking a shower, and wasn't even aware that I was gone. I was locked out for nearly 1/2 hour once she realized what was going on!

## What?
I have seen "deaf doorbells" before in some of our deaf friends. Instead of just playing a chime, they also blink a light or two in the house to give them a visual cue that they need to answer the door. This would be perfect for my wife!

## How?
*This is where the fun begins.* We live in a relatively old apartment on BYU campus, so there's no way I'm tapping into the wiring of our place. Conveniently, we received two TP-Link HS100 Smart Plugs for Christmas. I found an [open source TP-Link Python library](https://github.com/vrachieru/tplink-smartplug-api) that made [blinking two lights](https://github.com/nufsty2/DeafDoorbell/blob/master/src_raspberryPi/blink.py) connected to the smart plugs pretty easy.

Next, I had to figure out what to use as the doorbell. An ESP8266 works great, because it can be programmed like an Arduino, is small, and has built-in WiFi. I had it so the [FLASH button](https://github.com/nufsty2/DeafDoorbell/blob/master/src_ESP8266/doorbell/doorbell.ino) will trigger the blinking.

This was where I came to a wall. If the light blinking code has to be in Python, and the ESP8266 is programmed in C++, how am I going to get those to work together. I looked into running Python on Arduinos, but came to the conclusion that it's sketchy at best and you have to have the Arduino plugged into your computer. Then, I remembered that I have a Raspberry Pi connected to my network that acts as my DNS gateway and blocks ads using [PiHole](https://pi-hole.net/) (I would highly recommend setting one up!). Huzzah! So, I programmed a simple Flask HTTP server to [run on the Pi on startup](https://github.com/nufsty2/DeafDoorbell/blob/master/src_raspberryPi/start_server.sh). This server [simply waits for a GET request](https://github.com/nufsty2/DeafDoorbell/blob/master/src_raspberryPi/pi_server.py) from the ESP8266, and then runs the blinking lights code.

The last step was housing the ESP8266 in something cool, so I 3D printed a case for it on campus using [this file](https://www.thingiverse.com/thing:2786523)!

Block Diagram:
![Block Diagram](https://github.com/nufsty2/DeafDoorbell/blob/master/Demos/Deaf%20Doorbell.svg)

## Dependencies
[TP-Link Smart Plug Python Library](https://github.com/vrachieru/tplink-smartplug-api)

[Flask](https://pypi.org/project/Flask/) (for the Pi server)

[ESP8266 Arduino Libraries](https://github.com/esp8266/Arduino)
