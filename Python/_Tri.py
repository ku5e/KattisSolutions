#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 04/15/2022
#* Purpose: Tri
#*/
nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]
c = nums[2]


if a + b == c:
	print('%s+%s=%s' % (a, b, c))
if a == b + c:
	print('%s=%s+%s' % (a, b, c))
if a - b == c:
	print('%s-%s=%s' % (a, b, c))
if a == b - c:
	print('%s=%s-%s' % (a, b, c))
	
if a * b == c:
	print('%s*%s=%s' % (a, b, c))
if a == b * c:
	print('%s=%s*%s' % (a, b, c))
if a // b == c:
	print('%s/%s=%s' % (a, b, c))
if a == b // c:
	print('%s=%s/%s' % (a, b, c))
	