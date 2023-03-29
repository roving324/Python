from RPi_I2C_LCD_driver import RPi_I2C_driver
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(triggerPin, True)
	time.sleep(0.00001)				# 10us
	GPIO.output(triggerPin, False)

	while GPIO.input(echoPin) == False:
		start = time.time()					# echo High
	while GPIO.input(echoPin) == True:
		stop = time.time()					# echo Low
	elapsed = stop - start
	distance = (elapsed * 34000) / 2		# cm/us
	return distance

triggerPin = 24
echoPin = 23
piezoPin = 25 

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

lcd = RPi_I2C_driver.lcd(0x27)
lcd.clear()
lcd.setCursor(0,0)
lcd.print("Distance")
lcd.setCursor(14,1)
lcd.print("cm")

s = GPIO.PWM(piezoPin, 1000)

def sound(melody,sleep):
	s.start(50)
	s.ChangeFrequency(melody)
	lcd.setCursor(0,1)
	lcd.print("%.2f" % distance)
	time.sleep(sleep)

def lcdprint(distance):
	import threading

try:
	while True:
		distance = measure()
		if distance < 20:
			sound(4180,0.02)
		elif distance < 30:
			sound(2093,0.05)
		elif distance < 50:
			sound(1046,0.07)
		else:
			lcd.setCursor(0,1)
			lcd.print("%.2f" % distance)
		s.stop()
		time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
