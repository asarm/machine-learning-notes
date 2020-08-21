import pandas as pd

df = pd.DataFrame([1,5,8],columns=["first col"],index=["a","b","c"])
ser = pd.Series([30,40,50],name="new row")
print(df)

#Appending new row
print(f'\n{df.append(ser)}')

#Drop
df = df.append(ser)
df_drop1 = df.drop(labels='b') #drop row
print(f'\n{df_drop1}')

df_drop2 = df.drop(labels = 1,axis=1) #drop col 
print(f'\n{df_drop2}')