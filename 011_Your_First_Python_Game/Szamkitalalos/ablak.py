from tkinter import *
import random

rand_num = random.randint(0, 100)
ablak = Tk()  # itt hozzuk létre az ablakot
szoveg = Text(ablak, width=30, height=30)  # szövegbox létrehozás
l = Label(text="hello, world: " + str(rand_num))  # label létrehozás
ablak.geometry("500x500")  # ablakméret
l.pack()  # hozzáadom az ablakhoz a a label-t
szoveg.pack()  # itt meg a szövegboxot
ablak.mainloop()  # ez kell hogy az ablak ne záródjon be egyből
