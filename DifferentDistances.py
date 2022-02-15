#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: Different Distances

while(True):
	try:
		x1, y1, x2, y2, p = list(map(float, input().split()))
	except: 
		break
	out = ((abs(x1 - x2)**p) + (abs(y1-y2)**p))**(1/p)
	print(out)