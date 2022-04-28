#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/21/2022
#Purpose: I've Been Everywhere, Man

trips = int(input())

for i in range(trips):
	places = int(input())
	towns = []
	cleanTowns = []
	for j in range(places):
		towns.append(input())
	for k in towns:
		if k not in cleanTowns:
			cleanTowns.append(k)
	print(len(cleanTowns))
