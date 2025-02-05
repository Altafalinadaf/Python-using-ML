import pandas as pd

df =pd.read_csv('C:/Users/HP/Downloads/data1.csv')
#The fillna() method allows us to replace empty cells with number 130

df.fillna(130, inplace=True)
print(df.to_string())

#Replace only for specified colunms
#Replace NULL vslues in the "Calories" columns with the number 130

df['Calories'].fillna(130,inplace=True)
print(df.to_string())