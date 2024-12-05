#
# PROGRAM: characterCreator.py
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
from character import Character
import equipment
import random
import traits

class Reg:
	def __init__(self):
		pass
	def skills(self):
		skills = self.guy.skills
		skpts = 30
		for i in skills:
			num = random.randrange(0, skpts+1)
			skills[i] += num
			skpts += -num
			if skpts <= 0:
				break
		self.guy.setSkills(skills)
		return
	def equipment(self):
		return
	def traits(self):
		return
	def names(self):
		return
	def make(self, raceList="Human", sex="", noble = ""):
		if noble != True and noble != False and raceList != "Ogre" and raceList != "Kobold":
			num = random.randrange(1, 101)
			if num > 10:
				noble = False
			else:
				noble = True
		elif noble != True and noble != False and raceList == "Ogre" or raceList == "Kobold":
			noble = False
		self.guy = Character(raceList, sex, noble, "", "")
		self.skills()
		self.equipment()
		self.traits()
		self.names()
		return self.guy
	
class Watchman(Reg):
	def __init__(self):
		super().__init__()
	def skills(self):
		skills = {"fight":5, "stealth":4, "speech":4}
		self.guy.setSkills(skills)
		return
	def equipment(self):
		equip = {"armor":equipment.WatchGarb(), "weapon":equipment.Baton()}
		self.guy.setEquip(equip)
		return
	def traits(self):
		return super().traits()
	def names(self):
		self.guy.nickname = self.guy.race+" Watchman"
		return
	def make(self, raceList, sex, noble=""):
		return super().make(raceList, sex, noble)
	
class WatchmanVet(Reg):
	def __init__(self):
		super().__init__()
	def skills(self):
		skills = {"fight":8, "stealth":6, "speech":6, "management":8}
		self.guy.setSkills(skills)
		return
	def equipment(self):
		equip = {"armor":equipment.WatchCoat(), "weapon":equipment.Baton()}
		self.guy.setEquip(equip)
		return
	def traits(self):
		return super().traits()
	def names(self):
		self.guy.nickname = self.guy.race+" Veteran Watchman"
		return
	def make(self, raceList, sex, noble=""):
		return super().make(raceList, sex, noble)

class Soldier(Reg):
	def names(self):
		self.guy.nickname = self.guy.race+" Soldier"
		return
	def equipment(self):
		equip = {"weapon":equipment.Sword_1(), "armor":equipment.MilitaryVest()}
		self.guy.setEquip(equip)
		return
	def skills(self):
		skills = {"fight":25, "stealth":16, "speech":20}
		self.guy.setSkills(skills)
		return
	
class Captain(Reg):
	def names(self):
		self.guy.nickname = self.guy.race+" Officer"
		return
	def equipment(self):
		equip = {"weapon":equipment.Mace_1(), "armor":equipment.MilitaryCuirass()}
		self.guy.setEquip(equip)
		return
	def skills(self):
		skills = {"fight":50, "stealth":35, "speech":50, "management":45}
		self.guy.setSkills(skills)
		return

class Knight(Reg):
	def names(self):
		self.guy.nickname = self.guy.race+" Knight"
	def equipment(self):
		equip = {"weapon":equipment.Mace_2(), "armor":equipment.MilitaryKnight()}
		self.guy.setEquip(equip)
	def skills(self):
		skills = {"fight":60, "stealth":10, "speech":30}
		self.guy.setSkills(skills)
		return
	
# if __name__ == '__main__':
# 	gui_support.main()