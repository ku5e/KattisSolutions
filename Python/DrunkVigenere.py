#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose:

encrypted = input()
key = input()

for i in range(len(key)):
	shift = ord(key[i]) - 65
	if(i % 2 == 0):
		decrypted = chr(((ord(encrypted[i]) - 65 - shift) % 26) + 65)
	else:
		decrypted = chr(((ord(encrypted[i]) - 65 + shift) % 26) + 65)
	print(decrypted, end = '')