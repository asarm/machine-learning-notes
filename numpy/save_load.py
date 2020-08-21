import numpy as np

arr = np.array([1,2,5])

np.save('arr.npy',arr)
np.save('arr', arr)

load_arr = np.load('arr.npy')
print(load_arr)


arr2 = np.array([[1,23,4,8],[3,4,67,8]])
print(np.sum(arr2,axis=1))