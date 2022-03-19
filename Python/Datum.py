#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/18/2022
#Purpose: Datum

def dayOfWeek(y, m, d):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	if(m < 3):
		y -= 1
	return (y + y//4 - y//100 + y//400 + t[m-1] + d) % 7

year = 2009
day, month = list(map(int, input().split()))

dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(dow[dayOfWeek(year, month, day)])

