#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 04/22/2022
#* Purpose: Help a PHP
#*/

#imports

#methods
def disassemble(prob):
	signPos = prob.find('+')
	a = int(prob[:signPos])
	b = int(prob[signPos + 1:])
	ans = a + b
	return ans

#main
def main():
	count = int(input())
	for i in range(count):
		math = input()
		if math == 'P=NP':
			print('skipped')
		else:
			print(disassemble(math))
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	