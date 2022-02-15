#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/01/2022
#Purpose: License to Launch

input()
debrisCount = list(map(int, input().split()))

print(debrisCount.index(min(debrisCount)))