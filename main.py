import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import matplotlib.pyplot as plt
import ttkbootstrap as ttkb  # Importar ttkbootstrap para diseño moderno

# Conectar a la base de datos MySQL
def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",      
            password="root",  
            database="panaderia"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")

# Funciones CRUD (Agregar, Editar, Eliminar, Mostrar)
def agregar_producto():
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

# Configuración de la Interfaz de Tkinter con ttkbootstrap
ventana = ttkb.Window(themename="flatly")  # Usar tema de ttkbootstrap
ventana.title("Panadería - Gestión de Productos")
ventana.geometry("850x650")

# Crear marcos para organizar la interfaz con sombra y profundidad
frame_formulario = ttkb.Frame(ventana, padding=15, relief="solid", borderwidth=2, style="TFrame")
frame_formulario.place(x=10, y=10, width=380, height=220)

frame_botones = ttkb.Frame(ventana, padding=15, relief="solid", borderwidth=2, style="TFrame")
frame_botones.place(x=400, y=10, width=200, height=220)

frame_busqueda = ttkb.Frame(ventana, padding=10, relief="solid", borderwidth=2, style="TFrame")
frame_busqueda.place(x=10, y=240, width=820, height=60)

frame_tabla = ttkb.Frame(ventana, padding=10, relief="solid", borderwidth=2, style="TFrame")
frame_tabla.place(x=10, y=310, width=820, height=320)

# Etiquetas y campos de entrada en frame_formulario
ttkb.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = ttkb.Entry(frame_formulario, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

ttkb.Label(frame_formulario, text="Precio:").grid(row=1, column=0, sticky="w")
entry_precio = ttkb.Entry(frame_formulario, width=30)
entry_precio.grid(row=1, column=1, padx=5, pady=5)

ttkb.Label(frame_formulario, text="Vencimiento (YYYY-MM-DD):").grid(row=2, column=0, sticky="w")
entry_vencimiento = ttkb.Entry(frame_formulario, width=30)
entry_vencimiento.grid(row=2, column=1, padx=5, pady=5)

# Botones en frame_botones con hover y bordes redondeados
button_agregar = ttkb.Button(frame_botones, text="Agregar Producto", command=agregar_producto, width=18)
button_agregar.grid(row=0, column=0, pady=5)
button_agregar.bind("<Enter>", lambda e: on_hover_button(button_agregar))
button_agregar.bind("<Leave>", lambda e: off_hover_button(button_agregar))

button_editar = ttkb.Button(frame_botones, text="Editar Producto", command=editar_producto, width=18)
button_editar.grid(row=1, column=0, pady=5)
button_editar.bind("<Enter>", lambda e: on_hover_button(button_editar))
button_editar.bind("<Leave>", lambda e: off_hover_button(button_editar))

button_eliminar = ttkb.Button(frame_botones, text="Eliminar Producto", command=eliminar_producto, width=18)
button_eliminar.grid(row=2, column=0, pady=5)
button_eliminar.bind("<Enter>", lambda e: on_hover_button(button_eliminar))
button_eliminar.bind("<Leave>", lambda e: off_hover_button(button_eliminar))

# Botones adicionales
button_ordenar_precio = ttkb.Button(frame_botones, text="Ordenar por Precio Asc", command=lambda: ordenar_productos_por_precio("ASC"), width=18)
button_ordenar_precio.grid(row=3, column=0, pady=5)
button_ordenar_precio.bind("<Enter>", lambda e: on_hover_button(button_ordenar_precio))
button_ordenar_precio.bind("<Leave>", lambda e: off_hover_button(button_ordenar_precio))

button_ordenar_vencimiento = ttkb.Button(frame_botones, text="Ordenar por Vencimiento", command=lambda: ordenar_productos_por_vencimiento("ASC"), width=18)
button_ordenar_vencimiento.grid(row=4, column=0, pady=5)
button_ordenar_vencimiento.bind("<Enter>", lambda e: on_hover_button(button_ordenar_vencimiento))
button_ordenar_vencimiento.bind("<Leave>", lambda e: off_hover_button(button_ordenar_vencimiento))

button_graficar = ttkb.Button(frame_botones, text="Gráficar Precios", command=graficar_precios, width=18)
button_graficar.grid(row=5, column=0, pady=5)
button_graficar.bind("<Enter>", lambda e: on_hover_button(button_graficar))
button_graficar.bind("<Leave>", lambda e: off_hover_button(button_graficar))


# Barra de búsqueda en frame_busqueda
ttkb.Label(frame_busqueda, text="Buscar Producto:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_busqueda = ttkb.Entry(frame_busqueda, width=40)
entry_busqueda.grid(row=0, column=1, padx=5, pady=5)

button_buscar = ttkb.Button(frame_busqueda, text="Buscar", command=buscar_producto)
button_buscar.grid(row=0, column=2, padx=5, pady=5)

# Tabla para mostrar productos
tabla = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio", "Vencimiento"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Precio", text="Precio")
tabla.heading("Vencimiento", text="Vencimiento")
tabla.grid(row=0, column=0, sticky="nsew")

# Scrollbar
scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")

# Mostrar los productos en la tabla al iniciar
mostrar_productos()

ventana.mainloop()
