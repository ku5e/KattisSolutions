#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/08/2022
#Purpose:

y = int(input())
x = int(input())

main = (x // y)
extra = (x - (x // y) * y)

if extra == 0:
	for i in range(y):
		print('*' * main)
else:
	for i in range(y):
		print('*' * main, end = '')
		if extra > 0:
			print('*')
			extra -= 1
		else:
			print()
		