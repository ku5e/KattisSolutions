#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 04/11/2022
#Purpose: ACM Contest Scoring
correct = 0
time = list()
problem = list()
correct = list()

delay = list()
right = 0
totalTime = 0

ind = list()

while True:
	question = list(input().split())
	question[0] = int(question[0])
	if question[0] == -1:
		break
	time.append(question[0])
	problem.append(question[1])
	correct.append(question[2])

for i in range(len(time)):
	if(correct[i] == 'right'):
		right += 1
		totalTime += time[i]
		ind.append(i)

for sol in ind:
	count = 0
	answer = problem[sol]
	for ans in problem:
		if ans == answer:
			count += 1
	count -= 1;
	totalTime += count * 20


print('%s %s' % (right, totalTime)) 