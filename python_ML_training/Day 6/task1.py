from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('Infidata')
window.geometry('400x400')
window.configure(bg='gray')
def clear1():
    global L3
    L3.destroy()
def search():
    global L3
    a=txt.get()

    if (a=='vinith'):
       x='name : vinith \n Designation : designe engg \n Experience : 4+years \n Blood group : O+ve'
       L3=tk.Label(window,text=x)
       L3.place(x=110,y=120)
    elif(a=='khaleel'):
        x = 'name : khaleel \n Designation : computer science engg \n Experience : 3+years \n Blood group : O-ve'
        L3 = tk.Label(window, text=x)
        L3.place(x=110, y=120)
    elif(a=='altaf'):
        x = 'name : altaf \n Designation : computer science engg \n Experience : 3+years \n Blood group : a+ve'
        L3 = tk.Label(window, text=x)
        L3.place(x=110, y=120)
    elif (a == 'sanju'):
        x = 'name : sanju \n Designation : computer science engg \n Experience : 3+years \n Blood group : b+ve'
        L3 = tk.Label(window, text=x)
        L3.place(x=110, y=120)
    elif(a==''):
        x = 'pleas enter   name'
        L3 = tk.Label(window, text=x)
        L3.place(x=110, y=120)

    else:
        x = 'no details found'
        L3 = tk.Label(window, text=x)
        L3.place(x=110, y=120)

def clear():
    global a
    txt.delete(0,END)

L1 = tk.Label(window, text='Employee details')
L1.place(x=10, y=10)
L2 = tk.Label(window, text='name')
L2.place(x=40, y=40)
txt=tk.Entry(window,width=10)
txt.place(x=80,y=40)
b1=tk.Button(window,text='search',command=search)
b1.place(x=150,y=40)
b2=tk.Button(window,text='clear',command=clear)
b2.place(x=110,y=70)
b3=tk.Button(window,text='clear1',command=clear1)
b3.place(x=220,y=220)




window.mainloop()