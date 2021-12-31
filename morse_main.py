"""

Test main file for MorseBlinker

kward
"""
import sys
import time
from Debugger import onboardLED
from morse import MorseCode
from LedController import LED

led = ''

# Main function
def main():
    global led
    
    # Enable on-board LED as status indicator
    onboardLED(True)
    
    # Create class objects
    morse_code = MorseCode()
    led = LED(0)
    
    # Get blink duration codes 
    msg_codes = morse_code.say("Hello")
    
    for letter in msg_codes:
        for code in letter:
            led.enable(code/1000.0)
            time.sleep(0.2)
        time.sleep(morse_code.letter_space_dur)
    
    cleanup()
    
# Free resources
def cleanup():
    global led
    
    # Disabled on-board LED
    onboardLED(False)
    led.disable()
    
    sys.exit()

# Run as script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
        
        