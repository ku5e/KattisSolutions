#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/18/2022
#Purpose: Quick Brown Fox
def splitPrase(x):
	out = set()
	for i in range(len(x)):
		out.add(x[i])
	return out

count = int(input())

alpha = ['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'o', 'x', 'j', 'u', 'm', 'p', 's', 'o', 'v', 'e', 'r', 't', 'h', 'e', 'l', 'a', 'z', 'y', 'd', 'o', 'g']

for i in range(count):
	letters = splitPrase(input().lower().strip())
	ans = set()
	for j in range(len(alpha)):
		if alpha[j] not in letters:
			ans.add(alpha[j])
	if len(ans) > 0:
		print('missing ', end = '')
		for k in sorted(ans):
			print(k, end = '')
	else:
		print('pangram', end = '')
	print()