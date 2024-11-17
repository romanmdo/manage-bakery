import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk
from config.config_proveedores import (
    agregar_proveedor, editar_proveedor, eliminar_proveedor, obtener_proveedores
)

def actualizar_tabla(tabla, data_function):
    for item in tabla.get_children():
        tabla.delete(item)
    for fila in data_function():
        tabla.insert("", "end", values=fila)

def mostrar_gui_proveedores(ventana_principal):
    ventana_proveedores = ttkb.Toplevel(ventana_principal)
    ventana_proveedores.title("Gestión de Proveedores")
    ventana_proveedores.geometry("950x700")
    ventana_proveedores.resizable(False, False)

    # Crear marcos
    frame_formulario = ttkb.Frame(ventana_proveedores, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=250)

    frame_botones = ttkb.Frame(ventana_proveedores, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_tabla = ttkb.Frame(ventana_proveedores, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=340, width=920, height=330)

    # Formulario
    ttkb.Label(frame_formulario, text="Nombre:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_nombre = ttkb.Entry(frame_formulario, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Teléfono:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_telefono = ttkb.Entry(frame_formulario, width=30)
    entry_telefono.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Descripción:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_descripcion = ttkb.Entry(frame_formulario, width=30)
    entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

    # Tabla
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Nombre", "Teléfono", "Descripción"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Teléfono", text="Teléfono")
    tabla.heading("Descripción", text="Descripción")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=150)
    tabla.column("Teléfono", width=100)
    tabla.column("Descripción", width=200)
    tabla.pack(fill="both", expand=True)

    # Botones
    btn_agregar = ttkb.Button(frame_botones, text="Agregar 🟢", bootstyle="success-outline", width=18, command=lambda: (agregar_proveedor(entry_nombre.get(), entry_telefono.get(), entry_descripcion.get()), actualizar_tabla(tabla, obtener_proveedores)))
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(frame_botones, text="Editar 🟡", bootstyle="warning-outline", width=18, command=lambda: (editar_proveedor(tabla.item(tabla.focus())["values"][0], entry_nombre.get(), entry_telefono.get(), entry_descripcion.get()), actualizar_tabla(tabla, obtener_proveedores)))
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(frame_botones, text="Eliminar 🔴", bootstyle="danger-outline", width=18, command=lambda: (eliminar_proveedor(tabla.item(tabla.focus())["values"][0]), actualizar_tabla(tabla, obtener_proveedores)))
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    btn_volver_menu = ttkb.Button(frame_botones, text="Menú Principal 🏡", command=lambda: (ventana_proveedores.destroy(), ventana_principal.deiconify()), bootstyle="secondary-outline", width=18)
    btn_volver_menu.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    # Actualizar tabla
    actualizar_tabla(tabla, obtener_proveedores)

    ventana_proveedores.mainloop()
