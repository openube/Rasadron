#!/usr/bin/python
# Control PWM Motors

from __future__ import division
import time
#import RPi.GPIO as GPIO

class Motor:

	# Initialize motor
	def __init__(self,pin,GPIO):
		self.speed = 0
		self.hz = 50
		self.pin = pin
		self.GPIO = GPIO
		self.GPIO.setup(pin, self.GPIO.OUT)
		self.power = self.GPIO.PWM(pin, self.hz)
		#self.start()

	# Set motor speed (increase|decrease|0-100)
	def set_speed(self,speed):
		if speed == "increase":
			new_speed = self.get_speed()+1
		elif speed == "decrease":
			new_speed = self.get_speed()-1
		else:
			new_speed = speed
		if new_speed < 0:
			new_speed = 0
		elif new_speed > 100:
			new_speed = 100
		self.speed = new_speed
		self.power.ChangeDutyCycle(new_speed/10)

	# Get current motor speed
	def get_speed(self):
		return self.speed

	# Start motor
	def start(self):
		self.power.start(0)
		self.set_speed(40)

	# Stop motor
	def stop(self,exit):
		self.set_speed(0)
		self.power.stop()
		if exit == true:
			self.GPIO.cleanup()
