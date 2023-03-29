import RPi.GPIO as GPIO
import time

switchPin = 22
switchPin2 = 23
ledPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchPin,GPIO.IN)
GPIO.setup(switchPin2,GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

try:
	num = 0
	while True:
		if GPIO.input(switchPin) == False:
		   num = num + 1
		   time.sleep(0.2)

		if num %2 == 1:
			GPIO.output(ledPin,GPIO.HIGH)
		elif num %2 == 0:
			GPIO.output(ledPin,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.cleanup()
