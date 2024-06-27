#load library
import numpy as np 

#create a vector as a row
vector_row = np.array([1,2,3])

#create a vector as a column 
vector_column = np.array([[1],
                          [2],
                          [3]
                        ])


#creating a vector of zeroes
vector = np.zeros(shape=5)
print(vector)


#matrix with shape (3,3)
matrix = np.full(shape=(3,3), fill_value = 1)

#view the vector
print(matrix)

print('')


vector = np.array([1,2,3,4,5,6])

#create matrix
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]
                 ])


#third vector element
print()