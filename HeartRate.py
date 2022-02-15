#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Heart Rate

count = int(input())
for i in range(count):
	b, p = list(map(float, input().split()))
	bpm = 60 * b / p
	variance = 60 / p
	min = bpm - variance
	max = bpm + variance
	print(min, bpm, max)

