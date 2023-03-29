import RPi.GPIO as GPIO
import time

ledPin =
dstinPin =
dstoutPin =
piezoPin =

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(dstinPin,GPIO.IN)
GPIO.setup(dstoutPin,GPIO.OUT)

s = GPIO.PWM(piezoPin, 1000)

GPIO.output(dst

try:
	while True:
		
