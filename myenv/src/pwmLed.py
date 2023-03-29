import RPi.GPIO as GPIO
import time

led = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

m = GPIO.PWM(led, 1000) #1000Hz
m.start(0)

try:
	while True:
		for dc in range(0, 101, 1): #duty 0~100 duty time
			m.ChangeDutyCycle(dc)    #duty cycle change
			time.sleep(0.01)
		for dd in range (100,0, -1):
			m.ChangeDutyCycle(dd)
			time.sleep(0.01)

except KeyboardInterrupt:
	m.stop()
	GPIO.cleanup()
