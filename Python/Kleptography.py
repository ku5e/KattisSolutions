#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/01/2022
#Purpose: Kleptography

lengthKey, lengthMessage = map(int, input().split())

key = input()
message = input()
out = key[::-1]

for i, j in zip(range(lengthMessage - 1, lengthKey - 1, -1), range(len(message))):
	pos = 97 + (ord(message[i]) - ord(out[j])) % 26
	out += chr(pos)

print(out[::-1])
