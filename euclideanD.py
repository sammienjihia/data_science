"""
Euclidean distance is calculated as sqrt(sum((x1-x2)**2+(y1-y2)**2))
"""

import math



def euclidean(point1, point2, length):
	E_distance = 0

	for x in range(length):
		E_distance += pow((point1[x]-point2[x]),2)

	return math.sqrt(E_distance) 


