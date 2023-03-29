import sys, termios, tty, os, time
import RPi.GPIO as GPIO
import time

a = 2
b = 3
c = 4
d = 17
e = 27
f = 22
g = 10
dp = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)
GPIO.setup(f,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(dp,GPIO.OUT)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch
# a b c d e f g dp 7,8,9
pin = [a,b,c,d,e,f,g]
num = [[0,0,0,0,0,0,1],[1,0,0,1,1,1,1],[0,0,1,0,0,1,0],[0,0,0,0,1,1,0],[1,0,0,1,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,0,0,0],[0,0,0,1,1,0,0]]

def LedPin(nums):
	for i in range(7):
		GPIO.output(pin[i],num[nums][i])

LedPin(0)
GPIO.output(dp,1)
count = 0
try:
	while True:
		char = getch()
		if char == 'a':
			GPIO.cleanup()
			break
		if char == '.':
			if count % 2 == 0:
				GPIO.output(dp,0)
			elif count % 2 == 1:
				GPIO.output(dp,1)
			count = count + 1
			continue
		if char.isdigit() == False:
			continue

		LedPin(int(char))

except keyboardInterrupt:
	GPIO.cleanup()
