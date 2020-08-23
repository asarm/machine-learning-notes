import pandas as pd
import numpy as np

df = pd.DataFrame({
        'ID':['344120','346585','741568','805947','658201'],
        'year':['2018','2017','2018','2020',np.nan],
        'dept':['comp','ie','comp','ee','comp'],
        'age':[21,20,25,19,np.nan]
        })

print(f'{df}\n')

age = df['age'] > 20

print(f'{age}\n')
print(f'{df[age]}\n')
  
dept = df['dept'].str.startswith('c')
print(f'{dept}\n')

dept = df['dept'].str.endswith('e')
print(f'{dept}\n')

dept = df['dept'].str.contains('mp')
print(f'{dept}\n')


isin= df['age'].isin([20])
print(f'{df[isin]}\n')

isna = df['age'].isna()
print(f'{df[isna]}\n')


filt = df[df['age']>20]
age_mean = filt['age'].mean()
print(filt[['dept','age']])  
print(age_mean)