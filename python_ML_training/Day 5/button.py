from tkinter import *
import tkinter as tk
def vin():
    print('entered')
window = tk.Tk()
window.title('mk')
window.geometry('300x300')
window.configure(bg='gray')
L1=tk.Label(window,text='hello',bg='white',fg='red',font=('Times new Roman',30),height=10,width=10)
L1.place(x=125,y=10)
b1=tk.Button(window,text='click me',fg='blue',command=vin)
b1.place(x=10,y=10)
window.mainloop()