from db_config import conectar
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk
from config.config_empleados import (
    agregar_empleado, editar_empleado, eliminar_empleado, mostrar_empleados,
    buscar_empleado
)

def actualizar_tabla_empleados(tabla):
    """Refresca los datos en la tabla desde la base de datos."""
    for item in tabla.get_children():
        tabla.delete(item)
    mostrar_empleados(tabla)

def mostrar_gui_empleados(ventana_principal):
    """
    Interfaz gráfica para la gestión de empleados.
    """
    # Crear la ventana de empleados
    ventana_empleados = ttkb.Toplevel(ventana_principal)
    ventana_empleados.title("Gestión de Empleados")
    ventana_empleados.geometry("950x700")
    ventana_empleados.resizable(False, False)

    # Crear marcos para organizar los componentes
    frame_formulario = ttkb.Frame(ventana_empleados, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=250)

    frame_botones = ttkb.Frame(ventana_empleados, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_busqueda = ttkb.Frame(ventana_empleados, padding=10, relief="solid", borderwidth=2)
    frame_busqueda.place(x=10, y=270, width=920, height=60)

    frame_tabla = ttkb.Frame(ventana_empleados, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=340, width=920, height=330)

    # Formulario para agregar/editar empleados
    ttkb.Label(frame_formulario, text="Nombre:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_nombre = ttkb.Entry(frame_formulario, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Edad:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_edad = ttkb.Entry(frame_formulario, width=30)
    entry_edad.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Género:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_genero = ttkb.Entry(frame_formulario, width=30)
    entry_genero.grid(row=2, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Teléfono:", font=("Helvetica", 10, "bold")).grid(row=3, column=0, sticky="w")
    entry_telefono = ttkb.Entry(frame_formulario, width=30)
    entry_telefono.grid(row=3, column=1, padx=5, pady=5)

    # Tabla para mostrar empleados
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Nombre", "Edad", "Género", "Teléfono"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Edad", text="Edad")
    tabla.heading("Género", text="Género")
    tabla.heading("Teléfono", text="Teléfono")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=150)
    tabla.column("Edad", width=50)
    tabla.column("Género", width=100)
    tabla.column("Teléfono", width=120)
    tabla.pack(fill="both", expand=True)

    actualizar_tabla_empleados(tabla)

    # Botones de acción
    btn_agregar = ttkb.Button(frame_botones, text="Agregar 🟢", command=lambda: (agregar_empleado(entry_nombre.get(), entry_edad.get(), entry_genero.get(), entry_telefono.get()), actualizar_tabla_empleados(tabla)), bootstyle="success-outline", width=18)
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(frame_botones, text="Editar 🟡", command=lambda: (editar_empleado(tabla, entry_nombre, entry_edad, entry_genero, entry_telefono), actualizar_tabla_empleados(tabla)), bootstyle="warning-outline", width=18)
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(frame_botones, text="Eliminar 🔴", command=lambda: (eliminar_empleado(tabla), actualizar_tabla_empleados(tabla)), bootstyle="danger-outline", width=18)
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    # Campo de búsqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(frame_busqueda, text="Buscar 🔎", command=lambda: (buscar_empleado(entry_buscar.get(), tabla)), bootstyle="primary-outline", width=18)
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

    # Botón para regresar al menú principal
    btn_volver_menu = ttkb.Button(frame_botones, text="Menú Principal 🏡", command=lambda: (ventana_empleados.destroy(), ventana_principal.deiconify()), bootstyle="secondary-outline", width=18)
    btn_volver_menu.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    ventana_empleados.mainloop()
