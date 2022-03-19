#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:

count = int(input())
for i in range(count):
	case, test = list(input().split())
	case = int(case)
	num, den = list(map(int, test.split('/')))
	print(case, num, den)
