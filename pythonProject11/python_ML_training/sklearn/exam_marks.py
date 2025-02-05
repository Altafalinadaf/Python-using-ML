import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:/Users/HP/Downloads/Exam_marks.csv')

print(dataset.shape)
print(dataset.head(5))

x=dataset['hours'].median()

dataset['hours'].fillna(x,inplace=True)
#print(dataset.to_string())

#Segregate dataset into input x & output y
x=dataset.iloc[:,:-1].values
print(x.shape)

y=dataset.iloc[:,-1]
print(y.shape)


#Training dataset using linear regression
model=LinearRegression()
model.fit(x,y)

#Predicted price for Land sq.Feet of custom values
a=[[9.2,20,0]]
PredictemodelResult=model.predict(a)
print("Predicted Result :",PredictemodelResult)