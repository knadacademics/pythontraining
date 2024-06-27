import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
import pylab

mean = 128
std = 11
data = np.random.normal(mean,std, 1000)
data2 = data.reshape(1,-1)
scaled_data = StandardScaler().fit_transform(data2)

print(scaled_data)
