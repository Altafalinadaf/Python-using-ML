#plant species detection
#from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#load dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/psyc.csv')
print(dataset.columns[dataset.isna().any()])
print(dataset.shape)
print(dataset.head(5))

# mapping
gender_set=set(dataset['gender'])
dataset['gender']=dataset['gender'].map({'Female':0,'Male':1}).astype(int)
print(dataset.head)

# Personality_set=set(dataset['Personality'])
# dataset['Personality']=dataset['Personality'].map({'dependable':0,'serious':1,'responsible':2,'lively':3,'extraverted':4}).astype(int)
# print(dataset.head)

#segregate dataset

x=dataset.iloc[:,:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
#splitting as train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)

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

# plt.figure(figsize=(12,6))
# plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
# plt.title('Finding best Max_Depth')
# plt.xlabel('pred')
# plt.ylabel('score')
# plt.show()

#training
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=1,random_state=0)
model.fit(x_train,y_train)


# accuracy score
from sklearn.metrics import accuracy_score


window=tk.Tk()
window.title("Infidata")
window.geometry('300x300')
window.configure(bg='gray')
load = Image.open('C:/Users/altaf/Downloads/Personality.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image = render)
img.place(x=0,y=0)


l1=tk.Label(window,text='Psyc')
l1.place(x=160,y=20)
l2=tk.Label(window,text='gender')
l2.place(x=80,y=70)
l3=tk.Label(window,text='age')
l3.place(x=80,y=120)
l4=tk.Label(window,text='openness')
l4.place(x=80,y=170)
l5=tk.Label(window,text='neuroticism')
l5.place(x=80,y=220)
l6=tk.Label(window,text='conscientiousness')
l6.place(x=80,y=270)
l7=tk.Label(window,text='agreeableness')
l7.place(x=400,y=70)
l8=tk.Label(window,text='extraversion')
l8.place(x=400,y=120)


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
txt6.place(x=600,y=70)
txt7=tk.Entry(window,width=10)
txt7.place(x=600,y=120)

def clear():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    l6.destroy()
    l7.destroy()

def output():
    global l6
    global l7
    gender = int(txt1.get())
    age = int(txt2.get())
    openness = int(txt3.get())
    neuroticism = int(txt4.get())
    conscientiousness = int(txt5.get())
    agreeableness = int(txt6.get())
    extraversion = int(txt7.get())
    flower = [[gender,age,openness,neuroticism,conscientiousness,agreeableness,extraversion]]
    result = model.predict(flower)
    print(result)
    y_pred = model.predict(x_test)

    if result == 1:
        l6 = tk.Label(window, text="person is dependable")
        l6.place(x=160, y=330)

    elif result == 2:
        l6 = tk.Label(window, text="person is serious")
        l6.place(x=160, y=330)

    elif result==3:
        l6 = tk.Label(window, text="person is responsible")
        l6.place(x=160, y=330)
    elif result == 4:
        l6 = tk.Label(window, text="person is lively")
        l6.place(x=160, y=330)
    else:
        l6 = tk.Label(window, text="person is extraverted")
        l6.place(x=160, y=330)
    l7 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(y_test, y_pred) * 100))
    l7.place(x=160, y=550)

b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=160,y=440)
b2=tk.Button(window,text='Clear',height=1,width=7,command=clear,bg='red')
b2.place(x=160,y=500)

window.mainloop()