from sklearn.preprocessing import RobustScaler
import numpy as np

#Works on cols

arr = np.array([[ 1.2,  3.0],
       [0.3, 1.2],
       [ 5, 10.1],
       [ 2.2, 80.4]])

robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(arr)
print(f'\n{transformed}')
