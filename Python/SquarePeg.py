#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 05/13/2022
#* Purpose: SquarePeg
#*/

#imports

#methods

#main
def main():
	l, r = list(map(int, input().split()))
	if (r**2) >= ((l**2)/2):
		print('fits')
	else:
		print('nope')
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	