import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from config.config_clientes import (
    agregar_cliente, editar_cliente, eliminar_cliente, obtener_clientes, buscar_cliente
)

def actualizar_tabla_clientes(tabla, data):
    for item in tabla.get_children():
        tabla.delete(item)
    for cliente in data:
        tabla.insert("", "end", values=cliente)

def mostrar_gui_clientes(ventana_principal):
    ventana_clientes = ttkb.Toplevel(ventana_principal)
    ventana_clientes.title("Gestión de Clientes")
    ventana_clientes.geometry("950x700")
    ventana_clientes.resizable(False, False)

    # Crear marcos para organizar los componentes
    frame_formulario = ttkb.Frame(ventana_clientes, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=300)

    frame_botones = ttkb.Frame(ventana_clientes, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_busqueda = ttkb.Frame(ventana_clientes, padding=10, relief="solid", borderwidth=2)
    frame_busqueda.place(x=10, y=320, width=920, height=60)

    frame_tabla = ttkb.Frame(ventana_clientes, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=390, width=920, height=300)

    # Formulario para agregar/editar clientes
    ttkb.Label(frame_formulario, text="Nombre:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_nombre = ttkb.Entry(frame_formulario, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Apellido:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_apellido = ttkb.Entry(frame_formulario, width=30)
    entry_apellido.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Teléfono:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_telefono = ttkb.Entry(frame_formulario, width=30)
    entry_telefono.grid(row=2, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="DNI:", font=("Helvetica", 10, "bold")).grid(row=3, column=0, sticky="w")
    entry_dni = ttkb.Entry(frame_formulario, width=30)
    entry_dni.grid(row=3, column=1, padx=5, pady=5)

    # Tabla para mostrar clientes
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Nombre", "Apellido", "Teléfono", "DNI"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Apellido", text="Apellido")
    tabla.heading("Teléfono", text="Teléfono")
    tabla.heading("DNI", text="DNI")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=150)
    tabla.column("Apellido", width=150)
    tabla.column("Teléfono", width=100)
    tabla.column("DNI", width=100)
    tabla.pack(fill="both", expand=True)

    actualizar_tabla_clientes(tabla, obtener_clientes())

    # Botones de acción
    btn_agregar = ttkb.Button(
        frame_botones,
        text="Agregar 🟢",
        command=lambda: (agregar_cliente(entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_dni.get()),
                         actualizar_tabla_clientes(tabla, obtener_clientes())),
        bootstyle="success-outline", width=18
    )
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(
        frame_botones,
        text="Editar 🟡",
        command=lambda: editar_cliente(tabla, entry_nombre, entry_apellido, entry_telefono, entry_dni),
        bootstyle="warning-outline", width=18
    )
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(
        frame_botones,
        text="Eliminar 🔴",
        command=lambda: (eliminar_cliente(tabla.item(tabla.focus())["values"][0]), actualizar_tabla_clientes(tabla, obtener_clientes())),
        bootstyle="danger-outline", width=18
    )
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    # Campo de búsqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(
        frame_busqueda,
        text="Buscar 🔎",
        command=lambda: actualizar_tabla_clientes(tabla, buscar_cliente(entry_buscar.get())),
        bootstyle="primary-outline", width=18
    )
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

    # Botón para regresar al menú principal
    btn_volver_menu = ttkb.Button(
        frame_botones,
        text="Menú Principal 🏡",
        command=lambda: (ventana_clientes.destroy(), ventana_principal.deiconify()),
        bootstyle="secondary-outline", width=18
    )
    btn_volver_menu.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    ventana_clientes.mainloop()
