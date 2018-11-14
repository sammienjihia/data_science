import pandas as pd 
import numpy as np 
import math
from euclideanD import euclidean 



pd_TSindex = pd.read_csv('t_size_index.csv')

#print(np.array(pd_TSindex)[3][1])
e_distance = []

np_TSindex = np.array(pd_TSindex)

#print(len(np_TSindex[:]))
#print(len(np_TSindex[0][:]))

original = [[161,61]]
K = 3
"""
Find the euclidean distances
"""
# Iterates through the rows
for rows in range(len(np_TSindex[:])):
	# Iterates through the columns
	e_distance.append(euclidean(original[0], np_TSindex[rows], 2))

# Assign the distances to a new column in the dataFrame
pd_TSindex['E.Distance'] = e_distance

print(pd_TSindex)

# Find the K least values (K Nearest Neighbours) in the E.Distance column and assign that DataFrame to pd_data
pd_data = pd_TSindex.nsmallest(K, columns='E.Distance')

print(pd_TSindex.nsmallest(K, columns='E.Distance'))
#print(pd_TSindex['E.Distance'].nsmallest(3, 0))

#Find the most frequent Label in the pd_data: That's the predicted class
print(pd_data['Label'].mode())


 
