#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/26/2022
#Purpose: Mult!


input()
x = True

base = int(input())
candidate = int(input())

while x:
	while candidate % base != 0:
		try:
			candidate = int(input())
		except EOFError:
			exit()
	else: 
		print(candidate)
		base = int(input())
		try:
			candidate = int(input())
		except EOFError:
			exit()
	
	
	
