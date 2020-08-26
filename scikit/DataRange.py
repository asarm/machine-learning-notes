from sklearn.preprocessing import MinMaxScaler
import numpy as np


#•Works on cols
arr = np.array([[ 1.2,  3.0],
       [0.3, 1.2],
       [ 6.5, 10.1],
       [ 2.2, 8.4]])


arr2 = np.array([[ 1.2,  3.8],
       [-0.1, -0.2],
       [ 6.5, 15.1],
       [ 2.0, -4.4]])

print(f'{arr}\n')
scaler = MinMaxScaler()
transformed = scaler.fit_transform(arr)
print(f'\n{transformed}')

transformed = scaler.fit_transform(arr2)
print(f'\n{transformed}')

scaler = MinMaxScaler(feature_range=(0,100))
transformed = scaler.fit_transform(arr)
print(f'\n{transformed}')