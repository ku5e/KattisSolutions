#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Harshad Numbers

number = input()
n = [int(x) for x in list(number)]
if int(number) % sum(n) == 0:
	print(number)
else:
	
	while int(number) % sum(n) != 0:
		number = int(number)
		number += 1
		number = str(number)
		n = [int(x) for x in list(number)]
	print(number)