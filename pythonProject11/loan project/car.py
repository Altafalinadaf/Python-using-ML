import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw

#load dataset
dataset = pd.read_csv('C:/Users/altaf/Downloads/car.csv')
print(dataset.columns[dataset.isna().any()])
print(dataset.shape)
print(dataset.head(5))

#mapping
buying_price_set=set(dataset['buying prices'])
dataset['buying prices']=dataset['buying prices'].map({'vhigh':0,'high':1,'med':2,'low':3}).astype(int)
print(dataset.head)

mainrenance_cost_set=set(dataset['maintenance cost'])
dataset['maintenance cost']=dataset['maintenance cost'].map({'vhigh':0,'high':1,'med':2,'low':3}).astype(int)
print(dataset.head)

# number_0f_doors_set=set(dataset['number of doors'])
# dataset['number of doors']=dataset['number of doors'].map({'2':0,'3':1,'4':2,'5more':3}).astype(int)
# print(dataset.head)
#c
# number_0f_persons_set_set=set(dataset['number of persons'])
# dataset['number of persons']=dataset['number of persons'].map({'2':0,'4':1,'more':2}).astype(int)
# print(dataset.head)

lug_boot_set=set(dataset['lug_boot'])
dataset['lug_boot']=dataset['lug_boot'].map({'small':0,'med':1,'big':2}).astype(int)
print(dataset.head)

safety_set=set(dataset['safety'])
dataset['safety']=dataset['safety'].map({'low':0,'med':1,'high':2}).astype(int)
print(dataset.head)

decision_set=set(dataset['decision'])
dataset['decision']=dataset['decision'].map({'acc':0,'good':1,'unacc':2,'vgood':3}).astype(int)
print(dataset.head)


#segregate dataset
x=dataset.iloc[:,:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)


#splitting as train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)

##finding best max_depth value
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

plt.figure(figsize=(12,6))
plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='*',markerfacecolor='black',markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
# plt.show()

#training
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=7,random_state=0)
model.fit(x_train,y_train)

from sklearn.metrics import accuracy_score

window=tk.Tk()
window.title("Infidata")
window.geometry('700x500')
window.configure(bg='gray')
# load = Image.open('C:/Users/altaf/OneDrive/Desktop/download.jpg')
# render = ImageTk.PhotoImage(load)
# img = tk.Label(window, image=render)
#img.place(x=0,y=0)


l1=tk.Label(window,text='CAR EVALUATION')
l1.place(x=270,y=20)
l2=tk.Label(window,text='BUYING PRICE')
l2.place(x=200,y=72)
l3=tk.Label(window,text='MAINTENANCE COST')
l3.place(x=200,y=110)
l4=tk.Label(window,text='NUMBER OF DOORS')
l4.place(x=200,y=145)
l5=tk.Label(window,text='NUMBER OF PERSONS')
l5.place(x=200,y=185)
l6=tk.Label(window,text='LUG_BOOT')
l6.place(x=200,y=220)
l7=tk.Label(window,text='SAFETY')
l7.place(x=200,y=255)

txt1=tk.Entry(window,width=10)
txt1.place(x=360,y=72)
txt2=tk.Entry(window,width=10)
txt2.place(x=360,y=110)
txt3=tk.Entry(window,width=10)
txt3.place(x=360,y=145)
txt4=tk.Entry(window,width=10)
txt4.place(x=360,y=185)
txt5=tk.Entry(window,width=10)
txt5.place(x=360,y=220)
txt6=tk.Entry(window,width=10)
txt6.place(x=360,y=255)

def output():
    global l8
    i =  int(txt1.get())
    i1 = int(txt2.get())
    i2 = int(txt3.get())
    i3 = int(txt4.get())
    i4 = int(txt5.get())
    i5 = int(txt6.get())
    l = [[i,i1,i2,i3,i4,i5]]
    result = model.predict(l)
    if result==0:
        result="The Decision of the car is unacceptable"
    else:
        result = "The Decision of the car is acceptable"
    l8 = tk.Label(window, text=result)
    l8.place(x=280, y=340)
b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=280,y=310)

def clear():
    txt1.delete(0,END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    l8.destroy()
b2=tk.Button(window,text='Clear',height=1,width=7,command=clear,bg='red',font=('Times New Roman',12))
b2.place(x=280,y=360)

window.mainloop()