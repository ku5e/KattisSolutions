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
	day = list(input().split())
	if (day[0] == 'DEC' and day[1] == '25') or (day[0] == 'OCT' and day[1] == '31'):
		print('yup')
	else:
		print('nope')
	
	
#if name main main
if __name__ == "__main__":
	main();
	
	