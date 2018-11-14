import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

# countries_GDP = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

# countries_LE = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy')

# countries_POP = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)')


# countriesGDP = countries_GDP[2][[1,2]][2:]

# countriesLE = countries_LE[2][[1,2]][1:]

# countriesPOP = countries_POP[2][[1,2,3,4]][2:]

# countriesGDP.to_csv('UN_GDP.csv')
# countriesLE.to_csv('UN_LE.csv')
# countriesPOP.to_csv('UN_POP.csv')

pd_ungdp = pd.read_csv('UN_GDP.csv')
pd_unle = pd.read_csv('UN_LE.csv')
pd_unpop = pd.read_csv('UN_POP.csv')

pd_ungdp.columns = ['i', 'countries', 'gdp']
pd_unle.columns = ['i', 'countries', 'le']
pd_unpop.columns = ['i', 'countries', 'UN continental region', 'UN statistical region', 'pop']

pd_ungdp.drop("i", inplace=True, axis=1)
pd_unle.drop("i", inplace=True, axis=1)
pd_unpop.drop("i", inplace=True, axis=1)

pd_ungdp_unle = pd.merge(pd_ungdp, pd_unle, on='countries', how='inner')
pd_ungdp_unle_pop = pd.merge(pd_ungdp_unle, pd_unpop, on='countries', how='inner')
print(pd_ungdp_unle)
print("*****"*20)
print(pd_ungdp_unle_pop)

np_gdp = np.array(pd_ungdp_unle_pop['gdp'])
np_le = np.array(pd_ungdp_unle_pop['le'])
np_pop= np.array(pd_ungdp_unle_pop['pop'])

plt.scatter(np_gdp, np_le)
plt.show()





