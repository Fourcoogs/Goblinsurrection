#
# PROGRAM: combat.py
#
# Version: 0.1
#
# COURSE: COSC 3143-01
# AUTHOR: Will Berger
# ASSIGNMENT: Main Project ("Goblinsurrection")
# PURPOSE: ...
# DEPENDENCIES: character.py, dice.py
# Operational Status: WIP
#
import random
import character

class Combat:
	# this initialization method is primarily used to get the two teams ordered
	def __init__(self, player, opps):
		# these are the two teams: "player" and "opps", AKA player and opponents
		print("Initialization started")
		self.opps = []
		self.player = []
		# this is a list of each character sorted in order of agility--player team is 
		# favored if two characters have the same amount of agility
		# 0: the pointer to the character in question
		# 1: Boolean for "character is on the player's team" True or False
		# 2: Boolean for "character is still active" (i.e. alive and has neither fled nor surrendered) 
		# 		True or False
		lineup = [] 
		for i in opps:
			match len(lineup):
				case 0:
					lineup.append([i, False, True])
				case __:
					count = 0
					for e in lineup:
						if i.attr["agility"] >= e[0].attr["agility"]:
							lineup.insert(count, [i, False, True])
							break
						elif count == (len(lineup) - 1):
							lineup.append([i, False, True])
							break
						count += 1
		for o in player:
			count = 0
			for u in lineup:
				if o.attr["agility"] >= u[0].attr["agility"]:
					lineup.insert(count, [o, True, True])
					break
				elif count == (len(lineup) - 1):
					lineup.append([o, True, True])
					break
				count += 1
		self.lineup = lineup
		self.player = []
		self.opps = []
		for i in self.lineup:
			if i[1] == True:
				self.player.append(i)
			else:
				self.opps.append(i)
		self.base = 6 # base difficulty for landing an attack--if two opponents are evenly matched, they have a 50% chance of landing a hit
		self.iteration = 0
	def runTurn(self):
		# Updating the health statuses of all characters on the field
		for h in range(0, len(self.lineup)):
			if self.lineup[h][0].attr["health"] <= 0:
				self.lineup[h][2] = False
		# Checking to see if the opponents are still on the field
		count = 0
		for i in self.opps:
			if i[2] == False:
				count += 1
				if count >= len(self.opps):
					return True
		# Checking to see if the player team is still on the field
		count = 0
		for j in self.player:
			if j[2] == False:
				count += 1
				if count >= len(self.player):
					return False
		# Iterating through the lineup until reaching the next active participant
		while True:
			if self.iteration >= len(self.lineup):
				self.iteration = 0
			if self.lineup[self.iteration][2] == True:
				self.iteration += 1
				return (self.lineup[self.iteration-1])
			self.iteration += 1
	def retreat(self, coward):
		self.iteration.remove(coward)
		if coward in self.player:
			self.player.remove(coward)
		else:
			self.opps.remove(coward)
		return True
	def plotStealth(self, attacker, defender):
		difficulty = self.base - (attacker[0].skills["stealth"] - defender[0].skills["stealth"])
		if (12 - difficulty) < 1:
			difficulty = 11
		match attacker[0].equip["weapon"].id:
			case "d1":
				damage = attacker[0].attr["damage"]*(1 + (attacker[0].skills["fight"])/10)*(4)
			case "d2":
				damage = attacker[0].attr["damage"]*(1 + (attacker[0].skills["fight"])/10)*(4)
			case "d0":
				damage = attacker[0].attr["damage"]*(1 + (attacker[0].skills["fight"])/10)*(4)
			case __:
				damage = attacker[0].attr["damage"]*(1 + (attacker[0].skills["fight"])/10)*(2) - defender[0].attr["armor"]
		return (difficulty, damage)
	def plotAttack(self, attacker, defender):
		difficulty = self.base - (attacker[0].skills["fight"] - defender[0].skills["fight"])
		if (12 - difficulty) < 1:
			difficulty = 11
		elif difficulty < 1:
			difficulty = 1
		baseDam = attacker[0].attr["damage"]*(1 + (attacker[0].skills["fight"])/10) - defender[0].attr["armor"]
		if baseDam < 0:
			baseDam = 0
		medDam = baseDam + attacker[0].attr["ap"]
		minDam = (baseDam + attacker[0].attr["ap"])/2
		maxDam = (baseDam + attacker[0].attr["ap"])*2
		return (difficulty, minDam, medDam, maxDam)
	def launchAttack(self, attacker, defender, damage, hit=True):
		if hit == True:
			defender[0].updateStats({"health":-damage})
			if (defender[0].attr["health"]-damage) <= 0:
				defender[2] = False
				attacker[0].setHistory({"kills":[defender[0]]})
		return True