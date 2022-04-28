#!/usr/bin/env python3
#/*
#* Programmer: MM KU5E@KU5E.COM
#* date: 04/22/2022
#* Purpose: Synchronizing Lists
#*/

#imports

#methods

#main
def main():
	count = int(input())
	while count != 0:
		firstList = list()
		secondList = list()
		newFirst = list()
		newSecond = list()
		orderedDict = dict()
		ans = list()
		
		for i in range(count):
			firstList.append(int(input()))
		for i in range(count):
			secondList.append(int(input()))
			
		newFirst = sorted(firstList)
		newSecond = sorted(secondList)
		
		for i in range(count):
			orderedDict.update({newFirst[i] : newSecond[i]})
		
		for i in range(count):
			ans.append(orderedDict.get(firstList[i]))
		
		for num in ans:
			print(num)
		print()
			
		count = int(input())
		#print(newFirst, newSecond, orderedDict, ans)
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	