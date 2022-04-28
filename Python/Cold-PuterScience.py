#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/21/2022
#Purpose: Cold-Puter Science on Kattis

input() #Skip the counter
sum = 0
temps = input() #Take the temps as a 
				#string so I can count the - characters in it
for i in temps:
	if(i == "-"):
		sum = sum + 1
		
print(sum)