import pandas as pd

df=pd.read_csv('C:/Users/HP/Downloads/data1.csv')
df.loc[7,'Duration']= 45
print(df.to_string())