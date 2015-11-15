# How this works?
# 1. Set up GPIO to associate pin with led and output
# 2. Send output True/Flase (on/off) depending the case
# 3. Wait or Pause or 'sleep' and resent True/Flase (on/off)

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

number_of_blinks = 100
how_fast_to_blink = 0.01 # 0.01 of 1 second

for each_number in range(0, number_of_blinks):
    GPIO.output(pin, True) # Turn Led ON
    # Basically we just pause ('sleep') the for loop.
    #Next line does that, indicates the time period we want loop to pause.
    time.sleep(how_fast_to_blink) # Wait or Pause or 'sleep' 
    GPIO.output(pin, False) # Turn Led OFF
    print "Blink counter {0}".format(each_number)

# After all, clean up 
print "Blink is Over, you are awesome!!!"
GPIO.cleanup()

