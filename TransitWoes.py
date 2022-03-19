#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Transit Woes

s, t, n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

timeSum = 0
for x in d:
	timeSum += x

for y in b:
	timeSum += y

for i in range(len(c)):
	if i == 0:
		timeSum += c[i]
	elif i == n:
		timeSum += c[i]

if timeSum <= t - s:
	print('yes')
else:
	print('no')