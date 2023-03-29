import RPi.GPIO as GPIO
import time

pirPin = 14
redPin = 15
greenPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin,GPIO.IN)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == False:
			print("Detected")
			GPIO.output(redPin,GPIO.HIGH)
			GPIO.output(greenPin,GPIO.LOW)
			time.sleep(0.5)
		else:
			GPIO.output(redPin,GPIO.LOW)
			GPIO.output(greenPin,GPIO.HIGH)

except KeyboardInterrupt:
	GPIO.cleanup()
