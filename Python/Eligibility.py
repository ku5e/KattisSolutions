#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/07/2022
#Purpose: Eligibility

count = int(input())

for i in range(count):
	studInfo = input().split()
	print(studInfo[0], end = ' ')
	first = studInfo[1]
	dob = studInfo[2]
	courses = studInfo[3]
	
	if int(first[:4]) >= 2010 or int(dob[:4]) >= 1991:
		print('eligible')
	elif int(courses) >= 41:
		print('ineligible')
	else:
		print('coach petitions')
