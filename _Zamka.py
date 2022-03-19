#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/10/2022
#Purpose: Zamka

def getSum(n):
	sum = 0
	while n != 0:
		sum = sum + n % 10
		n = n//10
	return sum
		
minNum = int(input())
maxNum = int(input())
sumVal = int(input())

smallest = -1
biggest = -1

for i in range(minNum, maxNum):
	if getSum(i) == sumVal:
		smallest = i
		break

for j in range(maxNum, minNum, -1):
	if getSum(j) == sumVal:
		biggest = j
		break
	
print(smallest)
print(biggest)