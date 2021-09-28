from tkinter import *

def compteurdemort(event):
    f = open('chemin vers le fichier texte','r+')
    global mort
    t=event.keysym
    if t == "plus":
        mort = mort +1
        s=str(mort)
        f.write(s)
    elif t == "minus" and mort > 0:
        mort-=1
        s=str(mort)
        f.write(s)
    elif t == "0":
        mort=0
        s=str(mort)
        f.write(s)
root = Tk()
mort = 0
root.bind("<Key>", compteurdemort)
root.mainloop()
