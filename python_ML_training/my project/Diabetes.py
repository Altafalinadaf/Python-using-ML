import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#load dataset
dataset = pd.read_csv('C:/Users/altaf/Downloads/train_u6lujuX_CVtuZ9i (1).csv')
#segregate dataset
print(type(dataset))
# printing the first 5 rows of the dataframe
print(dataset.head())

x1=dataset["Gender"].mode()[0]
dataset["Gender"].fillna(x1,inplace=True)

x2=dataset["Married"].mode()[0]
dataset["Married"].fillna(x2,inplace=True)

x3=dataset["Dependents"].mode()[0]
dataset["Dependents"].fillna(x3,inplace=True)

x4=dataset["Self_Employed"].mode()[0]
dataset["Self_Employed"].fillna(x4,inplace=True)

x5=dataset["LoanAmount"].mode()[0]
dataset["LoanAmount"].fillna(x5,inplace=True)

x6=dataset["Loan_Amount_Term"].mode()[0]
dataset["Loan_Amount_Term"].fillna(x6,inplace=True)

x7=dataset["Credit_History"].mode()[0]
dataset["Credit_History"].fillna(x7,inplace=True)


x=dataset.iloc[:,:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)
# Mapping

Married_set=set(dataset['Married'])
dataset['Married']=dataset['Married'].map({'No':0,'Yes':1}).astype(int)
print(dataset.head)

Gender_set=set(dataset['Gender'])
dataset['Gender']=dataset['Gender'].map({'Male':0,'Female':1}).astype(int)
print(dataset.head)

Self_Employed_set=set(dataset['Self_Employed'])
dataset['Self_Employed']=dataset['Self_Employed'].map({'No':0,'Yes':1}).astype(int)
print(dataset.head)

Property_Area_set=set(dataset['Property_Area'])
dataset['Property_Area']=dataset['Property_Area'].map({'Rural':0,'Semiurban':1,'Urban':2}).astype(int)
print(dataset.head)

Education_set=set(dataset['Education'])
dataset['Education']=dataset['Education'].map({'Graduate':1,'Not Graduate':0}).astype(int)
print(dataset.head)



print(dataset.head())

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

#splitting Dataset into Train & Test
from sklearn.model_selection import  train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
print(X_train.shape)
print(X_test.shape)

#Finding best max_depth value

accuracy=[]
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

for i in range(1,10):
    model=DecisionTreeClassifier(max_depth=i,random_state=0)
    model.fit(X_train,Y_train)
    pred=model.predict(X_test)
    score = accuracy_score(Y_test,pred)
    accuracy.append(score)

# #training
# from sklearn.tree import DecisionTreeClassifier
# model=DecisionTreeClassifier(criterion='entropy',max_depth=1,random_state=0)
# model.fit(X_train,Y_train)

# accuracy score
# from sklearn.metrics import accuracy_score
plt.figure(figsize=(12,6))
plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
plt.show()
#Training
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
model.fit(X_train,Y_train)

#prediction
Y_pred = model.predict(X_test)


window=tk.Tk()
window.title("Infidata")
window.geometry('750x750')
window.configure(bg='gray')



l1=tk.Label(window,text='Loan Prediction')
l1.place(x=160,y=20)
l2=tk.Label(window,text='Loan_ID')
l2.place(x=80,y=70)
l3=tk.Label(window,text='Gender')
l3.place(x=80,y=120)
l4=tk.Label(window,text='Married')
l4.place(x=80,y=170)
l5=tk.Label(window,text='Dependents')
l5.place(x=80,y=220)
l7=tk.Label(window,text='Education')
l7.place(x=80,y=270)
l8=tk.Label(window,text='Self_Employed')
l8.place(x=80,y=320)
l9=tk.Label(window,text='ApplicantIncome')
l9.place(x=400,y=70)
l10=tk.Label(window,text='Co-applicantIncome')
l10.place(x=400,y=120)
l11=tk.Label(window,text='LoanAmount')
l11.place(x=400,y=170)
l12=tk.Label(window,text='Loan_Amount_Term')
l12.place(x=400,y=220)
l13=tk.Label(window,text='Credit_History')
l13.place(x=400,y=270)
l14=tk.Label(window,text='Property_Area')
l14.place(x=400,y=320)
txt1=tk.Entry(window,width=10)
txt1.place(x=200,y=70)
txt2=tk.Entry(window,width=10)
txt2.place(x=200,y=120)
txt3=tk.Entry(window,width=10)
txt3.place(x=200,y=170)
txt4=tk.Entry(window,width=10)
txt4.place(x=200,y=220)
txt5=tk.Entry(window,width=10)
txt5.place(x=200,y=270)
txt6=tk.Entry(window,width=10)
txt6.place(x=200,y=320)
txt7=tk.Entry(window,width=10)
txt7.place(x=200,y=70)
txt8=tk.Entry(window,width=10)
txt8.place(x=600,y=70)
txt9=tk.Entry(window,width=10)
txt9.place(x=600,y=120)
txt10=tk.Entry(window,width=10)
txt10.place(x=600,y=170)
txt11=tk.Entry(window,width=10)
txt11.place(x=600,y=220)
txt12=tk.Entry(window,width=10)
txt12.place(x=600,y=270)
txt13=tk.Entry(window,width=10)
txt13.place(x=600,y=320)
def output():
    Loan_ID =int (txt1.get())
    Gender= int(txt2.get())
    Married = int(txt3.get())
    Depedents = int(txt4.get())
    Education = int(txt5.get())
    Self_Employed = int(txt6.get())
    ApplicantIncome = int(txt7.get())
    Co_applicantIncome = int(txt8.get())
    LoanAmount = int(txt9.get())
    Loan_Amount_Term = int(txt10.get())
    Credit_History = int(txt11.get())
    Property_Area = int(txt12.get())
    Loan = [[Loan_ID,Gender,Married,Depedents,Education,Self_Employed,ApplicantIncome,Co_applicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_ID]]
    result = model.predict(Loan)
    print(result)
    Y_pred = model.predict(X_test)

    print(result)
    Y_pred = model.predict(X_test)
    l6 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(Y_test, Y_pred) * 100))
    l6.place(x=160, y=430)
    if result == 1:
        l6 = tk.Label(window, text="person is applicable for loan")
        l6.place(x=160, y=330)



    else:
        l6 = tk.Label(window, text="[0] person is Not applicable for loan ")
        l6.place(x=160, y=330)




b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=350,y=350)


window.mainloop()