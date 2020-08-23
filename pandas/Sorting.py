import pandas as pd
import numpy as np
df = pd.DataFrame({
        'ID':['344120','346585','741568','805947','658201'],
        'year':['2018','2017','2018','2020',np.nan],
        'dept':['comp','ie','comp','ee','comp'],
        'age':[21,20,25,19,np.nan]
        })

sort1 = df.sort_values('age')
print(f'{sort1}\n')

sort2 = df.sort_values('age',ascending=False)
print(f'{sort2}\n') 

sort3 = df.sort_values(['ID', 'age'],
                       ascending=[True, False])
print(f'{sort3}\n') 

