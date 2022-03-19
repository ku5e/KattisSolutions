#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/18/2022
#Purpose: GCVWR

gcvwr, weight, items = list(map(int, input().split()))
itemWeights = list(map(int, input().split()))

print(int(((gcvwr - weight) * .90) - sum(itemWeights)))

