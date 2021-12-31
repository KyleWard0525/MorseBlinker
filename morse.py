"""
This module is an attempt at creating an easy-to-use
English to Morse code converter

kward
"""
import time
#import winsound

# Morse code class
class MorseCode:
    
    # Initialize object
    def __init__(self, freq=1900, dot_dur=250, dash_dur=550):
        self.freq = freq
        self.dot_dur = dot_dur
        self.dash_dur = dash_dur
        self.letter_space_dur = 0.3
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    # Play dot sound
    def dot(self):
        pass
        #winsound.Beep(self.freq, self.dot_dur)

    # Play dash sound
    def dash(self):
        pass
        #winsound.Beep(self.freq, self.dash_dur)
        
    """ Letter Functions """
    def a(self):
        self.dot()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        # Return letter as array of beep durations
        return [self.dot_dur, self.dash_dur]
    
    def b(self):
        self.dash()
        [self.dot() for i in range(0,3)]
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dash_dur,self.dot_dur,self.dot_dur,self.dot_dur]
        
    def c(self):
        self.dash()
        self.dot()
        self.dash()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dash_dur,self.dot_dur,self.dash_dur,self.dot_dur]
    
    def d(self):
        self.dash()
        self.dot()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dash_dur,self.dot_dur,self.dot_dur]
    
    def e(self):
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur]
    
    def f(self):
        self.dot()
        self.dot()
        self.dash()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur,self.dot_dur,self.dash_dur,self.dot_dur]
    
    def g(self):
        self.dash()
        self.dash()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dash_dur,self.dash_dur,self.dot_dur]
    
    def h(self):
        [self.dot() for i in range(0,4)]
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur for i in range(0,4)]
    
    def i(self):
        self.dot()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur,self.dot_dur]
    
    def j(self):
        self.dot()
        [self.dash() for i in range(0,3)]
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur,self.dash_dur,self.dash_dur,self.dash_dur]

    def k(self):
        self.dash()
        self.dot()
        self.dash()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dash_dur,self.dot_dur,self.dash_dur]
    
    def l(self):
        self.dot()
        self.dash()
        self.dot()
        self.dot()
        
        # Sleep before next letter
        #time.sleep(self.letter_space_dur)
        
        return [self.dot_dur,self.dash_dur,self.dot_dur,self.dot_dur]
    
    def m(self):
        self.dash()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return[self.dash_dur, self.dash_dur]
        
    def n(self):
        self.dash()
        self.dot()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur, self.dot_dur]

    def o(self):
        [self.dash() for i in range(0,3)]

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur for i in range(0,3)]

    def p(self):
        self.dot()
        self.dash()
        self.dash()
        self.dot()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur,self.dash_dur,self.dash_dur,self.dot_dur]

    def q(self):
        self.dash()
        self.dash()
        self.dot()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur,self.dash_dur,self.dot_dur,self.dash_dur]

    def r(self):
        self.dot()
        self.dash()
        self.dot()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur,self.dash_dur,self.dot_dur]

    def s(self):
        [self.dot() for i in range(0,3)]

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur for i in range(0,3)]

    def t(self):
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur]

    def u(self):
        self.dot()
        self.dot()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur,self.dot_dur,self.dash_dur]

    def v(self):
        [self.dot() for i in range(0,3)]
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur,self.dot_dur,self.dot_dur,self.dash_dur]

    def w(self):
        self.dot()
        self.dash()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dot_dur,self.dash_dur,self.dash_dur]

    def x(self):
        self.dash()
        self.dot()
        self.dot()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur,self.dot_dur,self.dot_dur,self.dash_dur]

    def y(self):
        self.dash()
        self.dot()
        self.dash()
        self.dash()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur,self.dot_dur,self.dash_dur,self.dash_dur]

    def z(self):
        self.dash()
        self.dash()
        self.dot()
        self.dot()

        # Sleep before next letter
        #time.sleep(self.letter_space_dur)

        return [self.dash_dur,self.dash_dur,self.dot_dur,self.dot_dur]


    #   Say message in Morse code and return array of letter durations
    def say(self, message):
        # Letters encoded as arrays of beep durations
        encoded = []

        # Letter function template
        func = lambda x: getattr(self, x)()

        # Split message
        msg = message.split()

        # Check if the message contains more than one word
        if len(msg) > 1:
            # Loop through each word in the message
            for word in msg:
                # Convert word to array of chars
                word_arr = list(word.lower())

                # Array for storing all letter codes in the word
                letter_codes = []

                # Loop through each letter in the word
                for letter in word_arr:
                    # Check if letter is in alphabet
                    if not letter in self.alphabet:
                        return "ERROR in MorseCode.say(): '" + str(letter) + "' is not a supported character"
                    
                    # Call letter function
                    res = func(letter)

                    # Add letter codes to list
                    letter_codes.append(res)

                # Add word codes to encoded array
                encoded.append(letter_codes)

        # Contains 1 or fewer
        else:
            msg_arr = list(message.lower())

            # Loop through each letter in the message
            for letter in msg_arr:
                res = func(letter)

                # Add letter to encoded message
                encoded.append(res)

            
        return encoded
    