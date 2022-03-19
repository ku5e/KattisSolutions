#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/25/2022
#Purpose: Speeding

count = int(input())
totD, totT = list(map(int, input().split()))
oldD = totD
oldT = totT
greatest = 0

for i in range(count - 1):
	totD, totT = list(map(int, input().split()))
	speed = ((totT - oldT) // (totD - oldD))
	#print((totD - oldD), (totT - oldT), speed)
	if(speed > greatest):
		greatest = speed
	oldD = totD
	oldT = totT


print(speed)
	
	
	
	