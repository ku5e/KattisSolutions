#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/25/2022
#Purpose: Speeding

class Speeding :
	@staticmethod
	def main( args) :
		input()
		totD, totT = list(map(int, input().split()))
		speed = 0
		oldTotD = 1
		oldTotT = 1
		greatest = 0
		while True:
			speed = ((totD - oldTotD) // (totT - oldTotT))
			if (speed > greatest) :
				greatest = speed

			oldTotD = totD
			oldTotT = totT
			
			try:
				totD, totT = list(map(int, input().split()))
			except:
				break
		print(greatest)
		
		
if __name__=="__main__":
	Speeding.main([])