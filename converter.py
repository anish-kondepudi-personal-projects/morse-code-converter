
# Credits For Conversion Table and Testing Sample Data
# http://www.sckans.edu/~sireland/radio/code.html
# https://morsecode.world/international/translator.html

import os

FILENAME = "encoding.txt"

def getCharToMorse(filename):
	with open(filename) as file:
		lines = eval(file.readline())
		return lines

def convertMorseToAlphaNum(morseToChar,s):
	res,tmp = '',''
	for c in s:
		if c not in {' ','/','|'}:
			tmp += c
		else:
			res += morseToChar[tmp]
			tmp = ''
			if c != ' ': res += ' '
	if len(tmp) != 0: res += morseToChar[tmp]
	return res

def convertAlphaNumToMorse(charToMorse,s):
	res,tmp = '',''
	for c in s:
		if c != ' ':
			res += charToMorse[c.upper()]+' '
		else:
			res += '/ '
	return res

def userInteraction(filename):
	os.system('cls' if os.name == 'nt' else 'clear')
	charToMorse = getCharToMorse(filename)
	morseToChar = {v:k for (k,v) in charToMorse.items()}
	while True:
		print("Do you want to convert\n1) Morse to AlphaNum\n2) AlphaNum to Morse\nPlease Select 1 or 2: ",end='')
		action = input()
		while action not in {'1','2'}:
			print("Please select either '1' or '2': ",end='')
			action = input()
		if action == '1':
			print("Please type morse code: ",end='')
			print(convertMorseToAlphaNum(morseToChar,input()))
		else:
			print("Please type alphanum string: ",end='')
			print(convertAlphaNumToMorse(charToMorse,input()))
		print("Do you want to convert again? (y/n): ")
		action = input().lower()
		while action not in {'y','n'}:
			print("Please select either 'y' or 'n': ",end='')
			action = input().lower()
		os.system('cls' if os.name == 'nt' else 'clear')
		if action == 'n': break

userInteraction(FILENAME)
