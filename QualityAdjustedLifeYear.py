#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Quality-Adjusted Life-Year

count = int(input())
sum = 0

for i in range(count):
	a, b = list(map(float, input().split()))
	sum += a * b

print(sum)
