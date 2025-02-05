import pandas as pd

df=pd.read_csv('C:/Users/HP/Downloads/data1.csv')

#calculate the mean, and replace any empty values with it
"""
x=df["Calories"].mean()

df["Calories"].fillna(x,inplace=True)

print(df.to_string())
"""

#calculate the median, and replace any empty values with it


"""
x=df["Calories"].median()

df["Calories"].fillna(x,inplace=True)

print(df.to_string())
"""

#calculate the mode, and replace any empty values with it

"""
x=df["Calories"].mode()[0]

df["Calories"].fillna(x,inplace=True)

print(df.to_string())
"""