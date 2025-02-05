#plant species detection
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

#load dataset

dataset=load_iris()
#summarize dataset

print(dataset.data)
print(dataset.target)
print("Shape",dataset.data.shape)

X = pd.DataFrame(dataset.data,columns=dataset.feature_names)
#X
Y=dataset.target
#Y
#splitting Dataset into Train & Test
from sklearn.model_selection import  train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
print(X_train.shape)
print(X_test.shape)

#Finding best max_depth value

accuracy=[]
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

for i in range(1,10):
    model=DecisionTreeClassifier(max_depth=i,random_state=0)
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    score = accuracy_score(y_test,pred)
    accuracy.append(score)

plt.figure(figsize=(12,6))
plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
plt.show()

#Training
from sklearn.tree import DecisionTreeClassifier
model =DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
model.fit(X_train,y_train)

#prediction
Y_pred = model.predict(X_test)
#print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import accuracy_score
print("Accuracy of the Model:{0}%".format(accuracy_score(y_test,Y_pred)*100))
