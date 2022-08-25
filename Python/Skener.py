#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 05/16/2022
#* Purpose: Skener
#*/

#imports

#methods

#main
def main():
	r, c, zr, zc = list(map(int, input().split()))

	for i in range(r):
		nextRow = input()
		newRow = ''
		for j in range(len(nextRow)):
			newRow += nextRow[j] * zc

		for k in range(zr):
			print(newRow)

	return 0

#if name main main
if __name__ == "__main__":
	main();
	
