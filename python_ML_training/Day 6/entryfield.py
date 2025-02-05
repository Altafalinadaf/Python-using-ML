from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('mk')
window.geometry('400x400')
window.configure(bg='gray')
def mk():
    global a
    a=txt.get()
    print(a)
def clear():
    global a
    txt.delete(0,END)


txt=tk.Entry(window,width=10)
txt.place(x=100,y=200)
b1=tk.Button(window,text='click me',command=mk)
b1.place(x=125,y=90)
b2=tk.Button(window,text='clear',command=clear)
b2.place(x=140,y=120)
window.mainloop()