import numpy as np

arr1 = np.array([[4,1,3,2],[5,6,7,8],[0,2,3,1]])
print(arr1)
print()
print(arr1[:,1:])

#Print index of min-max element
print(np.argmin(arr1[0]))
print(np.argmax(arr1))

#axis = 0 means col, axis = 1 means row, -1 means cross
print(np.argmax(arr1,axis=-1)) 
print(np.argmax(arr1,axis=1)) 
print(np.argmax(arr1,axis=0)) 
