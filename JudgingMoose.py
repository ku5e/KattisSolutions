#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/25/2022
#Purpose:

x, y = input().split()
x = int(x)
y = int(y)
even = x == y
if(x + y == 0):
	print('Not a moose')
elif even:
	print('Even', (x + y))
else:
	if x > y:
		print('Odd', (x * 2))
	else:
		print('Odd', (y * 2))
