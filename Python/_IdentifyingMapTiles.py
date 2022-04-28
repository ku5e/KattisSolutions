#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: IdentifyingMapTiles
def genMap(zoom):
	map = dict()
	for i in range(0, zoom):
		first = i
		for j in range(0, zoom):
			map.update({})
	

mapSizes = {1:(2,2), 2:(4,4), 3:(8,8), 4:(16,16)} 

num = input()
zoom = len(num)

