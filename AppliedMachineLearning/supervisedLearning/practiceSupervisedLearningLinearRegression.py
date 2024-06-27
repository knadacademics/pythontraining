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
from sklearn.model_selection import cross_val_score

import pylab
from sklearn.metrics._regression import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.model_selection._validation import cross_validate




housing_dataset = pd.read_csv('C:/Users/kwabe/OneDrive/CLARK UNIVERSITY TEACHING/Applied Machine Learning_2024/Dataset/BostonHousing.csv')

#seeing the data
print(housing_dataset.head())

print(housing_dataset.isnull().sum())

#Exploratory Data Analysis

#checking the distribution of the target value
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.displot(housing_dataset['medv'], bins=30)

##checking the linear relationships between the variables

correlation_matrix = housing_dataset.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True)

#selecting RM and LSTAT as features

plt.figure(figsize=(20,5))

features = ['lstat', 'rm']
target = housing_dataset['medv']

for i, col in enumerate(features):
    plt.subplot(1,len(features),i+1)
    x = housing_dataset[col]
    y = target 
    plt.scatter(x, y, marker = 'o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('medv')

#plt.show()


#preparing the data for training the model
X = pd.DataFrame(np.c_[housing_dataset['lstat'],housing_dataset['rm']],columns=['lstat','rm'])
Y = housing_dataset['medv']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


#training and testing the model
lin_model = LinearRegression()
lin_model.fit(X_train,Y_train)


#model evaluation for training set
y_train_predict = lin_model.predict(X_train)

rmse = (np.sqrt(mean_squared_error(Y_train,y_train_predict)))

mse = mean_squared_error(Y_train,y_train_predict)

r2 = r2_score(Y_train,y_train_predict)


print("The Model performance for training set")
print("---------------------------------------")
print('RMSE is {}'.format(rmse))
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

#model evaluation for testing set
y_test_predict = lin_model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(Y_test,y_test_predict)))

mse = mean_squared_error(Y_test,y_test_predict)
r2 = r2_score(Y_test,y_test_predict)

print("The Model performance for testing set")
print("-------------------------------------")
print('RMSE is {}'.format(rmse))
print('mse is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

#applying cross validation to improve the model with k = 10
pipeline = make_pipeline(StandardScaler(),LinearRegression())
score_pipe = cross_val_score(pipeline, X_train, Y_train, cv = 10)

print(score_pipe.mean())