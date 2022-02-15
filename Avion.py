#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/02/2022
#Purpose: Avion

out = list()

for i in range(5):
	word = input()
	if word.find('FBI') >= 0:
		out.append(i)

if len(out) > 0:
	for nums in out:
		print(nums + 1, end = ' ')
else: 
	print('HE GOT AWAY!')