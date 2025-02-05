import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw



#load dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/Crop_recommendation.csv')
print(dataset.columns[dataset.isna().any()])
print(dataset.shape)
print(dataset.head(5))

#segregate dataset

x=dataset.iloc[:,:-1].values
print(x.shape)
y=dataset.iloc[:,-1].values
print(y.shape)

#mapping
label_set=set(dataset['label'])
dataset['label']=dataset['label'].map({'apple':0,'banana':1,'blackgram':2,'chickpea':3,'coconut':4,'coffee':5,'cotton':6,
                                       'grapes':7,'jute':8,'kindneybean':9,'lentil':10,'maize':11,'mango':12,'mothbean':13,
                                       'mungbean':14,'muskmelon':15,'orange':16,'papaya':17,'pigeonpeas':18,
                                       'pomegrante':19,'rice':20,'watermelon':21}).astype(float)
print(dataset.head)


#splitting as train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

# finding best max_depth value
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
plt.plot(range(1,10),accuracy,color='skyblue',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
#plt.show()
#trainingHAM_
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=9,random_state=0)
model.fit(x_train,y_train)



window=tk.Tk()
window.title("CROP")
window.geometry('400x440')
# load = Image.open('C:/Users/altaf/Downloads/loan.jpg')
# render = ImageTk.PhotoImage(load)
# img = tk.Label(window, image = render)
# img.place(x=0,y=0)
window.configure(bg='gray')

l1=tk.Label(window,text='CROP PREDICTION')
l1.place(x=160,y=10)
l2=tk.Label(window,text='N')
l2.place(x=80,y=80)
l3=tk.Label(window,text='P')
l3.place(x=200,y=110)
l4=tk.Label(window,text='K')
l4.place(x=80,y=150)
l5=tk.Label(window,text='temperature')
l5.place(x=200,y=180)
l6=tk.Label(window,text='humidity')
l6.place(x=80,y=220)
l7=tk.Label(window,text='ph')
l7.place(x=200,y=260)
l8=tk.Label(window,text='rainfall')
l8.place(x=80,y=300)

txt1=tk.Entry(window,width=10)
txt1.place(x=110,y=80)
txt2=tk.Entry(window,width=10)
txt2.place(x=230,y=110)
txt3=tk.Entry(window,width=10)
txt3.place(x=110,y=150)
txt4=tk.Entry(window,width=10)
txt4.place(x=280,y=180)
txt5=tk.Entry(window,width=10)
txt5.place(x=150,y=220)
txt6=tk.Entry(window,width=10)
txt6.place(x=230,y=260)
txt7=tk.Entry(window,width=10)
txt7.place(x=150,y=300)

def output():
    global l9
    N = int(txt1.get())
    P = int(txt2.get())
    K= int(txt3.get())
    temperature = int(txt4.get())
    humidity = int(txt5.get())
    Ph= int(txt6.get())
    rainfall= int(txt7.get())
    newVal = [[N,P,K,temperature,humidity,Ph,rainfall]]
    result=model.predict((newVal))
    print(result)
    y_pred = model.predict(x_test)
    print(result)
    y_pred = model.predict(x_test)

    l13 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(y_test, y_pred) * 100), width=40,
                   height=2, bg='pink')
    l13.place(x=160, y=460)

    if result == 1:
        l12 = tk.Label(window, text="rice",width=40,height=2,bg='pink')
        l12.place(x=160, y=420)



    elif result==2:
        l12 = tk.Label(window, text="banana ",width=40,height=2,bg='pink')
        l12.place(x=160, y=420)
    else:
        l12 = tk.Label(window, text="coconut ", width=40, height=2, bg='pink')
        l12.place(x=160, y=420)


    # l12=tk.Label(window,text=result)
    # l12.place(x=160,y=380)

b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=100,y=350)

def clear():
    txt1.delete(0,END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    l9.destroy()
b2=tk.Button(window,text='Clear',height=1,width=7,command=clear)
b2.place(x=170,y=350)
window.mainloop()


y_pred = model.predict(x_test)
# accuracy score

from sklearn.metrics import accuracy_score
print("Accuracy of the Model:{0}".format(accuracy_score(y_test,y_pred)*100))