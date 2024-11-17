import ttkbootstrap as ttkb
from tkinter import messagebox
import gui.gui_products as gui_products
import gui.gui_empleados as gui_empleados 
import gui.gui_provedores as gui_proveedores

def mostrar_menu_principal():
    ventana = ttkb.Window(themename="superhero")
    ventana.title("Menú Principal")
    ventana.geometry("300x200")

    def abrir_productos():
        gui_products.mostrar_gui_productos(ventana)

    def abrir_empleados():
        gui_empleados.mostrar_gui_empleados(ventana)
    
    def abrir_proveedores():
        gui_proveedores.mostrar_gui_proveedores(ventana)

    btn_productos = ttkb.Button(
        ventana, text="Productos 🍌", command=abrir_productos, width=20, bootstyle="success-outline"
    )
    btn_productos.pack(pady=10)

    btn_empleados = ttkb.Button(
        ventana, text="Empleados 🤠", command=abrir_empleados, width=20, bootstyle="success-outline"
    )
    btn_empleados.pack(pady=10)

    btn_proveedores = ttkb.Button(
        ventana, text="Proveedores 🚚", command=abrir_proveedores, width=20, bootstyle="success-outline"
    )
    btn_proveedores.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_menu_principal()
