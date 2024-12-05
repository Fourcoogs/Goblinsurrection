#
# PROGRAM: dice.py
#
# Version: 0.1
#
# COURSE: COSC 3143-01
# AUTHOR: Will Berger
# ASSIGNMENT: Main Project ("Goblinsurrection")
# PURPOSE: ...
# DEPENDENCIES: ...
# Operational Status: WIP
#
import random
import RPi.GPIO as GPIO
import time

R2 = 29
R1 = 10
R4 = 36
R6 = 31

L1 = 5
L2a = 35
L2b = 16
L4a = 32
L4b = 33
L6 = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)
GPIO.setup(R6, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2a, GPIO.OUT)
GPIO.setup(L2b, GPIO.OUT)
GPIO.setup(L4a, GPIO.OUT)
GPIO.setup(L4b, GPIO.OUT)
GPIO.setup(L6, GPIO.OUT)

GPIO.output(R1, GPIO.LOW)
GPIO.output(R2, GPIO.LOW)
GPIO.output(R4, GPIO.LOW)
GPIO.output(R6, GPIO.LOW)
GPIO.output(L1, GPIO.LOW)
GPIO.output(L2a, GPIO.LOW)
GPIO.output(L2b, GPIO.LOW)
GPIO.output(L4a, GPIO.LOW)
GPIO.output(L4b, GPIO.LOW)
GPIO.output(L6, GPIO.LOW)

def resetLEDs():
	#turning off the lights to ensure that only the corresponding
	# LEDs turn on in the roll() method
	GPIO.output(R1, GPIO.LOW)
	GPIO.output(R2, GPIO.LOW)
	GPIO.output(R4, GPIO.LOW)
	GPIO.output(R6, GPIO.LOW)
	GPIO.output(L1, GPIO.LOW)
	GPIO.output(L2a, GPIO.LOW)
	GPIO.output(L2b, GPIO.LOW)
	GPIO.output(L4a, GPIO.LOW)
	GPIO.output(L4b, GPIO.LOW)
	GPIO.output(L6, GPIO.LOW)
	return

def lightShow():
	global L1, L2a, L2b, L4a, L4b, L6, R1, R2, R4, R6
	for i in range(18):
		GPIO.output(L2b, GPIO.HIGH)
		GPIO.output(R1, GPIO.HIGH)
		GPIO.output(L1, GPIO.LOW)
		GPIO.output(R4, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(L2a, GPIO.HIGH)
		time.sleep(0.02)
		GPIO.output(R2, GPIO.HIGH)
		GPIO.output(L6, GPIO.LOW)
		GPIO.output(L4b, GPIO.LOW)
		GPIO.output(L4a, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(R6, GPIO.LOW)
		GPIO.output(L1, GPIO.HIGH)
		GPIO.output(R4, GPIO.HIGH)
		GPIO.output(R2, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(L2b, GPIO.LOW)
		GPIO.output(L2a, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(L4a, GPIO.HIGH)
		GPIO.output(R1, GPIO.LOW)
		time.sleep(0.02)
		GPIO.output(R6, GPIO.HIGH)
		GPIO.output(L4b, GPIO.HIGH)
		GPIO.output(L6, GPIO.HIGH)
	resetLEDs()
	return

class Dice:
	def roll(self, winNo, lossNo):
		die1 = random.randrange(1, 7)
		die2 = random.randrange(0, 7)
		lightShow()
		match die1:
			case 1:
				GPIO.output(L1, GPIO.HIGH)
			case 2:
				GPIO.output(L2a, GPIO.HIGH)
				GPIO.output(L2b, GPIO.HIGH)
			case 3:
				GPIO.output(L2a, GPIO.HIGH)
				GPIO.output(L2b, GPIO.HIGH)
				GPIO.output(L1, GPIO.HIGH)
			case 4:
				GPIO.output(L4a, GPIO.HIGH)
				GPIO.output(L4b, GPIO.HIGH)
				GPIO.output(L2a, GPIO.HIGH)
				GPIO.output(L2b, GPIO.HIGH)
			case 5:
				GPIO.output(L4a, GPIO.HIGH)
				GPIO.output(L4b, GPIO.HIGH)
				GPIO.output(L2a, GPIO.HIGH)
				GPIO.output(L2b, GPIO.HIGH)
				GPIO.output(L1, GPIO.HIGH)
			case 6:
				GPIO.output(L4a, GPIO.HIGH)
				GPIO.output(L4b, GPIO.HIGH)
				GPIO.output(L2a, GPIO.HIGH)
				GPIO.output(L2b, GPIO.HIGH)
				GPIO.output(L6, GPIO.HIGH)
		match die2:
			case 0:
				pass
			case 1:
				GPIO.output(R1, GPIO.HIGH)
			case 2:
				GPIO.output(R2, GPIO.HIGH)
			case 3:
				GPIO.output(R2, GPIO.HIGH)
				GPIO.output(R1, GPIO.HIGH)
			case 4:
				GPIO.output(R2, GPIO.HIGH)
				GPIO.output(R4, GPIO.HIGH)
			case 5:
				GPIO.output(R1, GPIO.HIGH)
				GPIO.output(R2, GPIO.HIGH)
				GPIO.output(R4, GPIO.HIGH)
			case 6:
				GPIO.output(R2, GPIO.HIGH)
				GPIO.output(R4, GPIO.HIGH)
				GPIO.output(R6, GPIO.HIGH)
		total = die1 + die2
		winThresh = 12 - winNo
		if total >= winNo:
			if total > (12 - (2*(winThresh/3))):
				outcome = 3
			elif total > (12 - (winThresh/3)):
				outcome = 2
			else:
				outcome = 1
		elif total <= lossNo:
			if total > (2*(lossNo/3)):
				outcome = -1
			elif total > (winThresh/3):
				outcome = -2
			else:
				outcome = -3
		else:
			outcome = 0
		return outcome
	def quietRoll(self, winNo, lossNo):
		die1 = random.randrange(1, 7)
		die2 = random.randrange(0, 7)
		'''
		insert lightshow here
		'''
		total = die1 + die2
		winThresh = 12 - winNo
		if total >= winNo:
			if total > (12 - (2*(winThresh/3))):
				outcome = 3
			elif total > (12 - (winThresh/3)):
				outcome = 2
			else:
				outcome = 1
		elif total <= lossNo:
			if total > (2*(lossNo/3)):
				outcome = -1
			elif total > (winThresh/3):
				outcome = -2
			else:
				outcome = -3
		else:
			outcome = 0
		return outcome
	def reset(self):
		resetLEDs()
	def cleanup(self):
		GPIO.cleanup()

if __name__ == "__main__":
	lightShow()
