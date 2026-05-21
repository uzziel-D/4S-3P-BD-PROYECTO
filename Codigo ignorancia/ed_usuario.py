from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conecta_bd import *
jugador1 = "Defina los jugadores"
jugador2 = "Defina los jugadores"
jugador3 = "Defina los jugadores"
id_jugador1 = 0
id_jugador2 = 0
id_jugador3 = 0

def manipula_usuarios():

	pantalla_user = Toplevel()
	pantalla_user.resizable(FALSE, FALSE)
	pantalla_user.geometry("1250x550")
	pantalla_user.config(background="Light Sky Blue")
	pantalla_user.title("Catalogo de Usuarios")
	fondo = PhotoImage(file=r"./im/pk3.png")
	fond_user = Label(pantalla_user, image=fondo, width=1250, height=550)
	fond_user.pack()
	str_user = StringVar()

	#marco para la pantallla 
	marco = Frame(pantalla_user)
	marco.pack()
	marco.place(x=80, y=170)
	#barra de desplazamiento para la tabla de los usarios
	scroll = ttk.Scrollbar(marco, orient="vertical")
	scroll.pack(side=RIGHT, fill=Y)
    #parte nueva para agranndar las letras del scrobball
	style = ttk.Style()
	#texto de las filas
	style.configure("Treeview",font=("Helvetica", 18),rowheight=25)

	#texto de los encabezados
	style.configure("Treeview.Heading",font=("Helvetica", 24, "bold"))
	Tab_user = ttk.Treeview(marco, columns=("nombre"), yscrollcommand=scroll.set)
	Tab_user.column("#0", width=100)
	Tab_user.column("nombre", width=300)
	Tab_user.heading("nombre", text="Nombre")
	Tab_user.pack()
	scroll.config(command=Tab_user.yview)



	# recupera los usuarios de la BD
	def recupera_db():
		for item in Tab_user.get_children():
			Tab_user.delete(item)
		users = recupera_usuarios()
		for u in users:
			Tab_user.insert(parent="",index="end",iid=u[0],text=u[0],values=(u[1],))

	#
	def select_user():
		global user_actual

		sel = Tab_user.selection()

        #para entender la falla cuando no se selecciona un usuario
		if not sel:
			print("No se seleccionó usuario")
			return
		#para seleccionar al usuario segun su id
		user_actual = sel[0]
		str_user.set(Tab_user.item(user_actual)["values"][0])
		print("Usuario seleccionado:", user_actual)
		
	#agrega al un usuario con la funcion inserta usuario pero si no se ingresa un nombre hara un print
	def agrega_user():
		nombre = str_user.get()
		if nombre == "":
			messagebox.showerror("Error", "No se ingresó un nombre. Por favor, ingresa un nombre de usuario.")
			return
		inserta_usuario(nombre)
		recupera_db()
		str_user.set("")
		
	def modifica_user():
		sel	=  Tab_user.selection()
		if not sel:
			messagebox.showerror("Error", "Selecciona un usuario para modificar")
			return
		#ac es la 	primera seleccion que hiso el usuario
		ac = sel[0]
		modif_usuario(ac,str_user.get())
		if str_user.get() == "":
			messagebox.showerror("Error", "No se ingresó un nombre. Por favor, ingresa un nombre de usuario.")
			return
		recupera_db()
    	
	def asignar_j1():
		global jugador1,id_jugador1
		#seleccion del usuario
		sel = Tab_user.selection()
		#en caso de que nomas le de al boton
		if not sel:
			messagebox.showerror("Error", "Selecciona un usuario")
			return
		id_jugador1 = int(sel[0])
		
		if id_jugador1 == id_jugador2 or id_jugador1 == id_jugador3:
			messagebox.showerror("Error", "El jugador ya ha sido seleccionado. Por favor, elige otro usuario.")
			return

		item = Tab_user.item(sel[0])
		nombre = item["values"][0]

		jugador1 = nombre
		str_j1.set(jugador1)
	
	def asignar_j2():
		global jugador2,id_jugador2
		sel = Tab_user.selection()
		if not sel:
			print("Selecciona un usuario")
			return
		id_jugador2 = int(sel[0])
		
		if id_jugador2 == id_jugador1 or id_jugador2 == id_jugador3:
			messagebox.showerror("Error", "El jugador ya ha sido seleccionado. Por favor, elige otro usuario.")
			return

		item = Tab_user.item(sel[0])
		nombre = item["values"][0]

		jugador2 = nombre
		str_j2.set(jugador2)

	def asignar_j3():
		global jugador3,id_jugador3
		sel = Tab_user.selection()
		if not sel:
			print("Selecciona un usuario")
			return
		id_jugador3 = int(sel[0])
		if id_jugador3 == id_jugador1 or id_jugador3 == id_jugador2:
			messagebox.showerror("Error", "El jugador ya ha sido seleccionado. Por favor, elige otro usuario.")
			return
		item = Tab_user.item(sel[0])
		nombre = item["values"][0]

		jugador3 = nombre
		str_j3.set(jugador3)
		


	str_user.set("")
	#entrada donde se muestra o se ingresa el usuario
	pre = Entry(pantalla_user, textvariable=str_user, font='Helvetica 18 bold ',bg="Lavender", width=80)
	pre.place(x=20, y=20)
	#boton para agregar un usuario
	agrusuario = PhotoImage(file=r"./im/agrusuario.png")
	btn_agrega = Button(pantalla_user, image=agrusuario, command=agrega_user, bg="yellow", fg="white", width=230, height=60)
	btn_agrega.place(x=600, y=80)
	#boton de seleccion de usuario
	selecusuario = PhotoImage(file=r"./im/selecusuario.png")
	btn_select = Button(pantalla_user,image=selecusuario,command=select_user,bg="green",fg="white", width=230, height=60)
	btn_select.place(x=40, y=80)
	#boton para modificar el nombre del usuaio seleccionado
	modifusuario = PhotoImage(file=r"./im/modifusuario.png")
	btn_modifica = Button(pantalla_user,image=modifusuario, command=modifica_user, bg="red", fg="white", width=230, height=60)
	btn_modifica.place(x=300, y=80)

	#Botones para los definir a los jugadores
	master_pkb = PhotoImage(file=r"./im/master_pkb.png")
	btn_j1 = Button(pantalla_user,image=master_pkb, command=asignar_j1, bg="orange",width=50,height=50)
	btn_j1.place(x=520, y=230)
	ultra_pkb = PhotoImage(file=r"./im/ultra_pkb.png")
	btn_j2 = Button(pantalla_user, image=ultra_pkb, command=asignar_j2, bg="orange",width=50,height=50)
	btn_j2.place(x=520, y=330)
	pkb = PhotoImage(file=r"./im/pkb.png")
	btn_j3 = Button(pantalla_user, image=pkb, command=asignar_j3, bg="orange",width=50,height=50)
	btn_j3.place(x=520, y=430)

	#nombre de los  jugadores definidos

	str_j1 = StringVar()
	str_j1.set(jugador1)

	str_j2 = StringVar()
	str_j2.set(jugador2)

	str_j3 = StringVar()
	str_j3.set(jugador3)
	definu = PhotoImage(file=r"./im/definu.png")
	jug = Label(pantalla_user,image=definu,textvariable=str_j1, font='Helvetica 18 bold', width=250, height=50
			 ,compound="center")
	jug.place(x=600, y=230)
	definu2 = PhotoImage(file=r"./im/definu2.png")
	jug2 = Label(pantalla_user,image=definu2, textvariable=str_j2, font='Helvetica 18 bold', width=250, height=50
			 ,compound="center")
	jug2.place(x=600, y=330)
	definu1 = PhotoImage(file=r"./im/definu1.png")
	jug3 = Label(pantalla_user, image=definu1, textvariable=str_j3, font='Helvetica 18 bold', width=250, height=50
			 ,compound="center")
	jug3.place(x=600, y=430)


	recupera_db()
	pantalla_user.mainloop()