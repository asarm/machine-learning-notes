from sklearn.preprocessing import scale
import numpy as np

"""
 z = (x-u)/a   u=> overall mean, a => standard deviation
"""

data = np.array([-12,3,5,6,20])
standardized = scale(data)
print(standardized) 

std = standardized.std(axis=0)# Column standard deviations
print(std)