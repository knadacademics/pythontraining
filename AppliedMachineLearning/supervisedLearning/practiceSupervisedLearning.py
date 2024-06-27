'''
Created on Dec 14, 2023

@author: kwabe
'''

if __name__ == '__main__':
    pass

from sklearn import datasets

import numpy as np
import pandas as pd 


#load the diabetest dataset
diabetes_all = datasets.load_diabetes(return_X_y=False, as_frame=True)

print(diabetes_all)

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True, as_frame=True)

#print(diabetes_X.head())
#print(diabetes_y.head())

#use only the BMI feature
diabetes_X = diabetes_X.loc[:,['bmi']]

#The BMI is zero-centered and normalized; recenter for ease or presentation
diabetes_X = diabetes_X * 30 + 25

#collect 20 data points
diabetes_X_train = diabetes_X.iloc[-20:]
diabetes_y_train = diabetes_y.iloc[-20:]

#display some of the data points
print(pd.concat([diabetes_X_train,diabetes_y_train],axis=1).head())







