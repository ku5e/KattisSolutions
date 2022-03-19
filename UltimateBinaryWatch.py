#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/10/2022
#Purpose: Ultimate Binary Watch

digits = ['....', '...*', '..*.', '..**', '.*..', '.*.*', '.**.', '.***', '*...', '*..*']
out = list()

time = input()

for digit in time:
	out.append(int(digit))

for i in range(4):
	print(digits[out[0]][i], digits[out[1]][i], ' ', digits[out[2]][i], digits[out[3]][i],)
