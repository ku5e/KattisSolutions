#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: Quadrant Selection

x = int(input())
y = int(input())

if x > 0:
	if y > 0:
		print(1)
	else:
		print(4)
elif x < 0:
	if y > 0:
		print(2)
	else:
		print(3)