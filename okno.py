from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=1080, height=720)
w.pack()

menu_frame = Tk.frame(hlavni)
menu_frame.pack()

startbtn = Button(hlavni, text=u"START", activebackground="red", background="green", font= (None, 30), height=10, width=10)
startbtn.place(x = 500, y = 500)
startbtn.pack(side="left")

b = Button(hlavni,text="EASY", activebackground="yellow", height=10, width=10)
b.pack(side='left')

def hello():
    print("Ahoj!")

#hlavni menu
obtiznost = Menu(hlavni)
obtiznost.add_command(label="EASY", command=hello)
obtiznost.add_command(label="MEDIUM", command=hlavni.destroy)
obtiznost.add_command(label="HARD", command=hlavni.destroy)

hlavni.config(menu=obtiznost)

#poloha robota
vstup = Entry(hlavni)
vstup.pack(side="left")
vstup.focus_set()

#def volanafunkce():
    #print(vstup.get())

#tlacitko = Button(hlavni, text=u"přečti", width=10, command=volanafunkce, font="ArialNarrow 10")
#tlacitko.pack()

mainloop()