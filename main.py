import ttkbootstrap as ttkb
from tkinter import messagebox
import gui.gui_products as gui_products  # Importar gui_helpers.py

def mostrar_menu_principal():
    '''
    Muestra la ventana principal
    donde permite seleccionar la acción 
    que se quiere llevar a cabo
    '''
    # Crear ventana principal
    ventana = ttkb.Window(themename="superhero")
    ventana.title("Menú Principal")
    ventana.geometry("300x200")

    def abrir_productos():
        '''
        Abrir la ventana de productos, 
        ejecutando la función de mostrar_gui_productos
        '''
        gui_products.mostrar_gui_productos(ventana)

    def abrir_empleados():
        '''
        Abrir la ventana de empleados 
        que hasta el momento no esta disponible
        '''
        messagebox.showinfo("Empleados", "Aquí se gestionan los empleados.")

    # Botones para elegir opción
    btn_productos = ttkb.Button(ventana, text="Productos 🍌", command=abrir_productos, width=20, bootstyle="success-outline")
    btn_productos.pack(pady=10)

    btn_empleados = ttkb.Button(ventana, text="Empleados 🤠", command=abrir_empleados, width=20, bootstyle="success-outline")
    btn_empleados.pack(pady=10)

    # Iniciar la ventana
    ventana.mainloop()

# Llamar a la función principal para mostrar el menú
if __name__ == "__main__":
    mostrar_menu_principal()