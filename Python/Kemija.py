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
	words = input()
	i = 0
	while i < len(words):
		if words[i] == 'a' or words[i] == 'e' or words[i] == 'i' or words[i] == 'o' or words[i] == 'u':
			i += 2
			print(words[i], end="")
		else:
			print(words[i], end ="")
		i += 1
		
	
#if name main main
if __name__ == "__main__":
	main();
	
	