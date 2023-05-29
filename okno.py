from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=1080, height=720)
w.pack()

b = Button(hlavni, text=u"START", activebackground="red", background="green", font= (None, 30), height=10, width=10)
b.place(x = 500, y = 500)
b.pack()


mainloop()