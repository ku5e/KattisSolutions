#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 04/15/2022
#* Purpose: Soda Slurper
#*/

arr = list(map(int, input().split()))
e = arr[0]
f = arr[1]
c = arr[2]

finCount = 0
bottlesCanBuy = 0

sum = e + f

while sum >= c:
	bottlesCanBuy = sum % c
	sum //= c
	finCount += sum
	sum += bottlesCanBuy

print(int(finCount))