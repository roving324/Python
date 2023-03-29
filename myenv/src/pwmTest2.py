import RPi.GPIO as GPIO
import time

piezoPin = 13

melody = [262,262,278,294,330,349,392,440,494,523]
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin,GPIO.OUT)

s = GPIO.PWM(piezoPin, 1000)

try:
	while True:
		num = str(getch())
		s.start(50)
		for i in num:
			if 0<int(i)<10:
				s.ChangeFrequency(melody[int(i)])
				time.sleep(0.5)
			else:
				continue
		s.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
