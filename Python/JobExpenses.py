#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Job Expenses

n = int(input())
arr = input().split(" ")

summ = 0
for i in range(n):
	if(int(arr[i]) < 0):
		summ += int(arr[i])
		
print(abs(summ))