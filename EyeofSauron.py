#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/26/2022
#Purpose: Eye of Sauron

drawing = input()
countFront = drawing.find('(')
countBack = len(drawing) - countFront - 2
if countFront == countBack:
	print('correct')
else:
	print('fix')