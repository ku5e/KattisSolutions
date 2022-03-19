#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/10/2022
#Purpose: Symetric Order

count = int(input())
num = 1
while count > 0:
	names = list()
	length = list()
	for i in range(count):
		names.append(input())
	newNames = names
	for j in range(0, count, 2):
		newNames[j] = names[j]
		print(j, count)
		if j < count - 1:
			newNames[len(names) - 1 - j] = names[j + 1]
		
		
	print('SET %s' % num)
	print(newNames)
	num += 1
	
	count = int(input())



