# -*- coding: utf-8 -*-
import numpy as np

array1 = np.array([0,1,3,5,6,-1],dtype=np.float32)


#array1 ve array2 birlikte değişir
"""array2 = array1
array2[0] = 5
print(array1)"""

#array1 etkilenmez
array2 = array1.copy()
array2[0] = 10
print(array1)
print(array2)


print(f"Array1 [0] = {array2[0]}")
print(f"Array2 [0] = {array2[0]}") 


#casting
array1.astype(np.int32)

#we can use np.nan to act as a placeholder. A common usage for np.nan is as a filler value for incomplete data.
array1[0] = np.nan

#To represent infinity in NumPy, we use the np.inf special value.
array1[1] = np.Infinity
array1[2] = -np.Infinity

print(array1)

matrix = np.array([[1,2,3], [4,5,6]], dtype = np.float32)
print(matrix)