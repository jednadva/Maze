from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=506, height=506)
w.pack()

a = 5
b = 5

for x in range(11):
    w.create_line(5,a,505,b)
    a += 50
    b += 50
class  Maze:
    def __init__(self):


class Robot:




mainloop()