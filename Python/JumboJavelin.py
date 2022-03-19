#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Jumbo Javelin

nums = []
count = int(input())
for i in range(count):
	nums.append(int(input()))
print(sum(nums) - (count - 1))