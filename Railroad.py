#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Railroad

x, y = list(map(int, input().split()))
if (x * 4 + y * 3) % 2 != 0:
	print('im', end='')
print('possible')