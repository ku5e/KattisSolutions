#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/10/2022
#Purpose: CPR Number
sum = 0
multiplier = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]

cprNum = input().replace('-','')

for i in range(len(multiplier)):
	sum += multiplier[i] * int(cprNum[i])

if sum % 11 == 0:
	print(1)
else:
	print(0)
	