import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from config.config_materia_prima import (
    agregar_materia_prima,
    editar_materia_prima,
    eliminar_materia_prima,
    obtener_materia_prima,
    buscar_materia_prima
)

def actualizar_tabla_materia_prima(tabla, data):
    for item in tabla.get_children():
        tabla.delete(item)
    for materia in data:
        tabla.insert("", "end", values=materia)

def mostrar_gui_materia_prima(ventana_principal):
    ventana_materia_prima = ttkb.Toplevel(ventana_principal)
    ventana_materia_prima.title("Gestión de Materia Prima")
    ventana_materia_prima.geometry("950x700")
    ventana_materia_prima.resizable(False, False)

    # Crear marcos para organizar los componentes
    frame_formulario = ttkb.Frame(ventana_materia_prima, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=300)

    frame_botones = ttkb.Frame(ventana_materia_prima, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_busqueda = ttkb.Frame(ventana_materia_prima, padding=10, relief="solid", borderwidth=2)
    frame_busqueda.place(x=10, y=320, width=920, height=60)

    frame_tabla = ttkb.Frame(ventana_materia_prima, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=390, width=920, height=300)

    # Formulario para agregar/editar materia prima
    ttkb.Label(frame_formulario, text="Marca:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_marca = ttkb.Entry(frame_formulario, width=30)
    entry_marca.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Nombre:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_nombre = ttkb.Entry(frame_formulario, width=30)
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Peso (kg):", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_peso = ttkb.Entry(frame_formulario, width=30)
    entry_peso.grid(row=2, column=1, padx=5, pady=5)

    # Tabla para mostrar materia prima
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Marca", "Nombre", "Peso"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Marca", text="Marca")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Peso", text="Peso (kg)")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Marca", width=150)
    tabla.column("Nombre", width=150)
    tabla.column("Peso", width=100, anchor="center")
    tabla.pack(fill="both", expand=True)

    actualizar_tabla_materia_prima(tabla, obtener_materia_prima())

    # Botones de acción
    btn_agregar = ttkb.Button(
        frame_botones,
        text="Agregar 🟢",
        command=lambda: (
            agregar_materia_prima(entry_marca.get(), entry_nombre.get(), entry_peso.get()),
            actualizar_tabla_materia_prima(tabla, obtener_materia_prima())
        ),
        bootstyle="success-outline", width=18
    )
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(
        frame_botones,
        text="Editar 🟡",
        command=lambda: editar_materia_prima(tabla, entry_marca, entry_nombre, entry_peso),
        bootstyle="warning-outline", width=18
    )
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(
        frame_botones,
        text="Eliminar 🔴",
        command=lambda: (
            eliminar_materia_prima(tabla.item(tabla.focus())["values"][0]),
            actualizar_tabla_materia_prima(tabla, obtener_materia_prima())
        ),
        bootstyle="danger-outline", width=18
    )
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    # Campo de búsqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(
        frame_busqueda,
        text="Buscar 🔎",
        command=lambda: actualizar_tabla_materia_prima(tabla, buscar_materia_prima(entry_buscar.get())),
        bootstyle="primary-outline", width=18
    )
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

    # Botón para regresar al menú principal
    btn_volver_menu = ttkb.Button(
        frame_botones,
        text="Menú Principal 🏡",
        command=lambda: (ventana_materia_prima.destroy(), ventana_principal.deiconify()),
        bootstyle="secondary-outline", width=18
    )
    btn_volver_menu.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    ventana_materia_prima.mainloop()
