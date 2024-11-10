import mysql.connector # conector de MySQL
from mysql.connector import Error

import tkinter as tk # tkinter - para las ventanas
from tkinter import messagebox, ttk

from datetime import datetime


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