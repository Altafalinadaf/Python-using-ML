import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw

dataset = pd.read_csv('C:/Users/altaf/Downloads/train_u6lujuX_CVtuZ9i (1).csv')

# print(dataset.shape)
print(dataset.head(5))
# number of missing values in each column
print(dataset.isnull().sum())

x1 = dataset["Gender"].mode()[0]
dataset["Gender"].fillna(x1, inplace=True)

x2 = dataset["Married"].mode()[0]
dataset["Married"].fillna(x2, inplace=True)

# x3=dataset["Dependents"].mode()[0]
# dataset["Dependents"].fillna(x3,inplace=True)

x4 = dataset["Self_Employed"].mode()[0]
dataset["Self_Employed"].fillna(x4, inplace=True)

x5 = dataset["LoanAmount"].mode()[0]
dataset["LoanAmount"].fillna(x5, inplace=True)

x6 = dataset["Loan_Amount_Term"].mode()[0]
dataset["Loan_Amount_Term"].fillna(x6, inplace=True)

x7 = dataset["Credit_History"].mode()[0]
dataset["Credit_History"].fillna(x7, inplace=True)

# mapping salary data to binary value
Married_set = set(dataset['Married'])
dataset['Married'] = dataset['Married'].map({'No': 0, 'Yes': 1}).astype(int)
print(dataset.head)

Gender_set = set(dataset['Gender'])
dataset['Gender'] = dataset['Gender'].map({'Male': 0, 'Female': 1}).astype(int)
print(dataset.head)

Self_Employed_set = set(dataset['Self_Employed'])
dataset['Self_Employed'] = dataset['Self_Employed'].map({'No': 0, 'Yes': 1}).astype(int)
print(dataset.head)

Property_Area_set = set(dataset['Property_Area'])
dataset['Property_Area'] = dataset['Property_Area'].map({'Rural': 0, 'Semiurban': 1, 'Urban': 2}).astype(int)
print(dataset.head)

Education_set = set(dataset['Education'])
dataset['Education'] = dataset['Education'].map({'Graduate': 1, 'Not Graduate': 0}).astype(int)
print(dataset.head)

x = dataset.iloc[:, 1:-1].values
print(x.shape)
y = dataset.iloc[:, -1].values
print(y.shape)

# splitting dataset into train & test

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# finding the best K-value

error = []
from sklearn.neighbors import KNeighborsClassifier

# import matplotlib.pyplot as plt

# calculating error for K value b/w 1 and 40
for i in range(1, 40):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train, y_train)
    pred_i = model.predict(x_test)
    error.append(np.mean(pred_i != y_test))

# plt.figure(figsize=(12,6))
# plt.plot(range(1,40),error,color='red',linestyle='dashed',marker='*',markerfacecolor='blue',markersize=10)
# plt.title("Error Rate K value")
# plt.xlabel('K Value')
# plt.ylabel('Mean Error')
# plt.show()
# accuracy score
from sklearn.metrics import accuracy_score

# Training
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
model.fit(x_train, y_train)

window = tk.Tk()
window.title("Infidata")
window.geometry('750x750')
window.configure(bg='gray')
load = Image.open('C:/Users/altaf/Downloads/loan.jpg')
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image=render)
img.place(x=0, y=0)

l1 = tk.Label(window, text='Loan Prediction', bg='yellow', width=50, height=1, font=('Times New Roman', 15))
l1.place(x=80, y=40)
l2 = tk.Label(window, text='Gender', bg='orange', font=('Times New Roman', 12))
l2.place(x=80, y=120)
l3 = tk.Label(window, text='Married', bg='orange', font=('Times New Roman', 12))
l3.place(x=80, y=170)
l4 = tk.Label(window, text='Education', bg='orange', font=('Times New Roman', 12))
l4.place(x=80, y=220)
l5 = tk.Label(window, text='Self_Employed', bg='orange', font=('Times New Roman', 12))
l5.place(x=80, y=270)
l6 = tk.Label(window, text='LoanAmount', bg='orange', font=('Times New Roman', 12))
l6.place(x=400, y=120)
l7 = tk.Label(window, text='Loan_Amount_Term', bg='orange', font=('Times New Roman', 12))
l7.place(x=400, y=170)
l8 = tk.Label(window, text='Credit_History', bg='orange', font=('Times New Roman', 12))
l8.place(x=400, y=220)
l9 = tk.Label(window, text='Property_Area', bg='orange', font=('Times New Roman', 12))
l9.place(x=400, y=270)

txt1 = tk.Entry(window, width=10)
txt1.place(x=200, y=120)
txt2 = tk.Entry(window, width=10)
txt2.place(x=200, y=170)
txt3 = tk.Entry(window, width=10)
txt3.place(x=200, y=220)
txt4 = tk.Entry(window, width=10)
txt4.place(x=200, y=270)
txt5 = tk.Entry(window, width=10)
txt5.place(x=600, y=270)
txt6 = tk.Entry(window, width=10)
txt6.place(x=600, y=120)
txt7 = tk.Entry(window, width=10)
txt7.place(x=600, y=170)
txt8 = tk.Entry(window, width=10)
txt8.place(x=600, y=220)


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
    Gender = int(txt1.get())
    Married = int(txt2.get())
    Education = int(txt3.get())
    Self_Employed = int(txt4.get())
    LoanAmount = int(txt5.get())
    Loan_Amount_Term = int(txt6.get())
    Credit_History = int(txt7.get())
    Property_Area = int(txt8.get())
    newEmp = [[Gender, Married, Education, Self_Employed, LoanAmount, Property_Area,
               Loan_Amount_Term, Credit_History]]
    result = model.predict(newEmp)
    print(result)
    y_pred = model.predict(x_test)
    print(result)
    y_pred = model.predict(x_test)
    print(result)

    l13 = tk.Label(window, text="Accuracy of the Model:{0}".format(accuracy_score(y_test, y_pred) * 100), width=40,
                   height=2, bg='pink')
    l13.place(x=160, y=460)

    if result == 'Y':
        l12 = tk.Label(window, text=" Person is Applicable for Loan", width=40, height=2, bg='brown')
        l12.place(x=160, y=420)


    elif result == 'R':
        l12 = tk.Label(window, text="Person is not Applicable for Loan ", width=40, height=2, bg='brown')
        l12.place(x=160, y=420)


b1 = tk.Button(window, text='Predict', height=2, width=15, command=output, bg='blue')
b1.place(x=150, y=350)
b2 = tk.Button(window, text='Clear', height=2, width=15, command=clear, bg='red')
b2.place(x=350, y=350)

window.mainloop()

#
# Y_pred = model.predict(X_test)
# print(np.concatenate((Y_pred.reshape(len(Y_pred),1),Y_test.reshape(len(Y_test),1)),1))
#
# from sklearn.metrics import confusion_matrix,accuracy_score
# cm=confusion_matrix(Y_test,Y_pred)
# print("Confusion Matrix:")
# print(cm)
# print("Accuricy of the Model:{0}%".format(accuracy_score(Y_test,Y_pred)*100))
