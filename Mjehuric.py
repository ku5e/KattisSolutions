#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 01/29/2022
#Purpose:
def printOut(arr):
	for num in arr:
		print(num, end=" ")

game = input().split()

for j in range(len(game)):
	for i in range(1, len(game)):
		if game[i] < game[i - 1]:
			temp = game[i]
			game[i] = game[i - 1]
			game[i - 1] = temp
			printOut(game)
			print()
