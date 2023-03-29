import RPi.GPIO as GPIO
import time

pin = [14,15,18,23,24,25,8,7]
digit = [17,4,3,2]

GPIO.setmode(GPIO.BCM)
for i in range(8):
	GPIO.setup(pin[i],GPIO.OUT)
for i in range(4):
	GPIO.setup(digit[i],GPIO.OUT)

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],
		 [0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],
		 [1,1,1,1,1,1,1],[1,1,1,0,0,1,1]]

def LedPin(nums):
	for i in range(7):
		GPIO.output(pin[i],num[nums][i])
def clear():
	for i in range(4):
		GPIO.output(digit[i],1)
def method(len,char,t):
	GPIO.output(digit[len],0)
	LedPin(char)
	time.sleep(t)
	GPIO.output(digit[len],1)

try:
	while True:
		t = 1/100
		for a in range(10):
			for b in range(50):
				method(0,a,t)
			time.sleep(0.1)
		t = 5/1000
		for a in range(1,10):
			for b in range(10):
				for i in range(50):
					method(1,a,t)
					method(0,b,t)
				time.sleep(0.005)
		t = 5/1000
		for a in range(1,10):
			for b in range(10):
				for c in range(10):
					for i in range(20):
						method(2,a,t)
						method(1,b,t)
						method(0,c,t)
					time.sleep(0.001)
		t = 3/1000
		for a in range(1,10):
			for b in range(10):
				for c in range(10):
					for d in range(10):
						for i in range(20):
							method(3,a,t)
							method(2,b,t)
							method(1,c,t)
							method(0,d,t)
						time.sleep(0.001)
except keyboardInterrupt:
	GPIO.cleanup()
finally:
	clear()
