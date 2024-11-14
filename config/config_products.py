# products.py
from db_config import conectar
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt

# Funciones CRUD (Agregar, Editar, Eliminar, Mostrar)
def agregar_producto(nombre, precio, vencimiento):
    '''
    CRUD - agregar-productos
    '''
    if validar_entrada(nombre, precio, vencimiento):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, vencimiento) VALUES (%s, %s, %s)", (nombre, float(precio), vencimiento))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False

def cargar_producto(tabla):
    '''
    CRUD - cargar-productos
    '''
    selected_item = tabla.focus()
    if selected_item:
        valores = tabla.item(selected_item, "values")
        return valores
    return None

def editar_producto(tabla, entry_nombre, entry_precio, entry_vencimiento):
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
            """, (nombre, float(precio), vencimiento, producto_id))  # Consulta a la DB
            conn.commit()
            cursor.close()
            conn.close()
            return True
    return False

def eliminar_producto(tabla):
    '''
    CRUD - eliminar-productos
    '''
    selected_item = tabla.focus()
    if selected_item:
        producto_id = tabla.item(selected_item, "values")[0]
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE productosID = %s", (producto_id,)) # Consulta a la DB
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False

def mostrar_productos(tabla):
    '''
    CRUD - mostrar-productos
    '''
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")  # Consulta a la DB
    filas = cursor.fetchall()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

def validar_entrada(nombre, precio, vencimiento):
    '''
    Validar datos de entrada
    '''
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

def ordenar_productos_por_precio(orden, tabla):
    '''
    Ordenar productos por precio
    '''
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos ORDER BY precio " + orden  # Consulta a la DB
    cursor.execute(query)
    filas = cursor.fetchall()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

def ordenar_productos_por_vencimiento(orden, tabla):
    '''
    Ordenar productos por fecha de vencimiento
    '''
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos ORDER BY vencimiento " + orden  # Consulta a la DB
    cursor.execute(query)
    filas = cursor.fetchall()
    for fila in filas:
        tabla.insert("", "end", values=fila)
    cursor.close()
    conn.close()

def buscar_producto(nombre_buscar, tabla):
    '''
    Buscar productos en la DB
    '''
    conn = conectar()
    cursor = conn.cursor()
    query = "SELECT * FROM productos WHERE nombre LIKE %s"  # Consulta a la DB
    cursor.execute(query, (f"%{nombre_buscar}%",))
    filas = cursor.fetchall()
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