#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/21/2022
#Purpose: Filip

x, y = input().split()
x = x[::-1]
y = y[::-1]
x = int(x)
y = int(y)
if(x > y):
	print(x)
else:
	print(y)
	