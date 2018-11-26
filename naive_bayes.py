import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# Gaussioan Naive Bayes
"""
This Naive bayes classifier assumes that the data from each label is drawn from a Gaussian distributin e.i a normal distribution
 The frequency distribution forms a bell curve
"""

from sklearn import datasets 
from sklearn.model_selection import train_test_split

iris_data = datasets.load_iris()

# The X variable carries the features while the y variable carries the labels

X = iris_data.data
y = iris_data.target

# Using the sklearn train test split function to split the data into training data and test data

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

# Initia lize the Gaussian naive bayes classifier
classifier = GaussianNB()

# Train your model/Classifier
# Nb Training invlovles mapping your features to your target values
classifier.fit(X_train,y_train)

# Use your test data to predict
y_predicted = classifier.predict(X_test)

# Check the accuracy of your classifier using the accuracy_score
# If normalize == True return the fruction of correctly classified samples, else if False return the number of samples that are correctly classified
print(accuracy_score(y_test, y_predicted, normalize=False))
print("***"*10)
print(accuracy_score(y_test, y_predicted, normalize=True))
print(len(X_test))

"""
Output
44 This is the number of correclty classified samples
******************************
0.9777777777777777 This is a fraction of the correctly classified samples
45 This the number of the test samples

Thus the model has an accuracy of 97%

"""

print(classification_report(y_test, y_predicted))



