"""

Basic single-LED controller

kward
"""

import time
from machine import Pin
from Debugger import onboardLED

# LED Controller
class LED:
    
    # Initialize
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        
    # Enable LED for a given time
    def enable(self, duration):
        # Check if no time was given
        if not duration:
            # Turn on led until disable() is called
            self.led.high()
        else:
            # Turn on led for given time
            self.led.high()
            time.sleep(duration)
            self.led.low()
            
    # Disable LED
    def disable(self):
        self.led.low()
        
    # Blink onboard led at every time interval for given duration
    def blink(self, delay, duration):
        start = time.time()
        
        # Loop until time limit is reached
        while time.time() - start < duration:
            self.led.toggle()
            time.sleep(delay)
            
        self.led.low()

