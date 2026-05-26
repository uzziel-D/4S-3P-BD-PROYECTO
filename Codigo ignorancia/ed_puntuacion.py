from tkinter import *
from tkinter import ttk
from conecta_bd import *

def manipula_puntuacion():

    pantalla_pun = Toplevel()
    pantalla_pun.geometry("900x500")
    pantalla_pun.config(background="Light Sky Blue")
    pantalla_pun.title("Tabla de puntuaciones")

    frame = Frame(pantalla_pun)
    frame.pack(fill=BOTH, expand=True)

    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)

    tabla = ttk.Treeview(
        frame,
        columns=("usuario", "categoria", "puntos"),
        yscrollcommand=scroll.set
    )

    scroll.config(command=tabla.yview)

    tabla.column("#0", width=80)
    tabla.column("usuario", width=250)
    tabla.column("categoria", width=250)
    tabla.column("puntos", width=150)

    tabla.heading("#0", text="ID")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("categoria", text="Categoria")
    tabla.heading("puntos", text="Puntos")

    tabla.pack(fill=BOTH, expand=True)

    def cargar_puntuaciones():
        for item in tabla.get_children():
            tabla.delete(item)

        datos = recupera_puntuacion()

        if datos:
            for dato in datos:
                tabla.insert(
                    "",
                    "end",
                    iid=dato[0],
                    text=dato[0],
                    values=(dato[1], dato[2], dato[3])
                )

    cargar_puntuaciones()