from db_config import conectar
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk
from config.config_products import (agregar_producto, editar_producto, eliminar_producto,
                            mostrar_productos, ordenar_productos_por_precio, 
                            ordenar_productos_por_vencimiento, buscar_producto, graficar_precios)

# Función para refrescar la tabla en tiempo real
def actualizar_tabla(tabla):
    # Limpiar todos los datos actuales en la tabla
    for item in tabla.get_children():
        tabla.delete(item)
    # Cargar datos actualizados desde la base de datos
    mostrar_productos(tabla)


def mostrar_gui_productos(ventana_principal):
    '''
    Muestra la ventana productos
    '''
    # Crear la ventana de productos (se muestra encima de la ventana principal)
    ventana_productos = ttkb.Toplevel(ventana_principal)
    ventana_productos.title("Gestión de Productos")
    ventana_productos.geometry("950x700")
    ventana_productos.resizable(False, False)

    # Crear marcos para organizar la interfaz
    frame_formulario = ttkb.Frame(ventana_productos, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=250)

    frame_botones = ttkb.Frame(ventana_productos, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_busqueda = ttkb.Frame(ventana_productos, padding=10, relief="solid", borderwidth=2)
    frame_busqueda.place(x=10, y=270, width=920, height=60)

    frame_tabla = ttkb.Frame(ventana_productos, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=340, width=920, height=330)

    # Etiquetas y campos de entrada en frame_formulario
    ttkb.Label(frame_formulario, text="Nombre:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_nombre = ttkb.Entry(frame_formulario, width=30)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Precio:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_precio = ttkb.Entry(frame_formulario, width=30)
    entry_precio.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Vencimiento (YYYY-MM-DD):", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_vencimiento = ttkb.Entry(frame_formulario, width=30)
    entry_vencimiento.grid(row=2, column=1, padx=5, pady=5)

    # Tabla para mostrar los productos en frame_tabla
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio", "Vencimiento"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Precio", text="Precio")
    tabla.heading("Vencimiento", text="Vencimiento")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Nombre", width=150)
    tabla.column("Precio", width=100)
    tabla.column("Vencimiento", width=100)
    tabla.pack(fill="both", expand=True)

    # Llamada inicial para mostrar los productos en la tabla
    actualizar_tabla(tabla)

    # Botones en frame_botones usando estilos de ttkbootstrap
    btn_agregar = ttkb.Button(frame_botones, text="Agregar 🟢", command=lambda: (agregar_producto(entry_nombre.get(), entry_precio.get(), entry_vencimiento.get()), actualizar_tabla(tabla)), bootstyle="success-outline", width=18)
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(frame_botones, text="Editar 🟡", command=lambda: (editar_producto(tabla, entry_nombre, entry_precio, entry_vencimiento), actualizar_tabla(tabla)), bootstyle="warning-outline", width=18)
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(frame_botones, text="Eliminar 🔴", command=lambda: (eliminar_producto(tabla), actualizar_tabla(tabla)),  bootstyle="danger-outline", width=18)
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    btn_ordenar_precio_asc = ttkb.Button(frame_botones, text="Ordenar por Precio ⬆️", command=lambda: (ordenar_productos_por_precio("ASC", tabla), actualizar_tabla(tabla)),  bootstyle="info-outline", width=18)
    btn_ordenar_precio_asc.grid(row=1, column=0, padx=5, pady=5)

    btn_ordenar_vencimiento_asc = ttkb.Button(frame_botones, text="Ordenar por Vencimiento ⬇️", command=lambda: (ordenar_productos_por_vencimiento("ASC", tabla), actualizar_tabla(tabla)), bootstyle="info-outline", width=18)
    btn_ordenar_vencimiento_asc.grid(row=1, column=1, padx=5, pady=5)

    button_graficar = ttkb.Button(frame_botones, text="Gráficar Precios 📊", command=graficar_precios, width=18, bootstyle="danger-outline")
    button_graficar.grid(row=1, column=2, padx=5, pady=5)
    #button_graficar.bind("<Enter>", lambda e: on_hover_button(button_graficar))
    #button_graficar.bind("<Leave>", lambda e: off_hover_button(button_graficar))

    # Campo de búsqueda en frame_busqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(frame_busqueda, text="Buscar 🔎", command=lambda: (buscar_producto(entry_buscar.get(), tabla), actualizar_tabla(tabla)), bootstyle="primary-outline", width=18)
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

    # Botón "Menú Principal 🏡" para regresar al menú
    btn_volver_menu = ttkb.Button(frame_botones, text="Menú Principal 🏡", command=lambda: (ventana_productos.destroy(), ventana_principal.deiconify()), bootstyle="secondary-outline", width=18)
    btn_volver_menu.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

    # Ejecutar la ventana de productos
    ventana_productos.mainloop()
