import RPi.GPIO as GPIO

class Servo:
	"""Servo will run by default on 50Hz"""
	def __init__(self, pin):
		self.pin = pin
		self.freq = 50
		self.angle = 0
		self.duty_cycle = 0
		self.servo = GPIO.PWM(self.pin, self.freq)
		self.servo.start(2.5)

	def angle_to_duty_cycle(self, degrees):
		print "Convert from angle to duty_cycle ...."
		interval = 12.5 - 2.5
		divisions = interval / 180
		return 2.5 + degrees * divisions

	def duty_cycle_to_angle(self, duty_cycle):
		print "Convert duty_cycle to angle ...."
		interval = 12.5 - 2.5
		divisions = interval / 180
		return float(duty_cycle - 2.5) / degrees

	def set_value(self, degrees): 
		print "Setting value ..."
		duty_cycle = self.angle_to_duty_cycle(degrees)
		print duty_cycle
		self.servo.ChangeDutyCycle(duty_cycle)
		self.angle = degrees

	def get_value(self):
		return self.angle

	def stop(self):
		self.servo.stop()

