#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/01/2022
#Purpose: No Duplicates

wordList = input().split()
wordSet = set(wordList)

if len(wordSet) == len(wordList):
	print('yes')
else:
	print('no')