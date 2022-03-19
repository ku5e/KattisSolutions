#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Turn It Up!

count = int(input())
vol = 7

for x in range(count):
	if len(input()) < 9:
		vol += 1
	else:
		vol -= 1
	if vol < 0:
		vol = 0
	if vol > 10:
		vol = 10
	
print(vol)