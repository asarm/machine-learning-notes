import numpy as np
from sklearn.impute import SimpleImputer

arr1 = np.array([[1,3,5,np.nan],[10,14,18,19],[20,34,28,np.nan]])
print(f'{arr1}\n')

imp_mean = SimpleImputer()
transformed = imp_mean.fit_transform(arr1)
print(f"{transformed}\n")

imp_mean = SimpleImputer(strategy="most_frequent")
transformed = imp_mean.fit_transform(arr1)
print(f"{transformed}\n")

imp_constant = SimpleImputer(strategy='constant',
                             fill_value=-1)
transformed = imp_constant.fit_transform(arr1)
print('{}\n'.format(repr(transformed)))
