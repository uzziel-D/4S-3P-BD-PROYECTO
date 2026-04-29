from tkinter import *
from tkinter import ttk
from conecta_bd import *

def manipula_usuario():
	pantalla_pre=Toplevel()
	pantalla_pre.resizable(1,1)
	pantalla_pre.geometry("1250x550")
	pantalla_pre.config(background="Light Sky Blue")
	pantalla_pre.title("Catalogo de Preguntas")
	str_cat=StringVar()
	str_pre=StringVar()
	str_op1=StringVar()
	str_op2=StringVar()	
	str_op3=StringVar()
	str_op4=StringVar()
	str_cor=StringVar()

