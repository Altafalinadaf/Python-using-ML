import pandas as pd

df=pd.read_csv('C:/Users/HP/Downloads/data1.csv')

df['Date']=pd.to_datetime(df['Date'])

df.dropna(subset=['Date'],inplace=True)

x=df["Calories"].median()

df["Calories"].fillna(x,inplace=True)
df.fillna(130, inplace=True)

df['Calories'].fillna(130,inplace=True)

new_df=df.dropna()
df.loc[7,'Duration']= 45
print(df.to_string())

