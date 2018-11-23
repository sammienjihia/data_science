import pandas as pd 
import numpy as np 
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import GaussianNB
# python requests library can download web pages
import requests
from bs4 import BeautifulSoup

# can't find a csv dataset of the golf dataset, so i just have to scrape the dataset from
# https://gerardnico.com/data_mining/weather

golf_url = 'https://gerardnico.com/data_mining/weather'

"""
pandas cannot access this site so we just have to use the requests lib and BeautifulSoup
"""
# golf_data = pd.read_html(golf_url) 
# Lets get that page from the above url 
dataset_page = requests.get(golf_url)

# if status code 200 then download was successful

# Parsing the content with beautiful soup

soup = BeautifulSoup(dataset_page.content, 'html.parser')

print(soup.table)
