from tkinter import *
from tkinter import ttk
from conecta_bd import *
#funcion para poder ver las puntuaciones
def manipula_puntuacion():

    pantalla_pun = Toplevel()
    pantalla_pun.resizable(FALSE, FALSE)
    pantalla_pun.geometry("900x500")
    pantalla_pun.config(background="Light Sky Blue")
    pantalla_pun.title("Tabla de puntuaciones")
    #frames de la pantalla
    frame = Frame(pantalla_pun)
    frame.pack(fill=BOTH, expand=True)
    #se crea el scrollbar
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)
    #el treeview
    tabla = ttk.Treeview(frame,columns=("usuario", "categoria", "puntos"),yscrollcommand=scroll.set)
    #se configura el treview
    scroll.config(command=tabla.yview)
    #se acomodan los damaños denntro de la tabla para que este de manera organizada
    tabla.column("#0", width=80)
    tabla.column("usuario", width=250)
    tabla.column("categoria", width=250)
    tabla.column("puntos", width=150)
    #se acomoda los encavezados
    tabla.heading("#0", text="ID")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("categoria", text="Categoria")
    tabla.heading("puntos", text="Puntos")
    tabla.pack(fill=BOTH, expand=True)

    #def para cargar las puntuaciones de los jugadores
    def cargar_puntuaciones():
        for item in tabla.get_children():#se obtienen todos los datos de la tablaa
            tabla.delete(item)#se eliminan para poder limpiar la tabla y poner nuevos datos
        datos = recupera_puntuacion()#se llama a la funcin que nos muestra la tabla de puintuacion 
        if datos:#si ahi datos
            for dato in datos:#va rellenando los datos
                tabla.insert("","end",text=dato[0],values=(dato[1], dato[2], dato[3]))#va insertando los datos en la tabla 1x1
    cargar_puntuaciones()#y carga las nuevas puntuaciones de los jugadores