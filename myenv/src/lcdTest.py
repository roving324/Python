from RPi_I2C_LCD_driver import RPi_I2C_driver
import RPi.GPIO as GPIO
import time

lcd = RPi_I2C_driver.lcd(0x27)
lcd.clear()

#lcd.setCursor(0, 0)
#lcd.print("Lcd Test")
#lcd.setCursor(0,1)
#lcd.print("Hello Lcd!!")

nums = (1,2,3,4,5,6,7,8,9)

try:
	while True:
		for num in nums:
			lcd.setCursor(0,0)
			lcd.print("%d dan" % num)
			for num2 in nums:
				lcd.setCursor(0,1)
				result = num * num2
				lcd.print("%d x %d = %d " %(num, num2, result))
				time.sleep(0.5)

		GPIO.cleanup()

except KeyboardInturrupt:
	GPIO.cleanup()
