#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/25/2022
#Purpose: Autori

word = input()
print(word[0], end ="")
for x in range(len(word)):
	if word[x] == '-':
		print(word[x+1], end ="")