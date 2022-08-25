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
	first, second = list(map(int, input().split()))
	
	while True:
		if first + second == 13:
			print('Never speak again.')
		elif first > second:
			print('To the convention.')
		elif second > first:
			print('Left beehind.')
		else:
			print('Undecided.')
			
		first, second = list(map(int, input().split()))
		if first == 0 and second == 0:
			break

	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	