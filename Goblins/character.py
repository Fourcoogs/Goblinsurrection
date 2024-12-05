#
# PROGRAM: character.py
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
import equipment
import traits
# import gui_support

#male and female names for each race
MANMALE = ["Robert", "Bartholomew", "Mortimer", "Stephen", "Thomas", "Rupert", "James", "William", 
		   "Garrett", "Borris", "Hugh", "Custis", "Morgan", "Arthur", "Kingsley", "Timothy", 
		   "Benjamin", "Michael", "Matthew", "Winston", "Terrence", "Lawrence", "Oliver", "Allistair",
		   "Geoff", "Thaddeus", "Marcus", "Ervrart"]
MANFEMALE = ["Lydia", "Emma", "Emilia", "Jessamine", "Esma", "Gwenneth", "Olivia", "Moira", 
			 "Maribeth", "Elizabeth", "Victoria", "Sophia", "Delilah", "Callista", "Annabeth",
			 "Lena"]
ELFMALE = ["Istuinaer", "Halvon", "Ganneldor", "Herion", "Adlegnir", "Ingion", "Echadion", 
		   "Gwaedhion", "Gweriion", "Cedhrion", "Duirronaer", "Aerdor", "Fingaerdir", "Naston", 
		   "Elhaelben", "Fingaeron", "Aderthion", "Faenion", "Northon", "Bruinaer", "Deliion", 
		   "Amarthedir", "Tyrion"]
ELFFEMALE = ["Galrien", "Taethadis", "Bornivel", "Pannil", "Suiladis", "Galrien", "Midhel", "Pangwen", 
			 "Duvaingwen", "Laingwen", "Penirien", "Eithrien", "Arwen", "Gaeralagosseth", "Gladhedis", 
			 "Lainien", "Calardassel", "Talvien", "Arradis", "Bastadis", "Ruthrriel", "Tegolien", 
			 "Bangwen", "Galadriel", "Ningannelwen"]
	#"Why" I hear you ask, "is 'Urist' in this list eleven times?"  Look up 'Urist' in the Dwarf Fortress wiki for
	# an answer
DWARFMALE = ["Aban", "Amost", "Ast", "Avuz", "Ber", "Bomrek", "Bëmbul", "Cerol", "Cilob", "Cog", 
			 "Dastot", "Datan", "Degël", "Ducim", "Dumed", "Dîshmab", "Etur", "Geshud", "Kadol", 
			 "Kikrost", "Kogsak", "Libash", "Mosus", "Nil", "Onol", "Stodir", "Tekkud", "Urdim", 
			 "Urist","Urist","Urist","Urist","Urist","Urist","Urist","Urist","Urist","Urist","Urist", 
			 "Zon", "Zutthan", "Èrith", "Ùshrir"]
DWARFFEMALE = ["Asën", "Athel", "Atír", "Ber", "Datan", "Deler", "Doren", "Edëm", "Etur", "Id", "Imush",
			   "Kadôl", "Kel", "Kosoth", "Kulet", "Likot", "Limul", "Logem", "Lolor", "Melbil", "Monom",
			   "Mörul", "Nish", "Onget", "Ral", "Rîsen", "Solon", "Thîkut", "Udib", "Urvad", "Uzol",
			   "Zas", "Zefon", "Zutthan", "Åblel", "Ònul"]
HIVERMALE = ["Ku", "Va", "Sik", "Ik", "Ems", "Tis", "Rem", "Ga"
	"Kul-Kut-Ku", "Kut-Ku", "Kul-Vat-Ik", "Kul-Emst-Sik", "Kul-Tist-Ku", "Kug-Tisl"
	"Ikt-Ku", "Ikl-Vat-Va", "Ikt-Sik", "Ikt-Ik", "Ikt-Ems", "Ikt-Tis", "Ikt-Rem", "Ikt-Ga"
	"Vag-Ku", "Val-Ikt", "Val-Vat-Ems", "Vat-Rem", "Vag-Gat"
	"Gag-Tisl-Tis", "Sikt-Ems"]
HIVERFEMALE = ["Etikosk", "Skimkat", "Kakatinsksa", "Sisk", "Umsist", "Sulsaket", "Tsinde", "Sheklind", "Haktuah",
			   "Igshekit"]
HOBBITMALE = ["Bilbo", "Frodo", "Samwise", "Peregrin", "Meriadoc", "Tomba", "Everard", "Bingo", "Bodo",
			  "Bungo", "Erling", "Ferdibrand", "Filibert", "Andwise", "Bandobras", "Gorbadoc", "Gormadoc",
			  "Longo", "Milo", "Saradoc", "Togo"]
HOBBITFEMALE = ["Rosemary", "Dahlia", "Marigold", "Lily", "Pansy", "Violet", "Amaranth", "Asphodel", 
				"Celandine", "Daisy", "Eglantine", "Lobelia", "Melilot", "Mentha", "Mimosa", "Myrtle",
				"Pearl", "Peony", "Pervinca", "Poppy", "Primrose", "Ruby"]
ORCMALE = ["Gortworg", "Agronak", "Bagdu", "Buramog", "Burz", "Dubok", "Dul", "Krognak", "Oghat", "Mug",
		   "Shagrol", "Shobob", "Shum", "Ulmug", "Urbul", "Ushnar", "Mongo", "Gashzug", "Morg", "Yamarz",
		   "Urgnok", "Ushnar", "Umum", "Kharag", "Ghorbash", "Ghamorz"]
ORCFEMALE = ["Agrob", "Badbog", "Bashuk", "Bogdub", "Bugdurash", "Bula", "Glasha", "Glob", "Gluronk", 
			 "Grat", "Grazob", "Gulfim", "Kharzug", "Lagakh", "Lambug", "Mogak", "Ulumpha", "Sloomalah"
			 "Urzul", "Yazgash"]
GOBLINMALE = ["Styx", "Byzuk", "Trazyn", "Caskyd", "Hexyn", "Bax", "Zak", "Rubyn", "Krakyn", "Rex",
			  "Haz", "Trykuk", "Zukhyn", "Ikyt", "Mystyd", "Horyd", "Tekyd", "Moon", "Gex", "Sexyn",
			  "Xakyd"]
GOBLINFEMALE = ["Styxo", "Byzukel", "Dymskel", "Haskel", "Caskel", "Baxo", "Hazo", "Krako", "Faxel",
				"Mistrel", "Ikyt", "Harzel", "Skel", "Anxel", "Anxo", "Starel", "Goldel", "Myndo", 
				"Kylo"]
OGRE = ["Gor", "Rek", "Sed", "Rog", "Kik", "Mok", "Sok", "Sek", "Nuk", "Ram", "Cob", "Hek", "Fik",
		"Rom", "Gom", "Sik", "Rig", "Gok", "Gek"]
KOBOLDMALE = ["Roaring-River", "Marches-Against-Darkness", "Almost", "Little-Fox", "Two-Bears-High-Fiving", 
			  "Horse-Master", "Wicked-Raid", "Stalwart-Protector", "He-Who-Knocks", "Red-Dawn"]
KOBOLDFEMALE = ["Tiger-Lily", "Skies-of-Flame", "Endless-Fields", "Herd-Guard"]

#last names for each race Note: only characters with Noble = True can have a last name
#Humans get their names from me taking a handful of British-sounding names (mostly from the 
#Dishonored series) and doing a bit of mixing and matching to make new ones
MANFAMS = ["Pendleton", "Pendelock", "Pendlethorn", "Pendsby", "Pendwell", "Pendle",
		   "Timsleton", "Timslethorn", "Timsby", "Timswell", "Timsh", "Timsel", 
		   "Curleton", "Curnow", "Curlock", "Curthorn", "Cursby", "Curwin", "Curwell", "Curh", "Curle",
		   "Havelton", "Havelock", "Havlethorn", "Havesby", "Havewell",
		   "Shackleton", "Shacklethorn", "Shacklesby", "Shacklewell", 
		   "Boyleton", "Boyelock", "Boylethorn", "Boyesby", "Boyle", 
		   "Brigsleton", "Brigsnow", "Brigslock", "Brigsthorn", "Brigsby", "Brigswell",
		   "Kaldwin", "Campbell", "Cromwell", "Ramsay"]
#I used a fantasy name generator to come up with names for elves because, if I'm being honest, 
#I don't care enough about the elves to give them more effort than this.  Last names come from 
#The Elder Scrolls, first names come from Lord of the Rings
ELFFAMS = ["Stormaine", "Jaeriane", "Silinihle", "Laretheus", "Aedahl", "Korkaender", "Thilinuseus", "Thramaire", 
		   "Elsiniath", "Thaoraine", "Chaeonin", "Kaeian", "Anaedaire", "Adosin", "Aedius", "Loraethkaender", 
		   "Larenhious", "Laraeththaer", "Jaeraen", "Thaorkaender", "Laemfhar"]
#Dwarves get their names from legends about their families and clans--I figured I'd leave it 
#up to interpretation how each family got its name.
DWARFFAMS = ["Stonehelm", "Stonefist", "Stonetooth", "Stoneshield", "Stoneaxe", "Stoneye", "Stoneater",
			 "Steelfist", "Steelhelm", "Steeltooth", "Steelshield", "Steelaxe", "Steeleye", "Steeleater",
			 "Goldtooth", "Goldenhelm", "Goldfist", "Goldenshield", "Goldenaxe", "Goldeneye", "Goldeater",
			 "Earthenshield", "Earthenhelm", "Earthenfist", "Earthtooth", "Earthenaxe", "Eartheneye", "Eartheater",
			 "Oakenaxe", "Oakenhelm", "Oakenfist", "Oaktooth", "Oakenshield", "Oakenaxe", "Oakeneye", "Oakeater",
			 "Shatterhelm", "Shatterfist", "Shattertooth", "Shattershield", "Shatteraxe",
			 "Deatheater", "Deathfist", "Deathshead",
			 "Godson", "Godeater", "Godfist"]
#Hivers get their names from me attempting to create the most unpronounceable words I can.  No vowels
#were purchased
HIVERFAMS = ["Tsndelmakr", "Tsndelgshel", "Tsndeltakr", "Tsndeldegr", "Tsndelsa",
			 "Krvdmakr", "Krvdgshel", "Krvdtakr", "Krvddegr", "Krvdsa",
			 "Mslmakr", "Mslgshel", "Msltakr", "Msldegr", "Mslsa",
			 "Etsmakr", "Etsgshel", "Etstakr", "Etsdegr", "Etssa"]
#Aside from female first names--which are all just names of plants--every Hobbit name comes from Lord of the 
#Rings.  That's all.  Copyright Infringement for the win, baby.
HOBBITFAMS = ["Baggins", "Bombodil", "Took", "Gamgee", "Proudfoot", "Brandybuck", "Fairbairn", "Greenhand",
			  "Hayward", "Boffin", "Mugwort", "Pott", "Puddifoot", "Roper", "Sackville", "Twofoot", 
			  "Underhill"]
#Orcs get their names from their families' greatest conquest/fortress, hence why some names are 
#partially derived from other races.  "Gro" means they sacked that place, "Gra" means they took and
#held land there, and "Ur" means that, for a time, they had complete control over that area
ORCFAMS = ["Gro-Hornburg", "Gro-Mistveil", "Gra-Stellengrad", "Ur-Tishkook", "Ur-Hobbiton", "Gro-Centria", 
		   "Gro-Graygold", "Gra-Vaewood", "Ur-Stonespire", "Gra-Media", "Ur-Ushnakh"]
GOBLINFAMS = ["Rakash", "Shakset", "Zagyk", "Silkul", "Yagaz", "Kelsun", "Totyk", "Shakyk", "Tokset", "Yalsun", 
			  "Zagash", "Rakyk", "Rakset", "Yagset", "Silset", "Silsyk", "Yagash", "Shakash"]
#There are no plans to give Ogres or Kobolds nobles, but I figured I may as well include these placeholders 
#just in case
OGREFAMS = ["Placeholder1", "Placeholder2"]
KOBOLDFAMS = ["Placeholder1", "Placeholder2"]

TOTALCHARS = 0

class Race:
	def __init__(self, relations = {}):
		self.relations = relations
		self.race = "raceName"
		self.description = "placeholder"
		self.attr = {"hmax":100, "damage":5, "ap":0, "armor":0, "agility":10, "morale":100}
		self.skills = {}
class Goblin(Race):
	def __init__(self, relations={"Player":0, "Dwarf":-25, "Orc":5, "Ogre":5, "Elf":-10, "Human":-10}):
		super().__init__(relations)
		self.race = "Goblin"
		self.attr = {"hmax":70, "agility":15}
		self.mprefs = ["Slum Lord"]
		self.fprefs = ["Slum Lady"]
class Orc(Race):
	def __init__(self, relations={"Player":0, "Human":-10, "Elf":-25, "Dwarf":-5}):
		super().__init__(relations)
		self.race = "Orc"
		self.attr = {"damage":8, "agility":7}
		self.mprefs = ["High Chief", "Chieftan", "Warlord"]
		self.fprefs = ["High Chiefess", "Chieftess", "Warlord","Black Witch"]
class Ogre(Race):
	def __init__(self, relations={"Player":0, "Dwarf":-20, "Hiver":-20}):
		super().__init__(relations)
		self.race = "Ogre"
		self.attr = {"hmax":150, "damage":15, "agility":5, "morale":60}
class Human(Race):
	def __init__(self, relations={"Player":0, "Orc":-10, "Ogre":-15, "Elf":10, "Hobbit":15, "Dwarf":15}):
		super().__init__(relations)
		self.race = "Human"
		self.mprefs = ["Lord", "Duke", "Baron", "Count"]
		self.fprefs = ["Madame", "Duchess", "Baroness", "Countess"]
class Dwarf(Race):
	def __init__(self, relations={"Player":0, "Goblin":-5, "Orc":-15, "Kobold":-5, "Ogre":-20, "Elf":-1, "Human":15, "Hobbit":10, "Hiver":-25}):
		super().__init__(relations)
		self.race = "Dwarf"
		self.attr = {"hmax":110, "agility":6}
		self.mprefs = ["Axelord", "High Mason", "Lord of Iron"]
		self.fprefs = ["Axelord", "High Mason", "Lady of Iron"]
class Hobbit(Race):
	def __init__(self, relations={"Player":0}):
		super().__init__(relations)
		self.race = "Hobbit"
		self.attr = {"agility":11}
		self.mprefs = ["Mayor", "Mister"]
		self.fprefs = ["Mayor", "Missus", "Miss"]
class Hiver(Race):
	def __init__(self, relations={"Player":0, "Goblin":-5, "Dwarf":-25, "Kobold":-30, "Elf":-5, "Human":10}):
		super().__init__(relations)
		self.race = "Hiver"
		self.attr = {"hmax":70, "armor":1}
		self.fprefs = ["Petty Queen"]
class Kobold(Race):
	def __init__(self, relations={"Player":0, "Hiver":-30, "Elf":-20, "Dwarf":-10}):
		super().__init__(relations)
		self.race = "Kobold"
class Elf(Race):
	def __init__(self, relations={"Player":0, "Elf":10, "Orc":-25, "Human":5, "Goblin":-10, "Ogre":-10}):
		super().__init__(relations)
		self.race = "Elf"
		self.mprefs = ["Woodslord", "Elder", "High Seer"]
		self.fprefs = ["Earth Mother", "High Seeress", "Elder"]

RACES = {"Goblin":Goblin(), "Orc":Orc(), "Ogre":Ogre(), "Human":Human(), "Dwarf":Dwarf(), "Hiver":Hiver(), 
		"Hobbit":Hobbit(), "Elf":Elf(), "Kobold":Kobold()}

def loadRaces(list):
	global RACES
	RACES = list

def findRace(raceName):
		for i in RACES:
			if i == raceName:
				return RACES[i]

class Character:
	# __init__ variables passed
	#
	# race: a touple containing one or more strings to define the character's race
	# sex: a string which can be either blank, "male", or "female"
	# noble: a boolean which defines if the character is a noble (True) or not (False)
	# firstName: a string which can be either blank (random) or filled in
	# lastName: a string which can be either blank (random) or filled in
	def __init__(self, race, sex, noble, firstName, lastName, location = 0):
		global TOTALCHARS
		self.race = race
		self.noble = noble
		self.location = location
		#this statement determines a character's sex if it's been left randomized
		match sex:
			case "":
				match self.race:
					case "Hiver":
						#for lore reasons, male Hivers will always be commoners and 
						#females will always be nobles
						match self.noble:
							case False:
								self.sex = "male"
							case True:
								self.sex = "female"
					case __:
						self.sex = random.choice(("male", "female"))
			case "male":
				self.sex = sex
			case "female":
				self.sex = sex
			case __:
				print("Error: invalid sex")
		#this statement determines a character's name if it's been randomized
		match firstName:
			case "":
				match self.race:
					#the randomization could be done more efficiently, but I 
					#don't want to change anything rn
					case "Human":
						match self.sex:
							case "male":
								i = random.randrange(0, len(MANMALE))
								self.firstName = MANMALE[i]
							case "female":
								i = random.randrange(0, len(MANFEMALE))
								self.firstName = MANFEMALE[i]
					case "Elf":
						match self.sex:
							case "male":
								i = random.randrange(0, len(ELFMALE))
								self.firstName = ELFMALE[i]
							case "female":
								i = random.randrange(0, len(ELFFEMALE))
								self.firstName = ELFFEMALE[i]
					case "Dwarf":
						match self.sex:
							case "male":
								i = random.randrange(0, len(DWARFMALE))
								self.firstName = DWARFMALE[i]
							case "female":
								i = random.randrange(0, len(DWARFFEMALE))
								self.firstName = DWARFFEMALE[i]
					case "Hiver":
						match self.sex:
							case "male":
								i = random.randrange(0, len(HIVERMALE))
								self.firstName = HIVERMALE[i]
							case "female":
								i = random.randrange(0, len(HIVERFEMALE))
								self.firstName = HIVERFEMALE[i]
					case "Hobbit":
						match self.sex:
							case "male":
								i = random.randrange(0, len(HOBBITMALE))
								self.firstName = HOBBITMALE[i]
							case "female":
								i = random.randrange(0, len(HOBBITFEMALE))
								self.firstName = HOBBITFEMALE[i]
					case "Orc":
						match self.sex:
							case "male":
								i = random.randrange(0, len(ORCMALE))
								self.firstName = ORCMALE[i]
							case "female":
								i = random.randrange(0, len(ORCFEMALE))
								self.firstName = ORCFEMALE[i]
					case "Goblin":
						match self.sex:
							case "male":
								i = random.randrange(0, len(GOBLINMALE))
								self.firstName = GOBLINMALE[i]
							case "female":
								i = random.randrange(0, len(GOBLINFEMALE))
								self.firstName = GOBLINFEMALE[i]
					case "Ogre":
						self.firstName = random.choice(OGRE)
					case "Kobold":
						match self.sex:
							case "male":
								i = random.randrange(0, len(KOBOLDMALE))
								self.firstName = KOBOLDMALE[i]
							case "female":
								i = random.randrange(0, len(KOBOLDFEMALE))
								self.firstName = KOBOLDFEMALE[i]
			case __:
				self.firstName = firstName		
		#this statement determines a character's last name if it's been left
		#randomized
		#Fun fact: only nobles can have last names, as medieval nobility is the source of 
		#modern-day last names--non-nobles later on adopted the names of their
		#crafts as their family names, which is why so many people are named "Baker"
		#or "Smith" (and also the reason why I haven't included those names in any list)
		match lastName:
			case "":
				match noble:
					case True:
						match self.race:
							case "Human":
								i = random.randrange(0, len(MANFAMS))
								self.lastName = MANFAMS[i]
							case "Elf":
								i = random.randrange(0, len(ELFFAMS))
								self.lastName = ELFFAMS[i]
							case "Dwarf":
								i = random.randrange(0, len(DWARFFAMS))
								self.lastName = DWARFFAMS[i]
							case "Hiver":
								i = random.randrange(0, len(HIVERFAMS))
								self.lastName = HIVERFAMS[i]
							case "Hobbit":
								i = random.randrange(0, len(HOBBITFAMS))
								self.lastName = HOBBITFAMS[i]
							case "Orc":
								i = random.randrange(0, len(ORCFAMS))
								self.lastName = ORCFAMS[i]
							case "Goblin":
								i = random.randrange(0, len(GOBLINFAMS))
								self.lastName = GOBLINFAMS[i]
							#The game is planned to never generate Ogre or Kobold families,
							#these lines of code exist solely in case that ever changes
							case "Ogre":
								i = random.randrange(0, len(OGREFAMS))
								self.lastName = OGREFAMS[i]
							case "Kobold":
								i = random.randrange(0, len(KOBOLDFAMS))
								self.lastName = KOBOLDFAMS[i]
					case False:
						self.lastName = lastName
			case __:
				self.lastName = lastName
		#skills: a map of five integers connected to "fight", "stealth", "speech", "finance",
		#		and "learning"
		#the following represent the bare minimum skills that any character can possess
		self.skills = {"fight":1, "stealth":1, "speech":1, "learning":1, "management":1}
		# attr: a map of five integers connected to "health", "damage", "ap" (AKA: "Armor-Piercing"), 
		#		"agility", and "morale"
		#the following represents the standard attributes of any character who doesn't have equipment,
		#	traits, etc.
		self.equip = {"weapon":equipment.Empty(), "armor":equipment.Empty(), "misc":[equipment.Empty()]} #emptying equipment slots
		self.nickname = False
		self.history = {"kills":[], "helps":[], "saves":[]}
		self.traits = []
		self.relationships = {"ally":[], "enemy":[], "friend":[]}
		self.id = "char" + str(TOTALCHARS)
		TOTALCHARS += 1
		self.theRace = findRace(self.race)
		self.attr = {"hmax":100, "damage":5, "ap":0, "armor":0, "agility":10, "morale":100}
		self.setAttr(self.theRace.attr)
		self.attr["health"] = self.attr["hmax"]
		self.attr["courage"] = self.attr["morale"]
		return
	def updateStats(self, update={}):
		for i in update:
			if i in self.skills:
				self.skills[i] += update[i]
			if i in self.attr:
				self.attr[i] += update[i]
		return True
	def setEquip(self, stuff):
		removed = []
		for i in stuff:
			if i == "misc":
				for n in self.equip[i]:
					removed.append(n)
			else:
				removed.append(self.equip[i]) # placing whatever is currently equipped in the appropriate spot into the greater owned item pool
				uneq = self.equip[i].unEq()
				self.updateStats(uneq) # removing the effects of the unequipped item
				self.equip[i] = stuff[i] # replacing the unequipped item
				activate = self.equip[i].activate()
				self.updateStats(activate) # acquiring the effects of the newly-equipped item(s)
		return removed # returning the list of unequipped items to be added to the greater owned item pool
	def setSkills(self, skills):
		for i in skills:
			self.skills[i] = skills[i]
		return True
	def setAttr(self, attr):
		for i in attr:
			self.attr[i] = attr[i]
		return True
	def setHistory(self, histAdds={}):
		for i in histAdds:
			for o in histAdds[i]:
				self.history[i].append(o)
		return True
	def getHistory(self):
		return self.history
	def addTraits(self, newTraits=[]):
		for i in newTraits:
			dupe = False
			for j in self.traits:
				if i == j:
					dupe = True
			if dupe == False:
				self.traits.append(i)
				stats, relMods = i.activate()
				self.updateStats(stats)
				self.updateBeliefs(relMods)
		return True
	def updateTraits(self):
		for i in range(0, len(self.traits)):
			update = self.traits[i].update(self.getInfo())
			match update[0]:
				case True: 
					if len(update[1]) > 0:
						self.updateStats(update(1))
				case "newTrait":
					newTrait = traits.traitId(update[0])
					self.addTraits(newTrait)
				case "replace":
					newTrait = traits.traitId(update[0])
					self.addTraits(newTrait)
					stats, belMods = self.traits[i].unEq()
					self.updateStats(stats)
					self.updateBeliefs(belMods)
					del self.traits[i]
				case False:
					stats, belMods = self.traits[i].unEq()
					self.updateStats(stats)
					self.updateBeliefs(belMods)
					del self.traits[i]
		return True
	def giveOpinions(self, other, score = 0):
		if other in self.relationships["ally"]:
			score += 10
		elif other in self.relationships["enemy"]:
			score += -10
		if self in other.history["saves"]:
			score += 20
		if self in other.history["helps"]:
			score += 10
		temp = other.traits
		theirTraits = []
		for i in temp:
			theirTraits.append(i.save())
		theirRace = other.race
		for u in self.relationships["ally"]:
			if u in other.history["kills"]:
				score += -10
			elif u in other.history["saves"]:
				score += 10
			elif u in other.history["helps"]:
				score += 5
		for y in self.relationships["enemy"]:
			if y in other.history["kills"]:
				score += 10
			elif y in other.history["saves"]:
				score += -10
			elif y in other.history["helps"]:
				score += -5
		return score
	def giveClass(self):
		highest = 0
		for i in self.skills:
			if self.skills[i] > highest:
				highest = self.skills[i]
				name = i
		passable = name + " (" + str(highest) + ")"
		return passable
	def getInfo(self):
		return (self.race, self.sex, self.noble, self.firstName, self.lastName, self.skills, 
		  self.attr, self.equip, self.nickname, self.history, self.traits)
	def save(self):
		match self.race:
			case "Goblin":
				race = "G"
			case "Orc":
				race = "O"
			case "Ogre":
				race = "R"
			case "Dwarf":
				race = "D"
			case "Human":
				race = "M"
			case "Hiver":
				race = "H"
			case "Kobold":
				race = "K"
			case "Elf":
				race = "E"
			case "Hobbit":
				race = "B"
		if self.sex == "male":
			sex = "m"
		else:
			sex = "f"
		if self.noble == True:
			noble = 1
			self.savetag = self.id + "_"+race+"_"+sex+"_"+noble+"_"+self.firstName+"_"+self.lastName
		else:
			noble = 0
			self.savetag = self.id + "_"+race+"_"+sex+"_"+noble+"_"+self.firstName
		skills = ""
		for i in self.skills:
			skills += i + str(self.skills[i])
		attr = ""
		for o in self.attr:
			attr += o + str(self.attr[o])
		equip = ""
		for u in self.equip:
			if u == "misc":
				for v in self.equip[u]:
					equip += self.equip[u][v].save()
			else:
				equip += self.equip[u].save()
			equip += "_"
		self.savetag += "_"+skills+"_"+attr+"_"+equip+self.nickname+"_"
		history = ""
		for y in self.history:
			history += y
			for z in self.history[y]:
				history += z.id
		self.savetag += history+"_"
		myTraits = ""
		for a in self.traits:
			myTraits += a.save + "_"
		self.savetag += myTraits
		return self.savetag

class Goal:
	def __init__(self, task, target, type = "open", priority = 2):
		# what specifically the character wants to accomplish.  Several types of tasks:
		# "kill": a person or race that this character wants to kill
		# "protect": a person, place, or race that this character wants to keep safe
		# "expel": a race this character wants to remove from the kingdom
		# "obey": a person whose goals this character wants to follow--will override 
		# 		other goals of equal or lower priority when triggered
		# "conquer": a place this character wants to have filled with members of their race
		self.task = task 
		# reference to a character, region, or string descriptor of a race
		self.target = target 
		# how open the character is in trying to accomplish this.  Comes in
		# three levels:
		# "secret": character will not directly act upon this without the player's help
		# "subtle": character will use less extreme means to accomplish this
		# "open": character will directly do this when prompted
		self.type = type 
		# integer with three levels corresponding to how frequently the character will 
		# attempt to achieve their goal.  Frequency is defined as 100%/priority, so a
		# priority of 1 will be attempted every turn, priority of 2 will have a 50%
		# chance of being attempted every turn, etc.
		self.priority = priority

class Leader(Character):
	def __init__(self, race, sex, noble, firstName, lastName, location, goals=[], prefix = None, suffix = None):
		super().__init__(race, sex, noble, firstName, lastName, location)
		self.goals = goals
		self.prefix = prefix
		self.suffix = suffix
		self.id = "lead" + str(TOTALCHARS)
	def addGoal(self, tasks):
		for i in range(0, len(tasks)):
			if tasks[i][1] == "self":
				tasks[i][1] = self
			match len(tasks[i]):
				case 2:
					self.goals.append(Goal(tasks[i][0], tasks[i][1]))
				case 3:
					self.goals.append(Goal(tasks[i][0], tasks[i][1], tasks[i][2]))
				case 4:
					self.goals.append(Goal(tasks[i][0], tasks[i][1], tasks[i][2], tasks[i][3]))
		return
	def getInfo(self):
		return (self.race, self.sex, self.noble, self.firstName, self.lastName, self.skills, 
		  self.attr, self.equip, self.nickname, self.history, self.traits, self.goals)
	def save(self):
		super().save()
		#unfinished
		return self.savetag

class Player(Character):
	def __init__(self, race, sex, noble, firstName, lastName, location=0):
		super().__init__(race, sex, noble, firstName, lastName, location)

# if __name__ == "__main__":
# 	gui_support.main()