#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

arr = input().split(';')
count = len(arr)

for num in arr:
	if '-' in num:
		temp = num.split('-')
		count += int(temp[1]) - int(temp[0])
		
print(count)