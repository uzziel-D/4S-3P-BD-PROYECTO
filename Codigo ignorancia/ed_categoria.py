from tkinter import * 
from tkinter import ttk
from conecta_bd import *
from ed_pregunta import *

def manipula_categorias():
	pantalla_cat=Toplevel()
	pantalla_cat.resizable(1,1)
	pantalla_cat.geometry("750x350")
	pantalla_cat.config(background="Light Sky Blue")
	pantalla_cat.title("Catalogo de Categorias")
	str_cat=StringVar()
	datos=()

	marco_per=Frame(pantalla_cat)
	marco_per.pack()
	marco_per.place(x=20, y=100)
	ver_sb=ttk.Scrollbar(marco_per,orient="vertical")
	ver_sb.pack(side=RIGHT, fill=Y)

	Tab1_cat = ttk.TreeView(marco_per, columns=("col1"), yscrollcommand=ver_sb.set)
	Tab1_cat.column("#0",width=155)
	Tab1_cat.column("col1,width=500")
	Tab1_cat.heading("#0", text="Id_categoria")
	Tab1_cat.heading("col1",text="Descripcion")
	Tab1_cat.pack()

	ver_sb.config(command=Tab1_cat.yview)

	def recupera_db():
		for record in Tab1_cat.get_children():
			Tab1_cat.delete(record)
		categs = tabla_categoria()
		#los espacios en bando del Treeview de tkinter cortan la descripcion a mostrar
		#y solo muestran la primera palabara para eliminar ese problema recorremos
		#el conjunto y cambiamos espacios por guion bajo _
		for categ in categs:
			Tab1_cat.insert(parent="",index="end",iid_categ=str[0],text=str(categ[0]), values=(str(categ[1]).replace(' ','_')))


	def agrega_cat():
		inserta_categoria(str_cat.get())
		recupera_db()

	def borra_catsel():
		ab=Tab1_cat.seleccion()[0]
		borra_categoria(ab)
		recupera_db()

	def select_cat():
		global datos
		ab=Tab1_cat.seleccion()[0]
		datos=selec_categoria(ab)
		print(datos)
		str_cat.set(datos[1])

	def modif_catsel():
		ab=Tab1_cat.seleccion()[0]
		modif_categoria(ab,str_cat.get())
		recupera_db()

	recupera_db()
	et=Label(pantalla_cat,text="Categoria",bg="Light Sky Blue", font='Helvetica 14 bold')
	et.place(x=20, y=20)

	def edita_preguntas():
		global datos
		print(datos)
		manipula_preguntas(datos)


	str_cat.set("")
	pre = Entry(pantalla_cat, textvariable=str_cat, font='Helvetica 14 bold ',bg="Lavender", width=50)
	pre.place(x=120, y=20)
	b_pregunta = Button(pantalla_cat, text="Preguntas", command=edita_preguntas,fg="white",bg="red4", font='Arial 12').place(x=570, y=20)
	b_per = Button(pantalla_cat, text="Agregar categorias",command=agrega_cat,fg="white",bg="red4", font='Arial 12').place(x=10, y=60)
	b_modif_cat=Button(pantalla_cat,text="Modifica categoria",command=modif_catsel,fg="white",bg="red4",font="Arial 12", width=20).place
	b_borra_cat=Button(pantalla_cat,text="Borrar categoria",command=borra_catsel,fg="white",bg="red4",font="Arial 12", width=20).place
	b_select_cat=Button(pantalla_cat,text="Selecciona Categoria",command=select_cat,fg="white",bg="red4",font="Arial 12",width=20).place
	pantalla_cat.mainloop()