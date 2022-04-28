#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 04/01/2022
#Purpose: FinalExam2

score = 0
count = int(input())

grades = list()

for i in range(count):
	grades.append(input())
	if(i > 0 and grades[i] == grades[i - 1]):
		score += 1
		
print(score)

