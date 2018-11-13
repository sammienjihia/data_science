import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np


# Find your current working directory
import os 
print(os.getcwd())

# Display all files in the cureent working directory
print(os.listdir(os.getcwd()))


countries_GDP = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

countries_LE = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy')


#print(countries_GDP[2][[1,2]][2:])

pd_countriesGDP = countries_GDP[2][[1,2]][2:]
pd_countriesLE = countries_LE[2][[1,2]][1:]

print(pd_countriesGDP)
print("****"*30)
print(pd_countriesLE)



#print(pd_countriesGDP.set_index([1]).join(pd_countriesLE.set_index([1])))

pd_countriesGDP.columns = ['countries', 'gdp']
pd_countriesLE.columns = ['countries', 'le']


# pd_countriesGDP.to_csv('COUNTRIESGDP.csv')
# pd_countriesLE.to_csv('COUNTRIESLE.csv')

countriesGDP = pd.read_csv('COUNTRIESGDP.csv')
countriesLE = pd.read_csv('COUNTRIESLE.csv')

print("****"*30)

print(countriesGDP.drop(columns='i'))
print(countriesLE.drop(columns='i'))

AcountriesGDP = countriesGDP.drop(columns='i')
AcountriesLE = countriesLE.drop(columns='i')


print(pd_countriesGDP)
print("****"*30)
print(pd_countriesLE)
print("****"*30)
print(pd.merge(pd_countriesGDP, pd_countriesLE, on='countries', how='outer'))
print("****"*30)
print(pd.merge(AcountriesGDP, AcountriesLE, on='countries', how='outer'))
print("****"*30)
print(AcountriesGDP.dtypes)
print("****"*30)
print(AcountriesGDP.describe())
print("****"*30)
print(AcountriesLE.dtypes)

combined_dataframe = pd.merge(AcountriesGDP, AcountriesLE, on='countries', how='outer')
print("****"*30)
print(combined_dataframe.describe())
print("*****"*20)
print(combined_dataframe.countries.describe())
print(combined_dataframe.set_index('countries').loc['Somalia',:])
print(combined_dataframe[combined_dataframe['countries']=='Somalia'])


print("*****"*20)
print(combined_dataframe.iloc[:5,:])
print("*****"*20)
print(combined_dataframe.iloc[5:,:])

