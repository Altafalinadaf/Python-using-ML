import pandas as pd
import numpy as np

#load dataset
dataset=pd.read_csv('C:/Users/HP/Downloads/titanicsurvival.csv')

#2..Load summarize
print(dataset.shape)  #prints rows and columns
print(dataset.head(5)) #from the top it prints 5 rows

#Mapping survival to Binary value
Sex_set=set(dataset['Sex'])
dataset['Sex']=dataset['Sex'].map({'male':0,'female':1}).astype(int)
print(dataset.head)

x=dataset["Age"].mode()[0]
dataset["Age"].fillna(x,inplace=True)
print(dataset.to_string())

#segregate dataset into X(Input/Indenpendent variable)&Y(output/DependentVariable)
X=dataset.iloc[:,:-1].values
print(X.shape)
Y=dataset.iloc[:,-1].values
print(Y.shape)

#Splitting Dataset into Train and Test
from sklearn.model_selection import  train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Finding the best K-value
error=[]
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#calculating error for k values between 1 and 40
for i in range(1,40):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train,y_train)
    pred_i=model.predict(X_test)
    error.append(np.mean(pred_i !=y_test))
plt.figure(figsize=(12,6))
plt.plot(range(1,40),error,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.title('Error Rate K value')
plt.xlabel('K value')
plt.ylabel('Mean Error')
plt.show()

#Training
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=4,metric='minkowski',p=2)
model.fit(X_train,y_train)

#Predicting, wheather new customer with Age and Salary will Buy or Not
Pclass=int(input("Enter Persons Pclass:"))
sex=int(input("Enter Persons Sex:"))
age=int(input("Enter Persons Age:"))
fare=int(input("Enter Persons Fare:"))
newEmp=[[Pclass,sex,age,fare]]
result=model.predict(sc.transform(newEmp))
print(result)
if result==1:
    print("Person might get survived")
else:
    print("Person might not get survived")
#Prediction for all Test Data
y_pred=model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))
#Evaluating Model-CONFUSION MATRIX
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print("confusion Matrix:")
print(cm)
print("Accuracy of the Model:{0}%".format(accuracy_score(y_test,y_pred)*100))