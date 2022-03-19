#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

word = set(input())
guesses = input()
badGuess = 0
lose = False

for letter in guesses:
	if letter in word:
		word.remove(letter)
	else:
		badGuess += 1
		if badGuess >= 10:
			lose = True
	if len(word) == 0:
		break
		
if lose:
	print("LOSE")
else:
	print('WIN')