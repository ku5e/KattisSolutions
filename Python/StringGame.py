#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:

num = int(input())

counter = 0
if num == 1:
	print(0)
	exit()
for i in range((num - 1), 1, -1):
	counter += 1
	if num % i == 0:
		print(counter)
		exit()
	