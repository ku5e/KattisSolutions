#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 05/16/2022
#* Purpose: Dice game
#*/

#imports

#methods

#main
def main():
	ga1, gb1, ga2, gb2 = list(map(int, input().split()))
	ea1, eb1, ea2, eb2 = list(map(int, input().split()))
	
	gMax = (gb1 + ga1) + (gb2 + ga2)
	eMax = (eb1 + ea1) + (eb2 + ea2)

	if(gMax > eMax):
		print('Gunnar')
	elif(gMax < eMax):
		print('Emma')
	else:
		print('Tie')
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	