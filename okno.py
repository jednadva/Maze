from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=1080, height=720)
w.pack()

startbtn = Button(hlavni, text=u"START", activebackground="red", background="green", font= (None, 30), height=10, width=10)
startbtn.place(x = 500, y = 500)
startbtn.pack()

easyoption = Button(hlavni,text=u"EASY",activebackground="yellow", font= (None, 30), height=10, width=10 )
easyoption.pack()


mainloop()