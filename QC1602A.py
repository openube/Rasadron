#!/usr/bin/python
# LCD Screen - QC1602A V2.0

# THIS IS STILL IN DEVELOPMENT
# AND PROBABLY WONT BE USED ON THIS PROJECT
# THIS FILE HERE IS JUST FOR REFERENCE

# import

import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping

LCD_RS = 7
LCD_E = 0x08
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

# Define some device constants

LCD_WIDTH = 0x10  # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80  # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0  # LCD RAM address for the 2nd line

# Timing constants

E_PULSE = 0.00005
E_DELAY = 0.00005

def message(msg1,msg2):
	lcd_byte(LCD_LINE_1, LCD_CMD)
	lcd_string(msg1)
	lcd_byte(LCD_LINE_2, LCD_CMD)
	lcd_string(msg2)

msg_txt1 = "Raspberry Pi"
msg_txt2 = "LCD Test"

def main():

  # Main program block

	GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers
	GPIO.setup(LCD_E, GPIO.OUT)  # E
	GPIO.setup(LCD_RS, GPIO.OUT)  # RS
	GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
	GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
	GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
	GPIO.setup(LCD_D7, GPIO.OUT)  # DB7

  # Initialise display

	lcd_init()

  # Send some test

	message(msg_txt1,msg_txt2)

	time.sleep(3)  # 3 second delay


def lcd_init():

  # Initialise display

	lcd_byte(0x33, LCD_CMD)
	lcd_byte(0x32, LCD_CMD)
	lcd_byte(0x28, LCD_CMD)
	lcd_byte(0x0C, LCD_CMD)
	lcd_byte(0x06, LCD_CMD)
	lcd_byte(0x01, LCD_CMD)


def lcd_string(message):

  # Send string to display

	message = message.ljust(LCD_WIDTH, ' ')

	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), LCD_CHR)


def lcd_byte(bits, mode):

  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

	GPIO.output(LCD_RS, mode)  # RS

  # High bits

	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	if bits & 0x10 == 0x10:
		GPIO.output(LCD_D4, True)
	if bits & 0x20 == 0x20:
		GPIO.output(LCD_D5, True)
	if bits & 0x40 == 0x40:
		GPIO.output(LCD_D6, True)
	if bits & 0x80 == 0x80:
		GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin

	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

  # Low bits

	GPIO.output(LCD_D4, False)
	GPIO.output(LCD_D5, False)
	GPIO.output(LCD_D6, False)
	GPIO.output(LCD_D7, False)
	if bits & 0x01 == 0x01:
		GPIO.output(LCD_D4, True)
	if bits & 0x02 == 0x02:
		GPIO.output(LCD_D5, True)
	if bits & 0x04 == 0x04:
		GPIO.output(LCD_D6, True)
	if bits & 0x08 == 0x08:
		GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin

	time.sleep(E_DELAY)
	GPIO.output(LCD_E, True)
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, False)
	time.sleep(E_DELAY)

if __name__ == '__main__':
	main()

while True:
	message(msg_txt1,msg_txt2)
	time.sleep(3)