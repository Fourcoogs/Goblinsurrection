#
# PROGRAM: equipment.py
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

class Empty:
	def __init__(self):
		self.name = "empty"
		self.desc = "empty"
		self.stats = {}
		self.type = "empty"
		self.id = "empty"
	def activate(self):
		return self.stats
	def unEq(self):
		for i in self.stats:
			self.stats[i]=-self.stats[i]
		return self.stats
	def save(self):
		return self.id

class Baton(Empty): #b1
	def __init__(self):
		self.name = "Baton"
		self.desc = "placeholder"
		self.stats = {"damage":10, "ap":1}
		self.type = "weapon"
		self.id = "b1"
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	
class WatchGarb(Empty): #wa1
	def __init__(self):
		self.name = "Watchman's Garb"
		self.desc = "placeholder"
		self.stats = {"armor":2}
		self.type = "armor"
		self.id = "wa1"
	def activate(self):
		return super().activate()

	def unEq(self):
		return super().unEq()
	
class WatchCoat(Empty): #wa2
	def __init__(self):
		self.name = "Watch Uniform"
		self.desc = "placeholder"
		self.stats = {"armor":3}
		self.type = "armor"
		self.id = "wa2"
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()

class Sword_1(Empty):
	def __init__(self):
		self.name = "Shortsword"
		self.desc = "placeholder"
		self.stats = {"damage":20}
		self.type = "weapon"
		self.id = "s1"
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
class MilitaryVest(Empty): #sa1
	def __init__(self):
		super().__init__()
		self.name = "Military Vest"
		self.stats = {"armor":10, "agility":-2}
		self.type = "armor"
		self.id = "sa1"
class MilitaryCuirass(Empty): #sa2
	def __init__(self):
		super().__init__()
		self.name = "Officer's Cuirass"
		self.stats = {"armor":25, "agility":-10}
		self.type = "armor"
		self.id = "sa2"
class MilitaryKnight(Empty): #sa3
	def __init__(self):
		super().__init__()
		self.name = "Knightly Armor"
		self.stats = {"armor":50, "agility":-15, "stealth":-20}
		self.type = "armor"
		self.id = "sa3"
class LightCuirass(Empty): #pa1
	def __init__(self):
		super().__init__()
		self.name = "Light Cuirass"
		self.type = "armor"
		self.stats = {"armor":6}
class HeavyCuirass(Empty): #pa2
	def __init__(self):
		super().__init__()
		self.name = "Heavy Cuirass"
		self.stats = {"armor":20, "agility":-8}
		self.type = "armor"
		self.id = "pa2"
class Mace_1(Empty): #m1
	def __init__(self):
		super().__init__()
		self.name = "Iron Mace"
		self.stats = {"damage":15, "ap":10}
		self.type = "weapon"
		self.id = "m1"
class Mace_2(Empty): #m2
	def __init__(self):
		super().__init__()
		self.name = "Steel Mace"
		self.stats = {"damage":35, "ap":30, "agility":-5}
		self.type = "weapon"
		self.id = "m2"
class Sword_2(Empty): #s2
	def __init__(self):
		super().__init__()
		self.name = "Longsword"
		self.stats = {"damage":50}
		self.type = "weapon"
		self.id = "s2"
class Dagger_1(Empty): #d1
	def __init__(self):
		super().__init__()
		self.name = "Concealable Blade"
		self.stats = {"damage":10}
		self.type = "weapon"
		self.id = "d1"
class Dagger_2(Empty): #d2
	def __init__(self):
		super().__init__()
		self.name = "Assassin's Dagger"
		self.type = "weapon"
		self.stats = {"damage":20}
		self.id = "d2"
class Dagger_0(Empty): #d0
	def __init__(self):
		super().__init__()
		self.name = "Rusty Shiv"
		self.type = "weapon"
		self.stats = {"damage":5}

EQUIPIDS = {"empty":Empty(), "b1":Baton(), "wa1":WatchGarb(), "wa2":WatchCoat(), "s1":Sword_1(), "sa1":MilitaryVest(), 
			"sa2":MilitaryCuirass(), "sa3":MilitaryKnight(), "m1":Mace_1(), "m2":Mace_2, "s2":Sword_2, "d1":Dagger_1(),
			"d2":Dagger_2, }

def findEquip(ids):
	equiplist = []
	for i in ids:
		if i in EQUIPIDS:
			equiplist.append(EQUIPIDS[i])
	return equiplist