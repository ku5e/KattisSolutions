#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/26/2022
#Purpose:I've been everywhere man

count = int(input())

for j in range(count):
	places = set()
	numPlaces = int(input())
	for i in range(numPlaces):
		places.add(input())
	print(len(places))