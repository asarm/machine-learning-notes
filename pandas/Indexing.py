import pandas as pd

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])

col1 = df['c1']
print(f'{col1}\n')

col1_df = df[['c1']]
print(f'{col1_df}\n')

col12_df = df[['c1','c2']]
print(f'{col12_df}\n')


r12 = df[0:2]
print(f'{r12}\n')

r_last2 = df['r1':'r2']
print(f'{r_last2}\n')


# use 'iloc' to access row based on index
print(f'{df.iloc[0]}\n')

print("True-False:")
bool_list = [False, True]
print('{}\n'.format(df.iloc[bool_list]))

# use 'loc' to access row based on label
print(f"{df.loc['r1']}\n")

print(f"{df.loc[['r1','r2'],'c1']}\n")

print(f"{df.loc['r1','c1']}\n") #row,col
