#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 04/11/2022
#Purpose: Count the Vowels

phrase = input().replace(' ', '').lower()

vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in range(len(phrase)):
	if phrase[i] in vowels:
		count += 1

print(count)
