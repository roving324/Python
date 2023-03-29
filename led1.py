import RPi.GPIO as GPIO
import time

ledPin = 4
Pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(Pin, GPIO.OUT)

while True:
	GPIO.output(ledPin, GPIO.HIGH)
	GPIO.output(Pin, GPIO.LOW)
	time.sleep(1)
	GPIO.output(ledPin, GPIO.LOW)
	GPIO.output(Pin, GPIO.HIGH)
	time.sleep(1)
   
GPIO.cleanup()
