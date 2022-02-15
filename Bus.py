#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/07/2022
#Purpose: Bus

# half of all passangers + .5 get off at each stop

count = int(input())

for i in range(count):
	stops = int(input())
	sum = 0
	for j in range(1,stops + 1):
		sum += .5
		sum *= 2
	print(int(sum))