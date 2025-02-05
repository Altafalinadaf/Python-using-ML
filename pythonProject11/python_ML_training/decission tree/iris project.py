#plant species detection
#from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#load dataset
dataset=pd.read_csv('C:/Users/altaf/Downloads/IRIS.csv')

print(dataset.shape)
print(dataset.head(5))

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

plt.figure(figsize=(12,6))
plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
plt.title('Finding best Max_Depth')
plt.xlabel('pred')
plt.ylabel('score')
plt.show()

#training
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=1,random_state=0)
model.fit(x_train,y_train)

# #prediction5.0
# sl=input("Enter the Sepal Length:")
# sw=input("Enter  the Sepal Width :")
# pl=input("Enter the Petal Length:")
# pw=input("Enter the Petal Width:")




# accuracy score
from sklearn.metrics import accuracy_score


window=tk.Tk()
window.title("Infidata")
window.geometry('300x300')
window.configure(bg='gray')
load = Image.open('C:/Users/altaf/download.jfif')
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image = render)
img.place(x=0,y=0)


l1=tk.Label(window,text='Iris Flower Classification')
l1.place(x=160,y=20)
l2=tk.Label(window,text='SL')
l2.place(x=80,y=70)
l3=tk.Label(window,text='SW')
l3.place(x=80,y=120)
l4=tk.Label(window,text='PL')
l4.place(x=80,y=170)
l5=tk.Label(window,text='PW')
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
    SL = int(txt1.get())
    SW = int(txt2.get())
    PL = int(txt3.get())
    PW = int(txt4.get())
    flower = [[SL,SW,PL,PW]]
    result = model.predict(flower)
    print(result)
    y_pred = model.predict(x_test)
    l6 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(y_test, y_pred) * 100))
    l6.place(x=160, y=430)
    if result == 1:
        l6 = tk.Label(window, text="Iris-setosa")
        l6.place(x=160, y=330)

    elif result == 2:
        l6 = tk.Label(window, text="Iris-versicolor")
        l6.place(x=160, y=330)

    else:
        l6 = tk.Label(window, text="Iris-virginica")
        l6.place(x=160, y=330)




b1=tk.Button(window,text='Predict',height=1,width=7,command=output)
b1.place(x=160,y=270)

window.mainloop()