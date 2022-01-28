#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/28/2022
#Purpose:

count = int(input())

for i in range(count):
	word = input();
	sqrtsz = int(len(word)**(1/2))
	out = ""
	for j in range(sqrtsz):
		position = sqrtsz - j - 1
		out += word[position::sqrtsz]
	print(out)