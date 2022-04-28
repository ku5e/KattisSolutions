#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 04/10/2022
#Purpose: Mirror Images

count = int(input())

for i in range (count):
	data = list()
	dims = list(map(int, input().split()))
	for row in range(dims[0]):
		data.append(input())
	print('Test %s' % (i+1))	
	data = data[::-1]
	for item in data:
		print(item[::-1])
