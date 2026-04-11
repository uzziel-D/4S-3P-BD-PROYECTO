
import random
import pymysql

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conecta_bd import *

#7#
pant = Tk()
pant.resizable(1,1)
pant.geometry("1200x900")
pant.config(bg="black")
pant.title("Juego de la ignorancia-BD")

fon=PhotoImage(file=r"./im/pista.png")
fond=Label(pant, image=fon, width=1200, bg="light sky blue", height=488).place(x=-2, y=218)

selection=()

str_preg=StringVar()
str_res1=StringVar()
str_res2=StringVar()
str_res3=StringVar()
str_res4=StringVar()
str_sig=StringVar()
correcto=0
x1=10
x2=10
x3=10
x4=10
turno=1

def avanza_jug():
    global x1, x2, x3
    if turno==1:
        x1=x1+100
        j1.place(x=x1, y=250)
    elif turno==2:
        x2=x2+100
        j2.place(x=x2, y=360)
    elif turno==3:
        x3=x3+100
        j3.place(x=x3, y=470)
    
def opc1():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    #8#
    if correcto==1:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set("Turno dejugador jugador "+str(turno))


def opc2():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    #8#
    if correcto==2:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set("Turno dejugador jugador "+str(turno))

def opc3():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    #8#
    if correcto==3:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
  
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set("Turno dejugador jugador "+str(turno))

def opc4():
    global turno, x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    #8#
    if correcto==4:
        avanza_jug()
    else:
        #9#
        x4=x4+100
        j4.place(x=x4, y=585)
    #17#
    turno=turno+1
    #25#
    if turno>3:
        turno=1
    str_sig.set("Turno dejugador jugador "+str(turno))

def sel_preg():
    global str_preg, correcto
    #21#
    tan=len(selection)
    #19#
    if tan!=0:
        #30#
        #30#calcula un numero aleatoorio entre 0 y el tamaño de la lista de preguntas
        n=random.randint(0, tan-1)
        #20#
        str_preg.set(selection[n][1])
        str_res1.set(selection[n][2])
        str_res2.set(selection[n][3])
        str_res3.set(selection[n][4])
        str_res4.set(selection[n][5])
        correcto=selection[n][6]
        ganaste()
        perdiste()
        #22#
        r1.config(state=NORMAL)
        r2.config(state=NORMAL)
        r3.config(state=NORMAL)
        r4.config(state=NORMAL)
    else:
        str_preg.set("categoria sin preguntas")
        str_res1("")
        str_res2("")
        str_res3("")
        str_res4("")
        #28#
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)

    pant.update()

def preguntas(event):
    global selection
    cat = event.Widget()
    selection=recupera_preguntas
    #print(preg)
    sel_preg()

def pregunta_sig():
    global selection
    cat=categorias.get()
    selection=recupera_preguntas(cat)
    #print(preg)
    sel_preg()

def perdiste():

    if x4 == 1110:
        messagebox.showerror("PERDISTE","GANO LA IGNORANCIA")
        pant.destroy()

def ganaste():
    if x1 == 1110:
        messagebox.showinfo("GANASTE","GANO EL JUGADOR 1")
        pant.destroy()
    if x2 == 1110:
        messagebox.showinfo("GANASTE","GANO EL JUGADOR 2")
        pant.destroy()
    if x3 == 1110:
        messagebox.showinfo("GANASTE","GANO EL JUGADOR 3")
        pant.destroy()


cats=recupera_categoria()
#entrada para la respuesta
eti=Label(pant, bg="light sky blue", text="categoria", font="helvetica 18 bold")
eti.place(x=10, y=10)
categorias=ttk.Combobox(pant, font="helvetico 18 bold")
categorias["values"]=cats
categorias.place(x=150, y=10)
categorias.bind("<<comboxselected>>", preguntas)

#35#
sig = Button(pant, text="siguiente", command=pregunta_sig, font="helvetica 14 bold", bg="green",)
sig.place(x=800, y=10)

#34#
str_sig.set("Turno dejugador jugador 1")
sig_jug=Label(pant, bg="yellow", textvariable=str_sig, font="helvetica 18 bold")
sig_jug.place(x=460, y=10)
#33#
eti=Label(pant, bg="light sky blue", text="pregunta", font="helvetica 18 bold")
eti.place(x=10, y=60)

str_preg.set("")
pre=Entry(pant, textvariable=str_preg, font="helvetica 18", bg="lavender", width=100, state=DISABLED)
pre.place(x=150, y=60)

str_res1.set("")
r1=Button(pant, textvariable=str_res1, command=opc1, font="helvetica 14 bold", bg="blue", fg="white", width=20)
r1.place(x=100, y=110)

str_res2.set("")
r2=Button(pant, textvariable=str_res2, command=opc2, font="helvetica 14 bold", bg="blue", fg="white", width=20)
r2.place(x=360, y=110)

str_res3.set("")
r3=Button(pant, textvariable=str_res3, command=opc3, font="helvetica 14 bold", bg="blue", fg="white", width=20)
r3.place(x=620, y=110)

str_res4.set("")
r4=Button(pant, textvariable=str_res4, command=opc4, font="helvetica 14 bold", bg="blue", fg="white", width=20)
r4.place(x=880, y=110)

#31#

ju1=PhotoImage(file=r"./im/ju1.png")
j1=Label(pant, image=ju1, bg="light sky blue")
j1.place(x=10, y=252)

ju2=PhotoImage(file=r"./im/ju2.png")
j2=Label(pant, image=ju2, bg="light sky blue")
j2.place(x=10, y=363)

ju3=PhotoImage(file=r"./im/ju3.png")
j3=Label(pant, image=ju3, bg="light sky blue")
j3.place(x=10, y=475)

ju4=PhotoImage(file=r"./im/ju4.png")
j4=Label(pant, image=ju4, bg="light sky blue")
j4.place(x=10, y=585)

#32#
pant.mainloop()

