import pandas as pd
import numpy as np

#load dataset
dataset=pd.read_csv('C:/Users/HP/Downloads/titanicsurvival.csv')
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
#training

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)

#predicting, wheather Person survived or not

pclassNo =int(input("Enter person's Pclass number: "))
Gender=int(input("Enter Person's Gender 0-female 1-male:"))
age=int(input("Enter Person's Age:"))
fare=int(input("Enter Person's Fare:"))
person =[[pclassNo,Gender,age,fare]]
result=model.predict(person)
print(result)

if result ==1:
    print("Person might be survived")
else:
    print("Person might not be survived")

#Prediction for all Test Data
y_pred=model.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

#Evaluating Model-CONFUSION MATRIX
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print("confusion Matrix:")
print(cm)
print("Accuracy of the Model:{0}%".format(accuracy_score(y_test,y_pred)*100))