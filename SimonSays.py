#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Simon Says

count = int(input())
for i in range(count):
	command = input()
	if command[:10] == 'Simon says':
		print(command[11:])