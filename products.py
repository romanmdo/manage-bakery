import mysql.connector # conector de MySQL
from mysql.connector import Error

from datetime import datetime
import matplotlib.pyplot as plt # matplotlib - para los graficos

import tkinter as tk # tkinter - para las ventanas
from tkinter import messagebox, ttk
import ttkbootstrap as ttkb # bootstrap pero para tkinter
from ttkbootstrap.constants import *

def conectar():
    '''
    conectar DB a Python
    '''
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",      
            password="root",  
            database="panaderia"
        )
        if conn.is_connected():
            return conn
        else:
            raise ValueError("No se pudo conectar a la base de datos.")
    except Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        return None
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None

# Funciones CRUD (Agregar, Editar, Eliminar, Mostrar)
def agregar_producto():
    '''
    CRUD - agregar-productos
    '''
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    vencimiento = entry_vencimiento.get()
    
    if validar_entrada(nombre, precio, vencimiento):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, vencimiento) VALUES (%s, %s, %s)", 
                       (nombre, float(precio), vencimiento))
        conn.commit()
        cursor.close()
        conn.close()
        mostrar_productos()
        messagebox.showinfo("Éxito", "Producto agregado correctamente")

def cargar_producto():
    '''
    CRUD - cargar-productos
    '''
    selected_item = tabla.focus()
    if selected_item:
        valores = tabla.item(selected_item, "values")
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_vencimiento.delete(0, tk.END)
        entry_nombre.insert(0, valores[1])
        entry_precio.insert(0, valores[2])
        entry_vencimiento.insert(0, valores[3])

def editar_producto():
    '''
    CRUD - editar-productos
    '''
    selected_item = tabla.focus()
    if selected_item:
        producto_id = tabla.item(selected_item, "values")[0]
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        vencimiento = entry_vencimiento.get()
        
        if validar_entrada(nombre, precio, vencimiento):
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(""" 
                UPDATE productos SET nombre=%s, precio=%s, vencimiento=%s WHERE productosID=%s
            """, (nombre, float(precio), vencimiento, producto_id))
            conn.commit()
            cursor.close()
            conn.close()
            mostrar_productos()
            messagebox.showinfo("Actualizado", "Producto actualizado correctamente")

def eliminar_producto():
    '''
    CRUD - eliminar-productos
    '''
    selected_item = tabla.focus()
    if selected_item:
        confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este producto?")
        if confirm:
            producto_id = tabla.item(selected_item, "values")[0]
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM productos WHERE productosID = %s", (producto_id,))
            conn.commit()
            cursor.close()
            conn.close()
            mostrar_productos()
            messagebox.showinfo("Eliminado", "Producto eliminado correctamente")

def mostrar_productos():
    '''
    CRUD - mostar-productos
    '''
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()
    limpiar_tabla()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

# Validación de Entrada
def validar_entrada(nombre, precio, vencimiento):
    try:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if float(precio) <= 0:
            raise ValueError("El precio debe ser un número positivo.")
        datetime.strptime(vencimiento, "%Y-%m-%d")
        return True
    except ValueError as e:
        messagebox.showerror("Error de Validación", f"Error en los datos ingresados: {e}")
        return False

# Limpiar Tabla
def limpiar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

# Función para ordenar productos por precio
def ordenar_productos_por_precio(orden):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos ORDER BY precio " + orden
    cursor.execute(query)
    filas = cursor.fetchall()
    limpiar_tabla()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

# Función para buscar productos por nombre
def buscar_producto():
    nombre_buscar = entry_busqueda.get()
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos WHERE nombre LIKE %s"
    cursor.execute(query, (f"%{nombre_buscar}%",))
    filas = cursor.fetchall()
    limpiar_tabla()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

def ordenar_productos_por_vencimiento(orden):
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos ORDER BY vencimiento " + orden
    cursor.execute(query)
    filas = cursor.fetchall()
    limpiar_tabla()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

def graficar_precios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio FROM productos")
    productos = cursor.fetchall()
    conn.close()

    # Extraer nombres y precios para la gráfica
    nombres = [producto[0] for producto in productos]
    precios = [producto[1] for producto in productos]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.barh(nombres, precios, color='skyblue')
    plt.xlabel('Precio')
    plt.ylabel('Producto')
    plt.title('Precios de Productos')
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()

# Función para crear un efecto de hover en los botones
def on_hover_button(button):
    button.config(style="Hover.TButton")  # Cambiar estilo en hover

def off_hover_button(button):
    button.config(style="TButton")  # Restablecer el estilo

# Configurar ventana principal con un tamaño ajustado
ventana = ttkb.Window(themename="superhero")
ventana.title("Panadería - Gestión de Productos")
ventana.geometry("950x700")  # Ajuste del tamaño total de la ventana
ventana.resizable(False, False)

# Crear marcos para organizar la interfaz
frame_formulario = ttkb.Frame(ventana, padding=15, relief="solid", borderwidth=2, style="TFrame")
frame_formulario.place(x=10, y=10, width=400, height=250)

frame_botones = ttkb.Frame(ventana, padding=15, relief="solid", borderwidth=2, style="TFrame")
frame_botones.place(x=420, y=10, width=500, height=150)  # Ajuste del ancho y alto para evitar desbordes

frame_busqueda = ttkb.Frame(ventana, padding=10, relief="solid", borderwidth=2, style="TFrame")
frame_busqueda.place(x=10, y=270, width=920, height=60)

frame_tabla = ttkb.Frame(ventana, padding=10, relief="solid", borderwidth=2, style="TFrame")
frame_tabla.place(x=10, y=340, width=920, height=330)  # Ajuste de tamaño de la tabla

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

# Botones de acción organizados en filas de 3 en frame_botones
btn_agregar = ttkb.Button(frame_botones, text="Agregar", command=agregar_producto, bootstyle=SUCCESS, width=18)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_editar = ttkb.Button(frame_botones, text="Editar", command=editar_producto, bootstyle=WARNING, width=18)
btn_editar.grid(row=0, column=1, padx=5, pady=5)

btn_eliminar = ttkb.Button(frame_botones, text="Eliminar", command=eliminar_producto, bootstyle=DANGER, width=18)
btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

btn_ordenar_precio_asc = ttkb.Button(frame_botones, text="Ordenar por Precio (Asc)", command=lambda: ordenar_productos_por_precio("ASC"), bootstyle=INFO, width=18)
btn_ordenar_precio_asc.grid(row=1, column=0, padx=5, pady=5)

btn_ordenar_precio_desc = ttkb.Button(frame_botones, text="Ordenar por Precio (Desc)", command=lambda: ordenar_productos_por_precio("DESC"), bootstyle=INFO, width=18)
btn_ordenar_precio_desc.grid(row=1, column=1, padx=5, pady=5)

btn_ordenar_vencimiento_asc = ttkb.Button(frame_botones, text="Ordenar por Vencimiento (Asc)", command=lambda: ordenar_productos_por_vencimiento("ASC"), bootstyle=INFO, width=18)
btn_ordenar_vencimiento_asc.grid(row=1, column=2, padx=5, pady=5)

btn_ordenar_vencimiento_desc = ttkb.Button(frame_botones, text="Ordenar por Vencimiento (Desc)", command=lambda: ordenar_productos_por_vencimiento("DESC"), bootstyle=INFO, width=18)
btn_ordenar_vencimiento_desc.grid(row=2, column=0, padx=5, pady=5)

btn_graficar_precios = ttkb.Button(frame_botones, text="Graficar Precios", command=graficar_precios, bootstyle=PRIMARY, width=18)
btn_graficar_precios.grid(row=2, column=1, padx=5, pady=5)

# Barra de búsqueda
entry_busqueda = ttkb.Entry(frame_busqueda, width=50)
entry_busqueda.grid(row=0, column=0, padx=10)

btn_buscar = ttkb.Button(frame_busqueda, text="Buscar", command=buscar_producto, bootstyle=PRIMARY)
btn_buscar.grid(row=0, column=1, padx=10)

# Tabla de productos
tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio", "Vencimiento"), show="headings", height=15)
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Precio", text="Precio")
tabla.heading("Vencimiento", text="Vencimiento")

tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=250)
tabla.column("Precio", width=100, anchor="center")
tabla.column("Vencimiento", width=150)

tabla.grid(row=0, column=0, sticky="nsew")

# Establecer expansión de la tabla
frame_tabla.grid_rowconfigure(0, weight=1)
frame_tabla.grid_columnconfigure(0, weight=1)

# Mostrar productos iniciales
mostrar_productos()

ventana.mainloop()