import numpy as np
import pandas as pd

series = pd.Series([1,2,3,4.6])
arr = np.array([1,2,3,4])

print(f'\n{series}')
print(f'\n{arr}')

series = pd.Series([1,2,3,4.6],index=["a","b","c","d"])
print(f'\n{series}')

series = pd.Series({'a':1,'b':2,'c':3,'d':4.6})
print(f'\n{series}')
