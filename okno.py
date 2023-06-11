import tkinter as tk
from tkinter import font
import random

hlavni = tk.Tk()

hlavni.geometry("1200x750")

label_font = font.Font(size=15, weight = 'bold')

def start():
    maze = create_maze()
    display_maze(maze)

def easy():
    canvas.delete('all')
    krok = 40
    krok2 = 0


    pravdepodobnost = 0.4
    pocet_car = 6

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(y*krok,krok2,y*krok, krok2+40,width=3)
        krok2 += 40
    
    krok = 40
    krok2 = 0

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(krok2, y*krok, krok2+40, y*krok,width=3)
        krok2 += 40

    canvas.create_rectangle(3,3,pocet_car*krok,pocet_car*krok,width=3)
    canvas.create_line(krok*(pocet_car/2), pocet_car*krok, krok*(pocet_car/2)+krok, pocet_car*krok, fill="red", width=3)


def medium():
    canvas.delete('all')
    krok = 40
    krok2 = 0


    pravdepodobnost = 0.4
    pocet_car = 8

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(y*krok,krok2,y*krok, krok2+40,width=3)
        krok2 += 40
    
    krok = 40
    krok2 = 0

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(krok2, y*krok, krok2+40, y*krok,width=3)
        krok2 += 40

    canvas.create_rectangle(3,3,pocet_car*krok,pocet_car*krok,width=3)
    canvas.create_line(krok*(pocet_car/2), pocet_car*krok, krok*(pocet_car/2)+krok, pocet_car*krok, fill="red", width=3)

def hard():
    canvas.delete('all')
    krok = 40
    krok2 = 0


    pravdepodobnost = 0.4
    pocet_car = 10

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(y*krok,krok2,y*krok, krok2+40,width=3)
        krok2 += 40
    
    krok = 40
    krok2 = 0

    for x in range(pocet_car):
        for y in range(pocet_car):
            if random.random() <= pravdepodobnost:
                canvas.create_line(krok2, y*krok, krok2+40, y*krok,width=3)
        krok2 += 40

    canvas.create_rectangle(3,3,pocet_car*krok,pocet_car*krok,width=3)
    canvas.create_line(krok*(pocet_car/2), pocet_car*krok, krok*(pocet_car/2)+krok, pocet_car*krok, fill="red", width=3)

menu_frame = tk.Frame(hlavni)
menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

button_frame = tk.Frame(menu_frame)
button_frame.pack(padx=10, pady=20)

position_frame = tk.Frame(menu_frame)
position_frame.pack(padx=10, pady=30)

option_label = tk.Label(button_frame, text="Výběr bludiště", font = label_font)
option_label.pack(pady=10, padx=10)

a = tk.Button(button_frame,text="EASY", background="green", height=2, width=10, command=easy)
a.pack(padx=10, pady=5)

b = tk.Button(button_frame,text="MEDIUM", background="orange", height=2, width=10, command=medium)
b.pack(padx=10, pady=5)

c = tk.Button(button_frame,text="HARD", background="red", height=2, width=10, command=hard)
c.pack(padx=10, pady=5)

position_label = tk.Label(position_frame, text="Umístění robota", font = label_font)
position_label.pack(pady=10, padx=10)


startbtn = tk.Button(menu_frame, text=u"START", activebackground="red", background="light green", font= (None, 20), height=2, width=10,command=easy)
startbtn.pack(side="left",pady=20, padx=20)


xposition_label = tk.Label(position_frame, text="x:", font = label_font)
xposition_label.pack(pady=10, padx=10)

xposition_entry = tk.Entry(position_frame, font = label_font)
xposition_entry.pack(pady=10, padx=35)

yposition_label = tk.Label(position_frame, text="y:", font = label_font)
yposition_label.pack(pady=10, padx=10)

yposition_entry = tk.Entry(position_frame, font = label_font)
yposition_entry.pack(pady=10, padx=35)

cara = tk.Canvas(hlavni, width=2, height=1080, bg="black")
cara.pack(side=tk.LEFT)

canvas = tk.Canvas(hlavni, width=400, height=400, bg="white")
canvas.pack(pady=100)
#####

#####
hlavni.mainloop()