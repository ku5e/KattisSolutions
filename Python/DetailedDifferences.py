#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/25/2022
#Purpose: Detailed Differences

counter = int(input())

for i in range(counter):
	a = input()
	b = input()
	
	pos = 0
	print(a)
	print(b)
	for la in a:
		if la == b[pos]:
			print('.', end='')
		else:
			print('*', end='')
		pos += 1
	print()
	print()