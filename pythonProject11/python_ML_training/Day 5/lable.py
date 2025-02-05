from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('mk')
window.geometry('300x300')
window.configure(bg='gray')
L1=tk.Label(window,text='hello',bg='white',fg='red',font=('Times new Roman',30))
L1.place(x=125,y=10)
window.mainloop()