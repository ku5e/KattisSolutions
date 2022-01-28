#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

prob = input().split(';')
total = []
for nums in prob:
	if '-' in nums:
		temp = [int(i) for i in nums.split('-')]
		for i in range (temp[1] - temp[0] + 1):
			total.append(True)
	else:
		total.append(True)

print(len(total))