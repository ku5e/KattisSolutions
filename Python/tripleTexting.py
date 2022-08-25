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
	mawmaw = input()
	length = len(mawmaw)
	size = length // 3
	word1 = mawmaw[:size]
	word2 = mawmaw[size:size*2]
	word3 = mawmaw[size*2:]
	
	if(word1 == word2):
		print(word1)
	elif(word2 == word3):
		print(word2)
	else:
		print(word3)
	
	return 0

#if name main main
if __name__ == "__main__":
	main();
	
	