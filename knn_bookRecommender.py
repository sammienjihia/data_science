"""
This is a book recommender system built using The K Nearest Neighbor Algorithm, SciKitLearn, numpy and Pandas python packages

The resources for this Exercise can be found at https://datascienceplus.com/building-a-book-recommender-system-the-basics-knn-and-matrix-factorization/

The data set is Book-Crossing http://www2.informatik.uni-freiburg.de/~cziegler/BX/
"""


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# Skipped bad lines using the error_bad_lines argument in read_csv(). This csv is encoded using the latin-1 encoder, the delimiter is ;
pd_BookRatings = pd.read_csv('BX-CSV-Dump/BX-Book-Ratings.csv', delimiter=';', error_bad_lines=False, encoding='latin-1')

pd_Books = pd.read_csv('BX-CSV-Dump/BX-Books.csv', delimiter=';', encoding='latin-1', error_bad_lines=False)

pd_Users = pd.read_csv('BX-CSV-Dump/BX-Users.csv', delimiter=';', encoding='latin-1', error_bad_lines=False)

# join the data frames using the isbn and the user id
pd_combined1 = pd.merge(pd_BookRatings, pd_Books, on='ISBN', how='left')
pd_combined2 =pd.merge(pd_combined1, pd_Users, on='User-ID', how='left')


# pd_combined2['Book-Rating'].value_counts(sort=False).plot(kind='bar')
# plt.xlabel("Ratings")
# plt.ylabel("Count")
# plt.title("Rating Distribution")
# plt.savefig('BookRating_distribution.png', bbox_inches='tight')

# The book ratings are unevenly distributed with majority having a 0 rating

# pd_combined2['Age'].hist(bins=[0,10,20,30,40,50,60,70,80,100])
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.title('Age Distribution')
# plt.savefig('Age_distribution.png', bbox_inches='tight')
# plt.show()

# Recommendations based on ratings count

# This script selects 5 Book-Ratings with the highest count
recommendations = pd_combined2['Book-Rating'].value_counts(sort=True).head()
# print(recommendations)

# recommendations2 = pd_combined2[['Book-Rating','ISBN']].groupby('ISBN')['Book-Rating'].value_counts()
# print(recommendations2.sort_values('Book-Rating', ascending=False).head())

# rating_count = pd.DataFrame(pd_combined2.groupby('ISBN')['Book-Rating'].count())
# print(rating_count.sort_values('Book-Rating', ascending=False).head())

print(pd_combined2[['ISBN','Book-Rating']].groupby('ISBN')['Book-Rating'].count().sort_values(ascending=False).head())
print("****"*10)
print(pd_combined2[['ISBN','Book-Rating']].groupby('ISBN').count().sort_values('Book-Rating', ascending=False).head())