from PIL import ImageTk, Image, ImageDraw
# from tkinter import *
import tkinter as tk

window=tk.Tk()
window.title("Infidata")
window.geometry('750x750')
load = Image.open('C:/Users/HP/OneDrive/Documents/download.jfif')
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image = render)
img.place(x=0,y=0)


window.mainloop()