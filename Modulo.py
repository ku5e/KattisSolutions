#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/18/2022
#Purpose: Modulo

mods = []
for i in range(10):
	mods.append(int(input()) % 42)
print(len(set(mods)))