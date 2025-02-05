from tkinter import *
import tkinter as tk
def vin():
    global L1
    L1=tk.Label(window,text='hello mk welcome')
    L1.place(x=175,y=100)
def clear():
    L1.destroy()

window = tk.Tk()
window.title('click me')
window.geometry('300x300')
window.configure(bg='gray')

b1=tk.Button(window,text='click me',fg='blue',command=vin)
b1.place(x=125,y=125)
b2=tk.Button(window,text='clear',fg='blue',command=clear)
b2.place(x=150,y=150)
window.mainloop()