"""
Resources used for this python script includes

1. wikipedai
2. https://stackoverflow.com/questions/34555135/pandas-read-html/34555201  (encountered error: ImportError: lxml not found, please install it )
https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)

https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy

"""


import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

countries_GDP = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

countries_LE = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy')


#print(countries_GDP[2][[1,2]][2:])

pd_countriesGDP = countries_GDP[2][[1,2]][2:]
pd_countriesLE = countries_LE[2][[1,2]][1:]

print (countries_LE[2][[1,2]][1:])
print("length of countries by GDP {} length of countries by LE {}".format(len(pd_countriesGDP), len(pd_countriesLE)))

# This will return row 23 as a series. NB the index of this dataframe is a list of integers
print (pd_countriesGDP.loc[23])

# this will return a row 100 in a dataframe form.
print(pd_countriesGDP.loc[[100]]) 

#this will return a data cell of row 23 and column 1
print (pd_countriesGDP.loc[23,1])

# This will return rows 24,29,100,150 and columns 1 and 2 as a frame
print(pd_countriesGDP.loc[[24,29,100,150],[1,2]])


# NB loc is only used with the actual names of the index or column, otherwise if using list indices then use iloc
# .loc is primarily label based, but may also be used with a boolean array.
# .iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.

# This will return a row of slice labels 1 to 100 and column label 1 in serires form
print(pd_countriesGDP.loc[1:100, 1])

# This will return a row of slice indeces 1 to 100 and 
print(pd_countriesGDP.iloc[1:100, 1])

#pd_countriesGDP.index = pd_countriesGDP.1

# This will return the column name 2
print(pd_countriesGDP.columns[1])

# This will retur the column name 1
print(pd_countriesGDP.columns[0])

# NB If the column name is a string, the you can access the column as
# pd_countriesGDP.column_name

# NB to convert a time column to pandas datetime and make it an index of the dataframe
# some_dataframe.index = pd.to_datetime(some_dataframe.pop('dt')) ; Where dt is the time column.

# Setting column 1 as an index of dataframe pd_countriesGDP
print(pd_countriesGDP.set_index([1], inplace=True))

# Setting column 1 as an index for dataframe pd_countriesLE
print(pd_countriesLE.set_index([1], inplace=True))

#combined_dataSET = pd_countriesGDP.merge(pd_countriesLE)
#combined_dataSET = pd_countriesGDP.set_index([1]).join(pd_countriesLE.set_index([1]))

print("****"*30)

print(pd_countriesLE)
print(pd_countriesGDP)

print(combined_dataSET)




# pd_frames = [pd_countriesGDP, pd_countriesLE]

# print("****"*20)

# print (pd.concat(pd_frames))


#combined_dataSET = pd_countriesGDP.set_index([1]).join(pd_countriesLE.set_index([1]))
print(pd_countriesGDP.set_index([1]).join(pd_countriesLE.set_index([1])))