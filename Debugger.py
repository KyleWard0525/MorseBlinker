"""
Debugging functions

kward
"""
import time
from machine import Pin

onboard_led = Pin(25, Pin.OUT)

# Enable onboard LED as a status indicator
def onboardLED(enable=True):
    if enable:
        onboard_led.high()
    else:
        onboard_led.low()
