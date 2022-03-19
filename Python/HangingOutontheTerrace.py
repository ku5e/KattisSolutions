#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/16/2022
#Purpose: Hanging Out on the Terrace

l, x = list(map(int, input().split()))

count = 0
inside = 0
for i in range(x):
	party = list(input().split())
	
	if party[0] == 'enter':
		if int(party[1]) > l - inside:
			count += 1
		else:
			inside += int(party[1])
	else: 
		inside -= int(party[1])

print(count)