#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/25/2022
#Purpose: SevenWonders

word = input()
count = [0, 0, 0]

for letter in word:
	if letter == 'T':
		count[0] += 1
	elif letter == 'C':
		count[1] += 1
	else:
		count[2] += 1

count.sort()

bonus = count[0] * 7
out = bonus + count[0] ** 2 + count[1] ** 2 + count[2] ** 2

print(out)
