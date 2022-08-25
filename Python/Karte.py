#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 06/07/2022
#* Purpose: Karte
#*/

#imports

#methods
def checkDups(listOfElems):
	if len(listOfElems) == len(set(listOfElems)):
		return False
	else:
		return True

#main
def main():
	suits = ['P', 'K', 'H', 'T']
	counts = list()
	out = list()
	
	deck = input()
	
	for i in range(0, len(deck), 3):
		counts.append(deck[i:i+3])

	if checkDups(counts):
		print('GRESKA')
	else:
		for suit in suits:
			sum = 0
			for i in range(len(deck)):
				if deck[i] == suit:
					sum += 1
			out.append(13-sum)
		
		print(*out)
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	