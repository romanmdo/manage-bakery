import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk
from products import *  # Asegúrate de importar las funciones necesarias como agregar_producto, etc.

def mostrar_gui_productos(ventana_principal):
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

    # Botones en frame_botones usando estilos de ttkbootstrap
    btn_agregar = ttkb.Button(frame_botones, text="Agregar", command=lambda: agregar_producto(entry_nombre.get(), entry_precio.get(), entry_vencimiento.get()), bootstyle=SUCCESS, width=18)
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(frame_botones, text="Editar", command=lambda: editar_producto(tabla, entry_nombre, entry_precio, entry_vencimiento), bootstyle=WARNING, width=18)
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(frame_botones, text="Eliminar", command=lambda: eliminar_producto(tabla), bootstyle=DANGER, width=18)
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    btn_ordenar_precio_asc = ttkb.Button(frame_botones, text="Ordenar por Precio (Asc)", command=lambda: ordenar_productos_por_precio("ASC", tabla), bootstyle=INFO, width=18)
    btn_ordenar_precio_asc.grid(row=1, column=0, padx=5, pady=5)

    btn_ordenar_precio_desc = ttkb.Button(frame_botones, text="Ordenar por Precio (Desc)", command=lambda: ordenar_productos_por_precio("DESC", tabla), bootstyle=INFO, width=18)
    btn_ordenar_precio_desc.grid(row=1, column=1, padx=5, pady=5)

    btn_ordenar_vencimiento_asc = ttkb.Button(frame_botones, text="Ordenar por Vencimiento (Asc)", command=lambda: ordenar_productos_por_vencimiento("ASC", tabla), bootstyle=INFO, width=18)
    btn_ordenar_vencimiento_asc.grid(row=1, column=2, padx=5, pady=5)

    # Botón "Menú Principal 🏡" en la fila 2, alineado con los otros botones
    btn_volver_menu = ttkb.Button(frame_botones, text="Menú Principal 🏡", command=lambda: (ventana_productos.destroy(), ventana_principal.deiconify()), bootstyle=SECONDARY, width=18)
    btn_volver_menu.grid(row=2, column=0, padx=5, pady=5, columnspan=3)  # Se coloca en la fila 2 y ocupa 3 columnas

    # Campo de búsqueda en frame_busqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(frame_busqueda, text="Buscar", command=lambda: buscar_producto(entry_buscar.get(), tabla), bootstyle=PRIMARY, width=18)
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

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

    # Llamar a la función para mostrar productos en la tabla al iniciar la interfaz
    mostrar_productos(tabla)

def obtener_productos_ordenados_por_precio(orden):
    """
    Obtiene los productos de la base de datos ordenados por precio.
    :param orden: "ASC" para ascendente, "DESC" para descendente.
    :return: Lista de productos ordenada por precio.
    """
    # Aquí debes implementar la lógica para conectar con tu base de datos y obtener los productos ordenados.
    # Simularemos una lista de productos de ejemplo.
    productos = [
        {'ID': 1, 'Nombre': 'Producto A', 'Precio': 10.0, 'Vencimiento': '2024-12-01'},
        {'ID': 2, 'Nombre': 'Producto B', 'Precio': 20.0, 'Vencimiento': '2024-11-01'},
        {'ID': 3, 'Nombre': 'Producto C', 'Precio': 5.0, 'Vencimiento': '2024-10-01'},
    ]
    # Ordenar la lista de productos por el campo "Precio"
    productos_ordenados = sorted(productos, key=lambda x: x['Precio'], reverse=(orden == "DESC"))
    return productos_ordenados

def obtener_productos_ordenados_por_vencimiento(orden):
    """
    Obtiene los productos de la base de datos ordenados por vencimiento.
    :param orden: "ASC" para ascendente, "DESC" para descendente.
    :return: Lista de productos ordenada por vencimiento.
    """
    # Simularemos una lista de productos de ejemplo.
    productos = [
        {'ID': 1, 'Nombre': 'Producto A', 'Precio': 10.0, 'Vencimiento': '2024-12-01'},
        {'ID': 2, 'Nombre': 'Producto B', 'Precio': 20.0, 'Vencimiento': '2024-11-01'},
        {'ID': 3, 'Nombre': 'Producto C', 'Precio': 5.0, 'Vencimiento': '2024-10-01'},
    ]
    # Ordenar la lista de productos por el campo "Vencimiento"
    productos_ordenados = sorted(productos, key=lambda x: x['Vencimiento'], reverse=(orden == "DESC"))
    return productos_ordenados


    # Ejecutar la ventana de productos
    ventana_productos.mainloop()
