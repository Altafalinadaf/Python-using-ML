from tkinter import *
import tkinter as tk


window = tk.Tk()
window.title('Arthimatic operation')
window.geometry('300x300')
window.configure(bg='gray')
L1=tk.Label(window,text='calculation')
L1.place(x=110,y=20)

def sum():
    global L1
    a=int(input('enter the number'))
    b=(int(input('enter the number')))
    sum=a+b
    x=('sum of {0} & {1} is {2}'.format(a ,b ,sum))
    L1=tk.Label(window,text=x)
    L1.place(x=100,y=190)

def mul():
    global L1
    a=int(input('enter the number'))
    b=(int(input('enter the number')))
    mul=a*b
    x = ('mul of {0} & {1} is {2}'.format(a, b, mul))
    L1 = tk.Label(window, text=x)
    L1.place(x=100, y=190)

def sub():
    global L1
    a=int(input('enter the number'))
    b=(int(input('enter the number')))
    sub=a-b
    x = ('sub of {0} &{1} is {2}'.format(a, b, sub))
    L1 = tk.Label(window, text=x)
    L1.place(x=100, y=190)

def div():
    global L1
    a=int(input('enter the number'))
    b=(int(input('enter the number')))
    div=a/b
    x = ('div of {0} & {1} is {2}'.format(a, b, div))
    L1 = tk.Label(window, text=x)
    L1.place(x=100, y=190)
def clear():
    L1.destroy()




b1=tk.Button(window,text='sum',fg='blue',command=sum)
b1.place(x=125,y=60)

b2=tk.Button(window,text='mul',fg='blue',command=mul)
b2.place(x=180,y=100)
b3=tk.Button(window,text='sub',fg='blue',command=sub)
b3.place(x=125,y=140)
b4=tk.Button(window,text='div',fg='blue',command=div)
b4.place(x=80,y=100)
b5=tk.Button(window,text='clear',fg='blue',command=clear)
b5.place(x=125,y=100)



window.mainloop()