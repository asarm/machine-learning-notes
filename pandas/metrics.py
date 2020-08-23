import pandas as pd
import numpy as np
df = pd.DataFrame({
        'ID':['344120','346585','741568','805947','658201'],
        'year':['2018','2017','2018','2020',np.nan],
        'dept':['comp','ie','comp','ee','comp'],
        'age':[21,20,25,20,np.nan]
        })

print(f'{df.describe()}\n') 

per = df.describe(percentiles=[.105,.5,.65]) #.105 = %10.5
print(f'{per}\n') 

count = df['dept'].value_counts()
print(f'{count}\n') 

count = df['age'].value_counts(normalize=True)
print(f'{count}\n') 


unique_depts = df['dept'].unique()
print(f'{unique_depts}\n') 
