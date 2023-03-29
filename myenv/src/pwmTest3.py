import sys,  termios,tty,os,time
import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [262,262,278,294,330,349,392,440,494,523]
GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin,GPIO.OUT)

s = GPIO.PWM(piezoPin, 1000)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
	return ch

try:
	while True:
		char = getch()
		s.start(50)
		s.ChangeFrequency(melody[int(char)])
		time.sleep(0.5)
		if char == '0':
			GPIO.cleanup()
		s.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
