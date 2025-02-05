import pandas as pd
import numpy as np

#load dataset
dataset=pd.read_csv('C:/Users/HP/Downloads/employee_promotion.csv')

print(dataset.columns[dataset.isna().any()])

x1=dataset["education"].mode()[0]
dataset["education"].fillna(x1,inplace=True)

x2=dataset["previous_year_rating"].mode()[0]
dataset["previous_year_rating"].fillna(x2,inplace=True)

x3=dataset["avg_training_score"].mode()[0]
dataset["avg_training_score"].fillna(x3,inplace=True)


education_set=set(dataset['education'])
dataset['education']=dataset['education'].map({"Master's & above":0,"Bachelor's":1,"Below Secondary":2}).astype(float)
print(dataset.head)

gender_set=set(dataset['gender'])
dataset['gender']=dataset['gender'].map({"f":0,"m":1}).astype(float)
print(dataset.head)


recruitment_channel=set(dataset['recruitment_channel'])
dataset['recruitment_channel']=dataset['recruitment_channel'].map({"sourcing":0,"other":1,"referred":2}).astype(float)
print(dataset.head)



#segregate dataset into X(Input/Indenpendent variable)&Y(output/DependentVariable)
x=dataset.iloc[:,3:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)

#Splitting Dataset into Train and Test

from sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

#Finding best max_depth value
accuracy=[]
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

for i in range(1,10):
    model=DecisionTreeClassifier(max_depth=i,random_state=0)
    model.fit(x_train,y_train)
    pred=model.predict(x_test)
    score=accuracy_score(y_test,pred)
    accuracy.append(score)

#training

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test = sc.transform(x_test)


#predicting, wheather Person survived or not

edu=int(input("Enter Employee's Education: "))
g=int(input("Enter  Employee's gender: "))
rc=int(input("Enter Employee's recruitment_channel: "))
tr=int(input("Enter Employee's no_of_trainings: "))
age=int(input("Enter Employee's age: "))
pyr=int(input("Enter Employee's previous_year_rating: "))
ls=int(input("Enter Employee's length_of_service: "))
aw=int(input("Enter Employee's awards_won: "))
ats=int(input("Enter Employee's avg_training_score: "))

newEMp=[[age,edu,g,rc,tr,pyr,ls,aw,ats]]
result = model.predict(sc.transform(newEMp))
print(result)

if result==1:
    print("Employee might get promotion")
else:
    print("Employee might Not get promotion")


#Prediction for all Test Data
y_pred = model.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

#Evaluating Model-CONFUSION MATRIX
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print("confusion Matrix:")
print(cm)
print("Accuracy of the Model:{0}%".format(accuracy_score(y_test,y_pred)*100))