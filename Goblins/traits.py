#
# PROGRAM: traits.py
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

class Base:
	def __init__(self):
		self.name = "Base_Trait"
		self.desc = "This acts as flavor text to describe the trait"
		self.stats = {} # what skills and attributes this trait adds to or removes from
		self.values = {} # relationship modifiers that this trait adds to or removes from
		self.id = "Not Applicable"
		return
	# this method checks to see if a info is elligible to receive it, returning either
	# True or False.  Any traits like this one that aren't passed through specific actions on 
	# the player's end will automatically return False
	# Note: this method is one of the only ones that is meant to be called exclusively by the
	# main program rather than the character itself
	def parameters(self, info):
		return False
	# used for keeping track of the conditions of a temporary trait.  Returns True if the
	# trait can still be kept and False if its time is up
	def update(self, info):
		return (True, {})
	def relMod(self, uinfo, tinfo):
		score = 0
		return score
	def activate(self):
		return self.stats, self.values
	def unEq(self):
		for i in self.stats:
			self.stats[i]=-self.stats[i]
		for o in self.values:
			self.values[o]=-self.values[o]
		return self.stats, self.values
	def save(self):
		return self.id

class Rizz_1(Base): #r1
	def __init__(self):
		self.name = "Empathetic"
		self.desc = "This character possesses an above-average understanding of social cues"
		self.stats = {"speech":3}
		self.values = {}
		self.id = "r1"
	def parameters(self, info):
		return super().parameters(info)
	def update(self, info):
		return super().update(info)
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Wound_1(Base): #w1
	def __init__(self):
		self.name = "Mild Injury"
		self.desc = "'Tis a flesh wound"
		self.stats = {}
		self.values = {}
		self.id = "w1"
	def parameters(self, info):
		vals = info[6]
		if vals["health"] < vals["hmax"] & vals["health"] >= (vals["hmax"]*0.85):
			return True
		else:
			return False
	def update(self, info):
		vals = info[6]
		if (vals["health"]+ (vals["hmax"]*10)) >= vals["hmax"]:
			return False
		else:
			return (True, {"health":(vals["hmax"]*0.1)})
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Dumb_1(Base): #d1
	def __init__(self):
		self.name = "Dullard"
		self.desc = "Learning is not this character's strongsuit"
		self.stats = {"learning":-3}
		self.values = {}
		self.id = "d1"
	def parameters(self, info):
		return super().parameters(info)
	def update(self, info):
		return super().update(info)
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Kill_1(Base): #k1
	def __init__(self):
		self.name = "First Blood"
		self.desc = "This individual has crossed the line and become a killer"
		self.stats = {"fight":2}
		self.values = {}
		self.id = "k1"
	def parameters(self, info):
		if len(info[9]["Kills"]) == 1:
			return True
		else:
			return False
	def update(self, info):
		if len(info[9]["Kills"]) > 1:
			return False
		else:
			return (True, {})
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Kill_2(Base): #k2
	def __init__(self):
		self.name = "Bloodied"
		self.desc = "This person's hands are stained with the blood of enemies past"
		self.stats = {"fight":4}
		self.values = {}
		self.id = "k2"
	def parameters(self, info):
		kills = len(info[9]["kills"])
		if kills > 1 & kills <= 3:
			return True
		else:
			return False
	def update(self, info):
		if len(info[9]["kills"]) > 3:
			return False
		else: return (True, {})
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Kill_3(Base): #k3
	def __init__(self):
		self.name = "Experienced Killer"
		self.desc = "This person is numb to the sensation of taking a life"
		self.stats = {"fight":8}
		self.values = {}
		self.id = "k3"
	def parameters(self, info):
		value = info[9]["kills"]
		if len(value) >= 4:
			return True
		else: return False
	def update(self, info):
		return super().update(info)
	def relMod(self, uinfo, tinfo):
		return super().relMod(uinfo, tinfo)
	def activate(self):
		return super().activate()
	def unEq(self):
		return super().unEq()
	def save(self):
		return super().save()

class Ashamed_1(Base): #a1
	def __init__(self):
		super().__init__()
		self.name = "Ashamed"
		self.desc = "This character feels ashamed after violating their beliefs"
		self.stats = {"morale":-20}
		self.id = "a1"
	
class Hate_k(Base): #hk
	def __init__(self):
		super().__init__()
		self.name = "Hates killing"
		self.desc = "This character is fundamentally opposed to killing in all forms"
		self.id = "hkill"
	def update(self, info):
		if len(info[9]["kills"]) > 0:
			verdict = random.choice((True, False))
			if verdict == True:
				for i in info[10]:
					if isinstance(i, Ashamed_1):
						break
				else: 
					return ("newTrait", "a1")
			else:
				return False
		return (True, {})
	def relMod(self, uinfo, tinfo):
		score = -10 * len(tinfo[9]["kills"])
		return score

class PlayBase(Base):
	def __init__(self):
		super().__init__()
class Player_slave(PlayBase): #ps
	def __init__(self):
		super().__init__()
		self.stats = {"agility":5}
		self.name = "Escaped Slave"
		self.desc = "You, alongside several others, escaped from bondage to make it to this point"
		self.id = "ps"
class Player_nomad(PlayBase): #pn
	def __init__(self):
		super().__init__()
		self.stats = {"hmax":10}
		self.name = "Nomad"
		self.desc = "You spent several years of your life wandering the planes of Elden, establishing relationships with its Kobold tribes and learning to survive in the wilderness."
		self.id = "pn"

TRAIT_IDS = {"pn":Player_nomad(), "ps":Player_slave(), "hkill":Hate_k(), "a1":Ashamed_1, "k3":Kill_3(),"k2":Kill_2(), 
			 "k1":Kill_1(), "d1":Dumb_1(), "w1":Wound_1(), "r1":Rizz_1()}

def traitId(ids, info = None):
	global TRAIT_IDS
	theTraits = []
	for i in ids:
		theTraits.append(TRAIT_IDS[i])
	if info is not None:
		info.addTrait(theTraits)
		return
	else:
		return theTraits	

