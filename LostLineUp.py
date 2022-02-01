#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/31/2022
#Purpose:

count = int(input())
people = input().split()
output = people.copy()

for i in range(count - 1):
	output[int(people[i])] = i + 2

print('1', end = ' ')
for x in output:
	print(x, end = ' ')
