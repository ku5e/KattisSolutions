#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

from collections import Counter

n = int(input())

for i in range(1, n + 1):
	input()
	for key, value in Counter(input().split()).items():
		if 1 == value:
			print('Case #%s: %s' % (i, key))
		