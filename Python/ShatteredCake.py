#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

w = int(input())
count = int(input())
totArea = 0

for i in range(count):
	x, y = input().split()
	x = int(x); y = int(y)
	totArea += (x * y)

l = totArea // w

print(l)
