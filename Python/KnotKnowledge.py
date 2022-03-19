#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/25/2022
#Purpose: Knot Knowledge

count = int(input())
needs = set(map(int, input().split()))
learned = set(map(int, input().split()))

ans = list(needs - learned)

print(ans[0])