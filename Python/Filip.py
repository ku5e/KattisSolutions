#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/21/2022
#Purpose: Filip

x, y = input().split()
x = int(x[::-1])
y = int(y[::-1])

if(x > y):
	print(x)
else:
	print(y)
	
