import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:/Users/HP/Downloads/House_data.csv')

print(dataset.shape)
print(dataset.head(5))

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(dataset.area,dataset.price,color='red',marker='*')
plt.show()

#Segregate dataset into input X & output Y

X=dataset.drop('price',axis='columns')
#X
Y=dataset.price
#Y

#Training Dataset using Linear Regression

model = LinearRegression()
model.fit(X,Y)

#predicted price for land sq.Feet of custom value

x=int(input('Enter your area size'))
L=[[x]]
PredictedmodelResult =model.predict(L)
print(PredictedmodelResult)
