#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Odd Echo

n = int(input())
for i in range(n):
	word = input()
	if (i + 1) % 2 != 0:
		print(word)