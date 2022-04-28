#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 03/10/2022
#Purpose: Symetric Order

def sortByLen(arr):
	finArr = sorted(arr, key=len)
	return finArr

def main():
	count = int(input())
	num = 1
	
	while count > 0:
		names = list()
		for i in range(count):
			names.append(input())
		names = sortByLen(names)
		
		print('SET %s' % num)
		for i in range(0, len(names), 2):
			print(names[i])
		for i in range(len(names)-1, 0, -2):
			if count % 2 == 0:
				print(names[i])
			else:
				print(names[i-1])
				
		count = int(input())
		num += 1
	return 0

#if name main main
if __name__ == "__main__":
	main();
	

	