import pandas as pd
import numpy as np

df = pd.DataFrame({'color':['red','blue','green','red','red','blue']})
df_indicator = pd.DataFrame({'blue':[0,1,0,0,0,1],'red':[1,0,0,1,1,0],'green':[0,0,1,0,0,0]})

converted = pd.get_dummies(df_indicator)
print(converted.columns)
print(converted[['blue','green']])

n_matrix = df.values
print(n_matrix)