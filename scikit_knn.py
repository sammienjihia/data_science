import pandas as pd 
import numpy as np 
from sklearn import datasets
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Using the iris data set from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# The dataset consists of four attributes: sepal-width, sepal-length, petal-width and petal-length

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

pd_data = pd.read_csv(url, names=column_names)

# Output the dataframe
print(pd_data)

# PREPROCESSING
# Split the dataset into it's attributes and labels

dataset_features = pd_data.iloc[:,:-1]
dataset_labels = pd_data.iloc[:,4]

# Output your features and labels
print(dataset_features)
print(dataset_labels)

# TRAIN TEST SPLIT
# Split your datasets into training_set and test_set by a given ratio
dataset_features_train, dataset_features_test, dataset_labels_train, dataset_labels_test = train_test_split( dataset_features, dataset_labels, test_size=0.20)

# Check your data
print(dataset_features_train)

# FEATURE SCALING
# Normalize your training data set to remove outliers. The outliers can affect the performance of the model

"""
Explanation from Wikipedia

Since the range of values of raw data varies widely, in some machine learning algorithms, objective functions will not work 
properly without normalization. For example, the majority of classifiers calculate the distance between two points by the 
Euclidean distance. If one of the features has a broad range of values, the distance will be governed by this particular 
feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately 
to the final distance.
"""
scaler = StandardScaler()
scaler.fit(dataset_features_train)

dataset_features_train = scaler.transform(dataset_features_train)
dataset_features_test = scaler.transform(dataset_features_test)


# TRAINING AND PREDICTION

# Assign the classifier class and add the number of neigbors (Value of K)

classifier = KNeighborsClassifier(n_neighbors=5)

# Train your data set
classifier.fit(dataset_features_train, dataset_labels_train)

# Predict your test data set
predicted_label = classifier.predict(dataset_features_test)

# Output your predicted labels
print(predicted_label)


# EVALUATING THE MODEL/CLASSIFIER
# For evaluation , the confusion matrix , precision and recall are the most considered metrices

prediction_report = classification_report(dataset_labels_test, predicted_label)

prediction_matrix = confusion_matrix(dataset_labels_test, predicted_label)

print(prediction_matrix)
print(prediction_report)

# Iris-virginica has a precision of 0.88 and a recall of 1.00 meaning 
# the model can predict iris-virgnica correctly 88% of the time and correclty predicted 100% of iris-virgnica

error = []
for i in range(1,40):
	knn = KNeighborsClassifier(n_neighbors=i)
	knn.fit(dataset_features_train, dataset_labels_train)
	pred_i  = knn.predict(dataset_features_test)
	error.append(np.mean(pred_i !=dataset_labels_test))


plt.figure(figsize=(12, 6))  
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',  
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')  
plt.xlabel('K Value')  
plt.ylabel('Mean Error')  

plt.show()



























