#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:

n, m = list(map(int, input().split()))
if n > m:
	largest = n
	smallest = m
else:
	largest = m
	smallest = n

first = smallest + 1
last = largest + 1

for i in range(first,last + 1):
	print(i)