import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk

#load dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/salary.csv')

#Mapping salary data to binary value
income_set=set(dataset['income'])
dataset['income']=dataset['income'].map({'<=50K':0,'>50K':1}).astype(int)

#segregate dataset into x(input/independent variable) & y(output/dependent variable)
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#splitting dataset into train & test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

#finding the best K-Value

error=[]
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

#calculating error for K values between 1 and 40
for i in range(1,40):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train,y_train)
    pred_i=model.predict(x_test)
    error.append(np.mean(pred_i !=y_test))

plt.figure(figsize=(12,6))
plt.plot(range(1,40),error,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

#training
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=16,metric='minkowski',p=2)
model.fit(x_train,y_train)

window=tk.Tk()
window.title("Infidata")
window.geometry('750x750')
window.configure(bg='gray')
def clear():

    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    l6.destroy()

l1=tk.Label(window,text='Salary Predictor')
l1.place(x=160,y=20)
l2=tk.Label(window,text='Age')
l2.place(x=80,y=70)
l3=tk.Label(window,text='Education')
l3.place(x=80,y=120)
l4=tk.Label(window,text='Capital')
l4.place(x=80,y=170)
l5=tk.Label(window,text='Hours')
l5.place(x=80,y=220)
txt1=tk.Entry(window,width=10)
txt1.place(x=200,y=70)
txt2=tk.Entry(window,width=10)
txt2.place(x=200,y=120)
txt3=tk.Entry(window,width=10)
txt3.place(x=200,y=170)
txt4=tk.Entry(window,width=10)
txt4.place(x=200,y=220)

def output():
    global l6
    age = int(txt1.get())
    edu = int(txt2.get())
    cg = int(txt3.get())
    wh = int(txt4.get())
    newEmp = [[age, edu, cg, wh]]
    result = model.predict(sc.transform(newEmp))
    if result == 1:
        l6 = tk.Label(window, text="Employee might get Salary above 50K")
        l6.place(x=160, y=330)
    else:
        l6 = tk.Label(window, text="Employee might get Salary below 50K")
        l6.place(x=160, y=330)


b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=160,y=270)
b2=tk.Button(window,text='clear',height=1,width=7,command=clear)
b2.place(x=240,y=270)

window.mainloop()