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
	pantalla_user.resizable(1,1)
	pantalla_user.geometry("720x470")
	pantalla_user.config(background="Light Sky Blue")
	pantalla_user.title("Catalogo de Usuarios")
	str_user = StringVar()

	#marco para la pantallla 
	marco = Frame(pantalla_user)
	marco.pack()
	marco.place(x=40, y=120)
	#barra de desplazamiento para la tabla de los usarios
	scroll = ttk.Scrollbar(marco, orient="vertical")
	scroll.pack(side=RIGHT, fill=Y)
    #
	Tab_user = ttk.Treeview(marco, columns=("nombre"), yscrollcommand=scroll.set)
	Tab_user.column("#0", width=80)
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
			print("no se ingreso un nombre")
			return
		inserta_usuario(nombre)
		recupera_db()
		str_user.set("")
		

	def modifica_user():
		sel	=  Tab_user.selection()
		if not sel:
			print("No se seleccionó usuario")
			return
		#ac es la 	primera seleccion que hiso el usuario
		ac = sel[0]
		modif_usuario(ac,str_user.get())
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
	pre = Entry(pantalla_user, textvariable=str_user, font='Helvetica 14 bold ',bg="Lavender", width=50)
	pre.place(x=20, y=20)
	#boton para agregar un usuario
	btn_agrega = Button(pantalla_user, text="Agregar usuario", command=agrega_user, bg="green4", fg="white")
	btn_agrega.place(x=400, y=60)
	#boton de seleccion de usuario
	btn_select = Button(pantalla_user,text="Seleccionar usuario",command=select_user,bg="red4",fg="white")
	btn_select.place(x=20, y=60)
	#boton para modificar el nombre del usuaio seleccionado
	btn_modifica = Button(pantalla_user, text="Modificar usuario", command=modifica_user, bg="blue4", fg="white")
	btn_modifica.place(x=200, y=60)

	#Botones para los definir a los jugadores
	btn_j1 = Button(pantalla_user, text="Ju1", command=asignar_j1, bg="orange")
	btn_j1.place(x=20, y=90)

	btn_j2 = Button(pantalla_user, text="Ju2", command=asignar_j2, bg="orange")
	btn_j2.place(x=100, y=90)

	btn_j3 = Button(pantalla_user, text="Ju3", command=asignar_j3, bg="orange")
	btn_j3.place(x=180, y=90)

	#nombre de los  jugadores definidos

	str_j1 = StringVar()
	str_j1.set(jugador1)

	str_j2 = StringVar()
	str_j2.set(jugador2)

	str_j3 = StringVar()
	str_j3.set(jugador3)

	jug = Label(pantalla_user, bg="green", textvariable=str_j1, font='Helvetica 18 bold')
	jug.place(x=450, y=130)

	jug2 = Label(pantalla_user, bg="green", textvariable=str_j2, font='Helvetica 18 bold')
	jug2.place(x=450, y=200)

	jug3 = Label(pantalla_user, bg="green", textvariable=str_j3, font='Helvetica 18 bold')
	jug3.place(x=450, y=280)


	recupera_db()
	pantalla_user.mainloop()
