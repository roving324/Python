import sys,  termios,tty,os,time
import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [392,330,330,392,330,262,311,330,311,262,330,392,523,392,523,392,523,392,330,392,262,349,330,311,262]
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
		if char == '1':
			print(char)
		#s.start(50) # PWM start
		#for i in range (len(melody)):
			#s.ChangeFrequency(melody[i])
			#time.sleep(0.5)
		#s.stop()  # PWM stop
		#time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
