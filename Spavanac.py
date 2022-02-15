#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/04/2022
#Purpose: Spavanac

h, m = list(map(int, input().split()))
m = m - 45
if m < 0:
	h -= 1
h = (((h % 24) + 24) % 24)
m = (((m % 60) + 60) % 60)

print(h, m)