import RPi.GPIO as GPIO
import time

switchPin = 22
switchPin2 = 23 
ledPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin,GPIO.IN)
GPIO.setup(switchPin2,GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin,GPIO.LOW)
try:
	while True:
		if GPIO.input(switchPin) == False:
		   GPIO.output(ledPin,GPIO.HIGH)

		if GPIO.input(switchPin2) == False:
			GPIO.output(ledPin,GPIO.LOW)

except KeyboardInterrupt:
	GPIO.cleanup()
