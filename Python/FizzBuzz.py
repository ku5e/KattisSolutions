#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

x, y, n = input().split()

x = int(x)
y = int(y)
n = int(n)

for i in range(1, n + 1):
	if i % x == 0 and i % y == 0:
		print('FizzBuzz')
	elif i % x == 0:
		print('Fizz')
	elif i % y == 0:
		print('Buzz')
	else: 
		print(i)