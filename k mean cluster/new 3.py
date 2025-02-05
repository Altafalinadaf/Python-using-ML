import pandas as pd
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
#load dataset
df=pd.read_csv("C:/Users/altaf/OneDrive/Documents/loan_train11.csv")
df.head(5)
df.isna().sum()
df.fillna(method ='pad',inplace=True)
df.info()
from sklearn.preprocessing import LabelEncoder
lr= LabelEncoder()
col=['Gender','Married','Dependents','Education','Self_Employed','Area','Status']
for i in col:
    df[i]=lr.fit_transform(df[i])
# df=df.drop('Unnamed: 32',axis=1)
df.head(5)
X=df.drop('Status',axis=1)
Y=df['Status']
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_s=ss.fit_transform(X)
from sklearn.model_selection import train_test_split
xtr,xte,ytr,yte=train_test_split(X_s,Y,test_size=0.8)
from sklearn.tree import DecisionTreeClassifier
clf_dt=DecisionTreeClassifier()
clf_dt.fit(xtr,ytr)
ypre_dt=clf_dt.predict(xte)
# from sklearn.neural_network import
from sklearn.neural_network import MLPClassifier
clf_nn = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf_nn.fit(xtr,ytr)
ypre_nn=clf_nn.predict(xte)
from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(yte,ypre_dt)
cm2=confusion_matrix(yte,ypre_nn)
from sklearn.metrics import accuracy_score
print(accuracy_score(yte,ypre_dt))
print(accuracy_score(yte,ypre_nn))
import seaborn as sns
sns.heatmap(cm1,annot=True,fmt='.1f')
sns.heatmap(cm2,annot=True,fmt='.1f')
