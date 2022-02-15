#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/11/2022
#Purpose: DRM Messages

def rotate(s):
	val = 0
	ch = list(s)
	for c in ch:
		val += ord(c) - ord('A')
	for i in range (len(ch)):
		ch[i] = rotateChar(ch[i], val)
	return(ch)
	
def rotateChar(c, val):
	return(chr((((ord(c) - ord('A') + val)) % 26) + ord('A')))

def merge(word, key):
	w = list(word)
	k = list(key)
	for i in range(len(w)):
		w[i] = rotateChar(w[i], ord(k[i]) - ord('A'))
	return w

s = input()
word = s[:(len(s) // 2)]
key = s[(len(s) // 2):]

word = rotate(word)
key = rotate(key)

for char in merge(word, key):
	print(char, end='')

