#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 04/22/2022
#* Purpose: Boat parts
#*/

#imports

#methods

#main
def main():
	p, n = list(map(int, input().split()))
	ordered = list()
	parts = list()
	
	for i in range(n):
		ordered.append(input())
		if ordered[i] not in parts:
			parts.append(ordered[i])
	
		#print(parts)
		#print(ordered)
	
	
	if len(parts) >= p:
		print(ordered.index(parts[len(parts) - 1]) + 1)
	else: 
		print('paradox avoided')
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	