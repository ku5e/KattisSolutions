#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 06/07/2022
#* Purpose: codetosavelives
#*/

#imports

#methods

#main
def main():
	for i in range(int(input())):
		first =int(input().replace(' ', ''))
		second = int(input().replace(' ', ''))
		out = str(first + second)
		
		print(*out)
		
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	