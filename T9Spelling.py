#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/07/2022
#Purpose:

def generateMap():
	dictionary[32] = (str(0)) #fill in for space
	char = 97 #lower case a
	#fill it up to 7 with 3 possibilities
	for i in range(2, 8):
		dictionary[char] = (str(i))
		dictionary[char + 1] = (str(i) * 2)
		dictionary[char + 2] = (str(i) * 3)
		char += 3
	#add the 4th to seven
	dictionary[char] = (str(7) * 4)
	char += 1
	#fill 8 and 9 with 3
	for i in range(8, 10):
		dictionary[char] = (str(i))
		dictionary[char + 1] = (str(i) * 2)
		dictionary[char + 2] = (str(i) * 3)
		char += 3
	#add the last to 9
	dictionary[char] = (str(9) * 4)

dictionary = {} #create the Dict
generateMap() #fill it

count = int(input())
lastCharNum = -1
for i in range(count):
	words = input()
	print('Case #%s: ' % (i + 1), end = '')
	for letter in words:
		charNum = dictionary.get(ord(letter))
		if str(charNum)[0] == str(lastCharNum)[0] and lastCharNum != 32:
			print(' ', end = '')
			#print(letter, end = '')
		print(charNum, end = '')
		lastCharNum = charNum
	print()
		
		