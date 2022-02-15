#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Forced Choice

cards, prediction, steps = input().split()

for i in range(int(steps)):
	turn = input().split()
	#print(turn)
	for j in range(1, len(turn)):
		#print(turn[j])
		trigger = False
		if(turn[j] == prediction):
			print("KEEP")
			trigger = True
			break
	if(not trigger):
		print("REMOVE")	