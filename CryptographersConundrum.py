#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Cryptographer's Conundrum

word = input()
keyWord = 'PER'
count = len(word)

for x in range(count):
	if keyWord[x % 3] == word[x]:
		count -= 1
print(count)