#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 04/11/2022
#Purpose: Double Password

first = input()
second = input()
count = 0

for i in range(4):
	if first[i] != second[i]:
		count += 1

print(2 ** count)