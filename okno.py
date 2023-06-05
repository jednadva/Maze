from tkinter import *
import tkinter

hlavni = Tk()

w = Canvas(hlavni, width=1080, height=720)
w.pack()

startbtn = Button(hlavni, text=u"START", activebackground="red", background="green", font= (None, 30), height=10, width=10)
startbtn.place(x = 500, y = 500)
startbtn.pack()

b = Button(hlavni,text=u"EASY",activebackground="yellow", font= (None, 30), height=10, width=10,)
b.pack(side=tk.LEFT)


mainloop()