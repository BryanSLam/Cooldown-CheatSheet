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
"Blitzcrank": (30,30,30), "Brand":(105,90,75), "Caitlyn":(90,75,60), "Cassiopeia":(130, 120, 110),
"Chogath": (60,60,60), "Corki":(1.2,1.2,1.2), "Darius":(120,100,80), "Diana":(25,20,15),
"Drmundo":(75,75,75), "Draven":(110,100,90), "Elise":(4,4,4), "Evelynn":(150,120,90),
"Ezreal":(80,80,80), "Fiddlesticks":(150,140,130), "Fiora":(130,120,110), "Fizz":(100,85,70),
"Galio":(170,150,130), "Gangplank":(120,115,110), "Garen":(160, 156, 152), "Gragas":(100,90,80),
"Graves":(100,90,80), "Hecarim":(140,120,100), "Heimerdinger":(130,115,100), "Irelia": (70,60,50),
"Janna":(150,135,120), "Jarvaniv":(120,105,90), "Jax":(80,80,80), "Jayce":(6,6,6), "Karma":(0,0,0), 
"Karthus":(200,180,160), "Kassadin":(7,6,5), "Katarina":(60,55,50), "Kayle":(90,75,60), "Kennen":(120,120,120),
"Khazix":(100,90,80), "Kogmaw":(2,1.5,1), "Leblanc":(40,32,24), "Leesin":(90,75,60), "Leona":(90,75,60),
"Lulu":(110,95,80), "Lux":(80,60,40), "Malphite":(130,115,100), "Malzahar":(120,100,80), "Maokai":(40,30,20),
"Masteryi":(75,75,75), "Missfortune":(120,110,100), "Mordekaiser":(120,105,90), "Morgana":(120,110,100), 
"Nami":(140,120,100), "Nasus":(120,120,120), "Nautilus":(140,110,80), "Nidalee":(4,4,4), "Nocturne": (180,140,100),
"Nunu":(150,120,90), "Olaf":(100,100,100), "Orianna":(120,105,90), "Pantheon":(150,135,120), "Poppy":(140,120,100),
"Quinn":(140,120,100), "Rammus":(60,60,60), "Renekton":(120,120,120), "Rengar":(140,105,70), "Riven":(110,80,50),
"Rumble":(105,90,75), "Ryze":(70,60,50), "Sejuani":(130,115,100), "Shaco":(100,90,80), "Shen":(200,180,160),
"Shyvana":(150,150,150), "Singed":(100,100,100), "Sion":(90,90,90), "Sivir":(100,90,80), "Skarner":(130,120,110),
"Sona":(140,120,100), "Soraka":(160,145,130), "Swain":(8,8,8), "Syndra":(100,90,80), "Talon":(75,65,55), "Taric":(60,60,60),
"Teemo":(1,1,1), "Thresh":(150,140,130), "Tristana":(60,60,60), "Trundle":(80,70,60), "Tryndamere":(110,100,90), "Twistedfate":(150,135,120),
"Twitch":(120,110,100), "Udyr":(6,6,6), "Urgot":(120,120,120), "Varus":(120,105,90), "Vayne":(70,70,70), "Veigar":(130,110,90),
"Vi":(130,105,80), "Viktor":(120,120,120), "Vladimir":(150,135,120), "Volibear":(100,90,80), "Warwick":(90,80,70), "Wukong":(120,105,90),
"Xerath":(80,70,60), "Xinzhao":(120,110,100), "Yorick":(120,105,90), "Zed":(120,105,90), "Ziggs":(120,105,90), "Zilean":(180,180,180),
"Zyra":(130,120,110)}
		

		
print "Main Menu"
menuSelection = 0
while(menuSelection != '3'):
	print "1: Input team line up"
	print "2: Individual lookup"
	print "3: Summoner spell reference"
	print "0: Quit"
	menuSelection = raw_input('>> ')
	
	if (menuSelection == '1'):
		print "There are no spaces, apostrophes, and capitalizations except the first letter. Examples: Drmundo, Khazix, Chogath, Jarvaniv"
		hero1 = raw_input('1:').capitalize()
		while((hero1 in database) == False):
			print "Character doesn't exist in database try again"
			hero1 = raw_input('1:').capitalize()
			
		hero2 = raw_input('2:').capitalize()
		while((hero2 in database) == False):
			print "Character doesn't exist in database try again"
			hero2 = raw_input('2:').capitalize()
			
		hero3 = raw_input('3:').capitalize()
		while((hero3 in database) == False):
			print "Character doesn't exist in database try again"
			hero3 = raw_input('3:').capitalize()
			
		hero4 = raw_input('4:').capitalize()
		while((hero4 in database) == False):
			print "Character doesn't exist in database try again"
			hero4 = raw_input('4:').capitalize()
			
		hero5 = raw_input('5:').capitalize()
		while((hero5 in database) == False):
			print "Character doesn't exist in database try again"
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
	
	elif (menuSelection == '0'):
		sys.exit()

