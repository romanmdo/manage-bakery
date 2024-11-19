import ttkbootstrap as ttkb
from tkinter import messagebox
import gui.gui_products as gui_products
import gui.gui_empleados as gui_empleados 
import gui.gui_provedores as gui_proveedores
import gui.gui_clientes as gui_clientes
import gui.gui_materia_prima as gui_materia_prima
import gui.gui_venta as gui_venta

def mostrar_menu_principal():
    ventana = ttkb.Window(themename="solar")
    ventana.title("Menú Principal")
    ventana.geometry("400x300")

    def abrir_productos():
        gui_products.mostrar_gui_productos(ventana)

    def abrir_empleados():
        gui_empleados.mostrar_gui_empleados(ventana)
    
    def abrir_proveedores():
        gui_proveedores.mostrar_gui_proveedores(ventana)

    def abrir_clientes():
        gui_clientes.mostrar_gui_clientes(ventana)

    def abrir_materia_prima():
        gui_materia_prima.mostrar_gui_materia_prima(ventana)

    def abrir_venta():
        gui_venta.mostrar_gui_venta(ventana)


    btn_productos = ttkb.Button(
        ventana, text="Registro de Productos 🍌", command=abrir_productos, width=25, bootstyle="success-outline"
    )
    btn_productos.pack(pady=10)

    btn_empleados = ttkb.Button(
        ventana, text="Registro de Empleados 🤠", command=abrir_empleados, width=25, bootstyle="success-outline"
    )
    btn_empleados.pack(pady=10)

    btn_proveedores = ttkb.Button(
        ventana, text="Registro de Proveedores 🚚", command=abrir_proveedores, width=25, bootstyle="success-outline"
    )
    btn_proveedores.pack(pady=10)

    btn_clientes = ttkb.Button(
        ventana, text="Registro de Clientes 💼", command=abrir_clientes, width=25, bootstyle="success-outline"
    )
    btn_clientes.pack(pady=10)

    btn_clientes = ttkb.Button(
        ventana, text="Registro de Materia Prima 🧱", command=abrir_materia_prima, width=25, bootstyle="success-outline"
    )
    btn_clientes.pack(pady=10)
    
    btn_clientes = ttkb.Button(
        ventana, text="Registro de Ventas 💰", command=abrir_venta, width=25, bootstyle="success-outline"
    )
    btn_clientes.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    mostrar_menu_principal()
