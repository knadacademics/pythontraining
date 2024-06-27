import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

from sklearn.datasets import fetch_california_housing
import pylab


housing_dataset = pd.read_csv('C:/Users/kwabe/OneDrive/CLARK UNIVERSITY TEACHING/Applied Machine Learning_2024/Dataset/housing.csv')

#showing random 5 samples
print(housing_dataset.sample(5))

#shape of the dataset
print(housing_dataset.shape)

#checking for missing data
print(housing_dataset.isna().sum())

#dropping the missing data
housing_dataset = housing_dataset.dropna()

#the shape after dropping
print(housing_dataset.shape)

#checking the shape again
print(housing_dataset.isna().sum())

#exploring the categorical data
print(housing_dataset['ocean_proximity'].unique())

#using OHE
housing_dataset = pd.get_dummies(housing_dataset,columns=['ocean_proximity'])

print(housing_dataset.head())


#printing
print('showing correlation')
housing_dataset_correlation = housing_dataset.corr()

print(housing_dataset_correlation)

#housing dataset correlation in heat map
plt.figure(figsize=(15,12))
sns.heatmap(housing_dataset_correlation, annot=True)
pylab.show()

#extracting the data
X = housing_dataset.drop('median_house_value', axis=1)
Y = housing_dataset['median_house_value']

#splitting the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2, random_state=45)

