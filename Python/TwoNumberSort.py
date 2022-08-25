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
	arr = list(map(int, input().split()))
	arr = sorted(arr)
	for num in arr:
		print(num, end=' ')
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	