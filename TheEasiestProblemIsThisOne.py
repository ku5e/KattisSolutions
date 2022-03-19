#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: The Easiest Problem Is This One
def sumDigits(x):
	sum = 0
	while x > 0:
		sum += x % 10
		x = x // 10
	return(sum)

num = int(input())
while num != 0:
	sumNum = sumDigits(num)
	mult = 11
	while sumNum != sumDigits(mult * num):
		mult += 1
	print(mult)
	num = int(input())
	