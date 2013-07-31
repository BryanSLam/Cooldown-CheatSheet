#Take in user input 
#Enemy line up
#Optional summoner spells
#Buff timers?
import sys

class Hero(object):
	def __init__(self, name, cd1, cd2, cd3):
		self.name = name
		self.cd1 = cd1
		self.cd2 = cd2
		self.cd3 = cd3
		
database = {"Ahri": (110, 95, 80), "Akali": (2, 1.5, 1), "Alistar": (120, 100, 80),
"Amumu": (150,130,110), "Anivia": (6,6,6), "Annie" : (120,120,120), "Ashe" : (100,90,80),
"Blitzcrank": (30,30,30}
		

		
print "Main Menu"
menuSelection = 0
while(menuSelection != '3'):
	print "1: Input team line up"
	print "2: Summoner spell reference"
	print "3: Quit"
	menuSelection = raw_input('>> ')
	
	if (menuSelection == '1'):
		hero1 = raw_input('1:').capitalize()
		hero2 = raw_input('2:').capitalize()
		hero3 = raw_input('3:').capitalize()
		hero4 = raw_input('4:').capitalize()
		hero5 = raw_input('5:').capitalize()
		print "\n"
		print "Enemy Line up\n"
	
		print hero1 + ":", database[hero1][0], database[hero1][1], database[hero1][2]
		print "\n"
		print hero2 + ":", database[hero2][0], database[hero2][1], database[hero1][2]
		print "\n"
		print hero3 + ":", database[hero3][0], database[hero3][1], database[hero1][2]
		print "\n"
		print hero4 + ":", database[hero4][0], database[hero4][1], database[hero1][2]
		print "\n"
		print hero5 + ":", database[hero5][0], database[hero5][1], database[hero1][2]
		print "\n"
	
	elif (menuSelection == '3'):
		sys.exit()

