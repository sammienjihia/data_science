import pandas as pd 
import os

# creating a pandas dataframe METHOD 1
pandas_dataframe1 = pd.DataFrame(
	{
		"column1":[1,2,3,4,5],
		"column2":['a','b','c','d','e']
	})

print(pandas_dataframe1)

# creating pandas dataframe METHOD 2
# NB This method can only be followed when you are passing data to one single column at a time
pandas_dataframe2 = pd.DataFrame(data=[x for x in range(10) ], columns=['column1'])
print(pandas_dataframe2)

# DataFrame rows and columns with .shape command
# will return a tuple of number of rows and number of columns

print(pandas_dataframe2.shape)
print(pandas_dataframe1.shape)

# ndim command gives the number of dimensions of your dataset
print(pandas_dataframe1.ndim)
print(pandas_dataframe2.ndim)

# Preview data frames with head() and tail() functions
#This will preview the first 5 rows
print(pandas_dataframe2.head(5))

#This will preview the last 2 rows
print(pandas_dataframe1.tail(2))

# Reading data from a csv file
# the read_csv() function has other arguments. Kindly refer to the pandas documentation
pandas_dataframe3 = pd.read_csv('COUNTRIESGDP.csv')
print(pandas_dataframe3)

# Deleting a column using the drop() function METHOD 1
# Note we are not using inplace=True since we are assigning a modified copy of pandas_dataframe3 to pandas_dataframe4
# If we wanted to change the original pandas_dataframe3 without creating a copy then we would have used inplace=True
pandas_dataframe4 = pandas_dataframe3.drop(columns='i')
print(pandas_dataframe4)

# Deleting a column using the drop() function METHOD 2
# Note the use of axis=1 which means select from the columns or (select from the x axis)
# the column argument can also be a list of columns e.g ['column1', 'column2']
pandas_dataframe5 = pandas_dataframe3.drop('i', axis=1)
print(pandas_dataframe5)

# Deleting a row using the drop() function
# note the use of axis=0 meaning select rows or select from the y axis.
# Note, I have set the countries as the index making the country names as the labels for the rows
pandas_dataframe6 = pandas_dataframe3.set_index('countries')
pandas_dataframe6 = pandas_dataframe6.drop(['Kiribati', 'Palau'], axis=0)
print(pandas_dataframe6)

# Renaming columns using the rename() function METHOD 1 using a dictionary
# with the old column name as the key and the new column name as the value
pandas_dataframe7 = pandas_dataframe3.rename(columns={
	"countries":"kwantry"
	})
print(pandas_dataframe7)


"""
lambda functions are anonymous (unnamed function) functions that are defined by the key word lambda instead of def
Syntax of lambda funcions are as follows 
lambda arguments:expression 
"""
pandas_dataframe8 = pandas_dataframe3.rename(columns= lambda x:x.upper() )
print(pandas_dataframe8)

# Renaming columns METHOD 2 assigning new column names to the dataframe's columns directive  
pandas_dataframe9 = pandas_dataframe3
pandas_dataframe9.columns = ['asd', 'dfg', 'kgf']
print(pandas_dataframe9)


