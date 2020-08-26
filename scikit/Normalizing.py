from sklearn.preprocessing import Normalizer
import numpy as np

#Works on rows

data = np.array([[ 1.2,  3.0],
       [0.3, 1.2],
       [ 6.5, 100.1],
       [ 75.2, 80.4]])

normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
print(f'\n{transformed}')
