#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: XX/XX/XXXX
#* Purpose:
#*/

#imports

#methods

#main
def main():
	x = int(input())
	n = int(input())
	sum = 0
	
	for i in range(n):
		month = int(input())
		sum += x - month
		
	print(sum + x)
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	