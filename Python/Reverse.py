#!/usr/bin/env python3
#/*
#* Programmer: Mario Martinez
#* date: 04/15/2022
#* Purpose: Revers
#*/

count = int(input())
arr = list()
for i in range(count):
	arr.append(input())

for i in range(count-1, -1, -1):
	print(arr[i])