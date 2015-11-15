import RPi.GPIO as GPIO


# use board pin numbering, other choice is BCM
GPIO.setmode(GPIO.BOARD)

# set pin number
pin = 7

# set GPIO out to pin 
GPIO.setup(pin, OUT)

# set Led to On or High or True
GPIO.output(pin, True) # Led is on 

# set Led to Off or Low or False
GPIO.output(pin, False) # Led is off

