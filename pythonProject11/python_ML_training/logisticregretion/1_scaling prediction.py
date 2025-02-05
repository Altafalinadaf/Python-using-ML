import numpy as np
import pandas as pd

dataset = pd.read_csv('C:/Users/HP/Downloads/sales_data.csv')

print(dataset.shape)
print(dataset.head(5))

# saperating variables - dependent and independent
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values
# print(X.shape)
# print(Y.shape)
# print(X)


# spliting data for Training and Testing..
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#training
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state=0)
model.fit(X_train,Y_train)

#predicting,wheather new customer with age & salary will buy or not

# age=int(input("Enter New Customer Age: "))
# sal=int(input("Enter New Customer Salary: "))
# newCust=[[age,sal]]
# result=model.predict(sc.transform(newCust))
# print(result)
# if result==1:
#     print("Customer will Buy")
#
# else:
#     print("Customer won't Buy")

#prediction for all test data
Y_pred = model.predict(X_test)
#print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y_test.reshape(len(Y_test),1)),1))

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix:")
print(cm)

print("Accuricy of the Model:{0}%".format(accuracy_score(Y_test,Y_pred)*100))

