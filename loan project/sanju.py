import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#load dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/healthcare-dataset-stroke-data.csv')

# number of missing values in each column
print(dataset.isnull().sum())

#Mapping Function
gender_set=set(dataset['gender'])
dataset['gender']=dataset['gender'].map({'Male':0,'Female':1,'Other':2}).astype(int)
print(dataset.head)

ever_married_set=set(dataset['ever_married'])
dataset['ever_married']=dataset['ever_married'].map({'Yes':0,'No':1}).astype(int)
print(dataset.head)


work_type_set=set(dataset['work_type'])
dataset['work_type']=dataset['work_type'].map({'Private':0,'Never_worked':1,'Self-employed':2,'Govt_job':3,'children':4}).astype(int)
print(dataset.head)

Residence_type_set=set(dataset['Residence_type'])
dataset['Residence_type']=dataset['Residence_type'].map({'Urban':0,'Rural':1}).astype(int)
print(dataset.head)

smoking_status_set=set(dataset['smoking_status'])
dataset['smoking_status']=dataset['smoking_status'].map({'formerly smoked':0,'never smoked':1,'Unknown':2,'smokes':3}).astype(int)
print(dataset.head)



x=dataset.iloc[:,1:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)


#splitting as train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

#finding best max_depth value
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
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=1,random_state=0)
model.fit(x_train,y_train)


y_pred = model.predict(x_test)
# accuracy score
from sklearn.metrics import accuracy_score

#print("Accuracy of the Model:{0}%".format(accuracy_score(y_test,y_pred)*100))


window=tk.Tk()
window.title("Infidata")
window.geometry('750x750')
window.configure(bg='gray')
load = Image.open('C:/Users/altaf/Downloads/loan.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image = render)
img.place(x=0,y=0)



l1=tk.Label(window,text='sanju ka pain',bg='yellow',width=50,height=1,font=('Times New Roman',15))
l1.place(x=80,y=40)
l2=tk.Label(window,text='gender',bg='orange',font=('Times New Roman',12))
l2.place(x=80,y=120)
l3=tk.Label(window,text='age',bg='orange',font=('Times New Roman',12))
l3.place(x=80,y=170)
l4=tk.Label(window,text='hypertension',bg='orange',font=('Times New Roman',12))
l4.place(x=80,y=220)
l5=tk.Label(window,text='heart_disease',bg='orange',font=('Times New Roman',12))
l5.place(x=80,y=270)
l6=tk.Label(window,text='ever_married',bg='orange',font=('Times New Roman',12))
l6.place(x=400,y=120)
l7=tk.Label(window,text='work_type',bg='orange',font=('Times New Roman',12))
l7.place(x=400,y=170)
l8=tk.Label(window,text='Residence_type',bg='orange',font=('Times New Roman',12))
l8.place(x=400,y=220)
l9=tk.Label(window,text='smoking_status',bg='orange',font=('Times New Roman',12))
l9.place(x=400,y=270)

txt1=tk.Entry(window,width=10)
txt1.place(x=200,y=120)
txt2=tk.Entry(window,width=10)
txt2.place(x=200,y=170)
txt3=tk.Entry(window,width=10)
txt3.place(x=200,y=220)
txt4=tk.Entry(window,width=10)
txt4.place(x=200,y=270)
txt5=tk.Entry(window,width=10)
txt5.place(x=600,y=270)
txt6=tk.Entry(window,width=10)
txt6.place(x=600,y=120)
txt7=tk.Entry(window,width=10)
txt7.place(x=600,y=170)
txt8=tk.Entry(window,width=10)
txt8.place(x=600,y=220)

def clear():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    txt8.delete(0, END)
    l12.destroy()
    l13.destroy()
def output():
    global l12
    global l13
    gender = int(txt1.get())
    age = int(txt2.get())
    hypertension = int(txt3.get())
    heart_disease = int(txt4.get())
    ever_married = int(txt5.get())
    work_type = int(txt6.get())
    Residence_type = int(txt7.get())
    smoking_status = int(txt8.get())

    stroke = [[gender,age,heart_disease,ever_married,work_type,Residence_type,smoking_status]]
    result = model.predict(stroke)
    print(result)
    y_pred = model.predict(x_test)

    l13 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(y_test, y_pred) * 100),width=40,height=2,bg='pink')
    l13.place(x=160, y=460)

    if result == 0:
        l12 = tk.Label(window, text=" Person have Stroke",width=40,height=2,bg='brown')
        l12.place(x=160, y=420)



    else:
        l12 = tk.Label(window, text="Person donot have Stroke",width=40,height=2,bg='brown')
        l12.place(x=160, y=420)


b1 = tk.Button(window, text='Predict', height=1, width=7, command=output,bg='blue')
b1.place(x=350, y=350)
b2=tk.Button(window,text='Clear',height=1,width=7,command=clear,bg='red')
b2.place(x=350,y=380)

window.mainloop()

