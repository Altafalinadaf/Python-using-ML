import pandas as pd
df = pd.read_csv('C:/Users/HP/Downloads/data.csv')

#Get a quick overview by printing the first 10 rows of the dataFrame

print('Accessing from the data set first 10 rows:\n',df.head(20))
print('Accessing from the data set first 5 rows:\n',df.head())

#Tail
print('Accessing from the data set first 10 rows:\n',df.tail())#5 rows
print('Accessing from the data set first 10 rows:\n',df.tail(10))# 10 rows
