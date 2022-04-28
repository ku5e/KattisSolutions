#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/25/2022
#Purpose: Birthday Memorization

counter = 0
names = list()
ratings = list()
date = list()
count = int(input())

for i in range(count):
	#Element legend 0 - name, 1 - rating, 2 - date
	stdIn = list(input().split())
	names.append(stdIn[0])
	ratings.append(stdIn[1])
	date.append(stdIn[2])
	
print(names)
print(ratings)
print(date)

for i in range(count):
	for j in range(i+1, count):
		if date[i] == date[j]:
			counter += 1
			if ratings[i] > ratings[j]:
				names[j] = '***'
			else:
				names[i] = '***'

finalNames = list()
for i in range(count):
	if names[i] != '***':
		finalNames.append(names[i])
		
finalNames.sort()

print(len(finalNames))
for name in finalNames:
	print(name)
	

