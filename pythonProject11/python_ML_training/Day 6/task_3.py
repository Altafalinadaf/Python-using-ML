from tkinter import *
import tkinter as tk
window=tk.Tk()
window.title("Infidata")
window.geometry('600x600')
window.configure(bg='gray')
l1=tk.Label(window,text='Shopping cart')
l1.place(x=250,y=30)

def Ele():
    global total
    window1 = tk.Tk()
    window1.title("Electronics")
    window1.geometry('600x600')
    window1.configure(bg='gray')
    l1 = tk.Label(window1, text='Electronics section')
    l1.place(x=250, y=30)
    l2 = tk.Label(window1, text='Mobile\n10000')
    l2.place(x=200, y=60)
    l3 = tk.Label(window1, text='Tablet\n500')
    l3.place(x=280, y=60)
    l4 = tk.Label(window1, text='Laptop\n4000')
    l4.place(x=360, y=60)
    l5 = tk.Label(window1, text='Tv\n1000')
    l5.place(x=450, y=60)
    b1 = tk.Button(window1, text='Buy now', height=2, width=6 )
    b1.place(x=200, y=100)
    b2 = tk.Button(window1, text='Buy now', height=2, width=6)
    b2.place(x=280, y=100)
    b3 = tk.Button(window1, text='Buy now', height=2, width=6)
    b3.place(x=360, y=100)
    b4 = tk.Button(window1, text='Buy now', height=2, width=6)
    b4.place(x=450, y=100)
    b5 = tk.Button(window1, text='Skip', height=2, width=6)
    b5.place(x=330, y=170)
b1=tk.Button(window,text='Electronics',height=2,width=8,command=Ele)
b1.place(x=120,y=60)
def Fur():
    window2 = tk.Tk()
    window2.title("Furnitures")
    window2.geometry('600x600')
    window2.configure(bg='gray')
    l1 = tk.Label(window2, text='Furniture section')
    l1.place(x=250, y=30)
    l2 = tk.Label(window2, text='sofa\n1000')
    l2.place(x=200, y=60)
    l3 = tk.Label(window2, text='bed\n800')
    l3.place(x=280, y=60)
    l4 = tk.Label(window2, text='table\n300')
    l4.place(x=360, y=60)
    l5 = tk.Label(window2, text='chair\n100')
    l5.place(x=450, y=60)
    b1 = tk.Button(window2, text='Buy now', height=2, width=6)
    b1.place(x=200, y=100)
    b2 = tk.Button(window2, text='Buy now', height=2, width=6)
    b2.place(x=280, y=100)
    b3 = tk.Button(window2, text='Buy now', height=2, width=6)
    b3.place(x=360, y=100)
    b4 = tk.Button(window2, text='Buy now', height=2, width=6)
    b4.place(x=450, y=100)
    b5 = tk.Button(window2, text='Skip', height=2, width=6)
    b5.place(x=330, y=170)
b2=tk.Button(window,text='Furnitures',height=2,width=8,command=Fur)
b2.place(x=200,y=60)
def clo():
    window3 = tk.Tk()
    window3.title("Clothes")
    window3.geometry('600x600')
    window3.configure(bg='gray')
    l1 = tk.Label(window3, text='clothes section')
    l1.place(x=250, y=30)
    l2 = tk.Label(window3, text='Top\n400')
    l2.place(x=200, y=60)
    l3 = tk.Label(window3, text='Jeans\n900')
    l3.place(x=280, y=60)
    l4 = tk.Label(window3, text='shirt\n1000')
    l4.place(x=360, y=60)
    l5 = tk.Label(window3, text='Frok\n800')
    l5.place(x=450, y=60)
    b1 = tk.Button(window3, text='Buy now', height=2, width=6)
    b1.place(x=200, y=100)
    b2 = tk.Button(window3, text='Buy now', height=2, width=6)
    b2.place(x=280, y=100)
    b3 = tk.Button(window3, text='Buy now', height=2, width=6)
    b3.place(x=360, y=100)
    b4 = tk.Button(window3, text='Buy now', height=2, width=6)
    b4.place(x=450, y=100)
    b5 = tk.Button(window3, text='Skip', height=2, width=6)
    b5.place(x=330, y=170)
b3=tk.Button(window,text='clothes',height=2,width=8,command=clo)
b3.place(x=280,y=60)
def App():
    window4 = tk.Tk()
    window4.title("Applicances")
    window4.geometry('600x600')
    window4.configure(bg='gray')
    l1 = tk.Label(window4, text='Applicances section')
    l1.place(x=250, y=30)
    l2 = tk.Label(window4, text='Mixer\n2000')
    l2.place(x=200, y=60)
    l3 = tk.Label(window4, text='juicer\n1000')
    l3.place(x=280, y=60)
    l4 = tk.Label(window4, text='blender\n3000')
    l4.place(x=360, y=60)
    l5 = tk.Label(window4, text='Iron\n2000')
    l5.place(x=450, y=60)
    b1 = tk.Button(window4, text='Buy now', height=2, width=6)
    b1.place(x=200, y=100)
    b2 = tk.Button(window4, text='Buy now', height=2, width=6)
    b2.place(x=280, y=100)
    b3 = tk.Button(window4, text='Buy now', height=2, width=6)
    b3.place(x=360, y=100)
    b4 = tk.Button(window4, text='Buy now', height=2, width=6)
    b4.place(x=450, y=100)
    b5 = tk.Button(window4, text='Skip', height=2, width=6)
    b5.place(x=330, y=170)
b4=tk.Button(window,text='Applicances',height=2,width=8,command=App)
b4.place(x=370,y=60)
def Bill():
    window5 = tk.Tk()
    window5.title("Bill")
    window5.geometry('600x600')
    window5.configure(bg='gray')
    l1 = tk.Label(window5, text='Bill section')
    l1.place(x=250, y=30)
    txt = tk.Entry(window5)
    txt.place(x=250, y=60)
    global l2
    x=txt.get()
    if(x=='suman'):
       x="Mobile-10000\n""table-300\n""Frok-800\n""Mixer-2000\n""Total price is:13,100"
       l2=tk.Label(window5,text=x)
       l2.place(x=250,y=90)
    elif(x=='vinith'):
        x="Laptop-4000\n""sofa-1000\n""shirt-1000\n""Iron-2000\n""Total price is:8000"
        l2=tk.Label(window5,text=x)
        l2.place(x=250,y=90)
b5=tk.Button(window,text='Bill',height=2,width=8,command=Bill)
b5.place(x=240,y=140)


window.mainloop() 