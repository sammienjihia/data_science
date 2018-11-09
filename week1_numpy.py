import numpy as np 

# This will create a 2 by 5 matrix with random floats between 0 and 1
data = np.random.random((2,5))

print(data)

# This will create a 2 by 5 matrix with 10 as the elements of the matrix
full_array = np.full((2,5),10)

print(full_array)

#will create an array where the elements are sorted and evenly distributed with a space of 5
even_array = np.arange(10,100,5)

print (even_array)

# an evenly distributed array of 9 elements from 0 to 2
line_space_array = np.linspace(0,2,9)

print(line_space_array)


# loading an array from csv PART 1
# delimeter used when the file is a comma seperated value
# unpack True means the matrix is transposed to allow assigning each column to its corresponding variable
# Please not, loadtxt() is a numpy function that returns a ndarray
height, weight, age = np.loadtxt('bmi.csv', delimiter=',', skiprows=1, unpack=True)

bmi_array = np.array([height,weight,age])

print(bmi_array)

#loading an array from csv PART 2
bmi = np.loadtxt('bmi.csv', delimiter=',', skiprows=1)
print (bmi)
print (type(bmi))


# loading an array from a csv file with missing values
bmi_missing = np.genfromtxt('bmi_missing_values.csv', delimiter=',', skip_header=1, filling_values=0)
print(bmi_missing)

# this script shall print out the correlation coeficient of the first column and the second column
print(np.corrcoef(bmi_missing[0], bmi_missing[1]))

# this below script shall print out the standard deviation of the bmi missing data
print(np.std(bmi_missing))

# prints out the ages
print(bmi_missing[:,2])

# prints out the median of the ages
print (np.median(bmi_missing[:,2]))

#prints out the mean of the ages
print (np.mean(bmi_missing[:,2]))

# prints out the standard deviation of the ages
print (np.std(bmi_missing[:2]))

# prints out sorted elements in the array 
print(np.sort(bmi_missing[:,2]))


# prints out the median 
print(np.median(bmi_missing[:,]))


# MATPLOTLIB
# to draw a line graph
import matplotlib.pyplot as plt


year = [1950,1970, 1990, 2010]
population = [20, 30, 40, 50]

chart = plt.plot(year, population)

plt.show(chart)

# to draw a scatter graph
chart_scatter = plt.scatter(year, population)
plt.show(chart_scatter)



















