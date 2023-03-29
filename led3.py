import RPi.GPIO as GPIO
import time

redPin = 2 
greenPin = 3
bluePin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

while True:
	GPIO.output(redPin, GPIO.HIGH)
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(bluePin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(redPin, GPIO.LOW)
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(bluePin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(redPin, GPIO.LOW)
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(bluePin, GPIO.HIGH)
	time.sleep(1)
   
GPIO.cleanup()
