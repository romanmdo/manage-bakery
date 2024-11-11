import ttkbootstrap as ttkb
from tkinter import messagebox
import gui_helpers  # Importar gui_helpers.py

def mostrar_menu_principal():
    # Crear ventana principal
    ventana = ttkb.Window(themename="darkly")
    ventana.title("Menú Principal")
    ventana.geometry("300x200")

    def abrir_productos():
        # Abrir la ventana de productos, pasándole la ventana principal
        gui_helpers.mostrar_gui_productos(ventana)

    def abrir_empleados():
        messagebox.showinfo("Empleados", "Aquí se gestionan los empleados.")

    # Botones para elegir opción
    btn_productos = ttkb.Button(ventana, text="Productos", command=abrir_productos, width=20)
    btn_productos.pack(pady=10)

    btn_empleados = ttkb.Button(ventana, text="Empleados", command=abrir_empleados, width=20)
    btn_empleados.pack(pady=10)

    # Iniciar la ventana
    ventana.mainloop()

# Llamar a la función principal para mostrar el menú
if __name__ == "__main__":
    mostrar_menu_principal()
