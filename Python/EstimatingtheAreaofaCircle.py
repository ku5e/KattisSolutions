#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/04/2022
#Purpose: Estimating the Area of a Circle
import math

r, m, c = list(map(float, input().split()))
while(r != 0 and m != 0 and c != 0):
	area = (2 * r) ** 2
	estimate = area * c / m
	actualArea = math.pi * r ** 2
	print('%s %s' % (actualArea, estimate))
	r, m, c = list(map(float, input().split()))
	