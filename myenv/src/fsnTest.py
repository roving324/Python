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
	for i in range(7):
		GPIO.output(pin[i],0)
def method(len,char):
	GPIO.output(digit[len],0)
	LedPin(char)
	time.sleep(0.001)
	GPIO.output(digit[len],1)
list = []
for i in reversed(str(input("4 num : "))):
	list.append(i)
	clear()
try:
	while True:
		for a,b in enumerate(list):
			method(a,int(b))
except keyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup()
	clear()
