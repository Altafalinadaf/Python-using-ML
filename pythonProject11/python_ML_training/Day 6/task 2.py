from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('Infidata')
window.geometry('600x600')
window.configure(bg='gray')
def DA():
    global l3
    l3 = tk.Label(window, text='D.A is 2000')
    l3.place(x=190,y=150)
def HRA():
    global l3
    l3 = tk.Label(window, text='HRA is 1000')
    l3.place(x=190, y=150)
def Basic():
    global l3
    l3 = tk.Label(window, text='Basic is 20000')
    l3.place(x=190, y=150)
def Total():
    global l3
    l3 = tk.Label(window, text='Total\n'
                               'DA= 2000\n'
                               'HRA= 1000\n'
                               'Basic= 20000\n'
                               'NET= 230000')
    l3.place(x=190, y=150)

def clear():
        global l3
        l3.destroy()
def search():
    global a
    a = txt.get()
    print(a)

    if (a=='vinith'):

        b2=tk.Button(window,text='DA',command=DA)
        b2.place(x=130,y=100)
        b3 = tk.Button(window, text='HRA',command=HRA)
        b3.place(x=130, y=140)
        b4 = tk.Button(window, text='Basic',command=Basic)
        b4.place(x=130, y=188)
        b5 = tk.Button(window, text='Total',command=Total)
        b5.place(x=130, y=220)

L1 = tk.Label(window, text='salary Details')
L1.place(x=10, y=10)
L2 = tk.Label(window, text='name')
L2.place(x=40, y=40)
txt=tk.Entry(window,width=10)
txt.place(x=80,y=40)
b1=tk.Button(window,text='search',command=search)
b1.place(x=150,y=40)
b2 = tk.Button(window, text='clear', command=clear)
b2.place(x=220, y=220)

window.mainloop()