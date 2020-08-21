import pandas as pd

df1 = pd.DataFrame({'c1':[1,2],'c2':[3,4]},index=['r1','r2'])

df2 = pd.DataFrame({'c3':[5,6],'c4':[7,8]},index=['r1','r2'])
 
df3 = pd.DataFrame({'c1':[9,10],'c2':[11,12]},index=['r3','r4'])

concat = pd.concat([df1,df2],axis=1) #for cols
print(f'{concat}\n')

concat = pd.concat([df1,df3 ]) #for rows (default axis=0)
print(f'{concat}\n')



#combines common columns
mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})
                        
print('{}\n'.format(mlb_df1))
print('{}\n'.format(mlb_df1))

mlb_merged = pd.merge(mlb_df1, mlb_df2)
print('{}\n'.format(mlb_merged))