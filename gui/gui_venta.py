import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
from config.config_venta import (
    agregar_venta,
    editar_venta,
    eliminar_venta,
    obtener_ventas,
    buscar_venta
)

def actualizar_tabla_venta(tabla, data):
    for item in tabla.get_children():
        tabla.delete(item)
    for venta in data:
        tabla.insert("", "end", values=venta)

def mostrar_gui_venta(ventana_principal):
    ventana_venta = ttkb.Toplevel(ventana_principal)
    ventana_venta.title("Gestión de Ventas")
    ventana_venta.geometry("950x700")
    ventana_venta.resizable(False, False)

    # Crear marcos para organizar los componentes
    frame_formulario = ttkb.Frame(ventana_venta, padding=15, relief="solid", borderwidth=2)
    frame_formulario.place(x=10, y=10, width=400, height=300)

    frame_botones = ttkb.Frame(ventana_venta, padding=15, relief="solid", borderwidth=2)
    frame_botones.place(x=420, y=10, width=500, height=150)

    frame_busqueda = ttkb.Frame(ventana_venta, padding=10, relief="solid", borderwidth=2)
    frame_busqueda.place(x=10, y=320, width=920, height=60)

    frame_tabla = ttkb.Frame(ventana_venta, padding=10, relief="solid", borderwidth=2)
    frame_tabla.place(x=10, y=390, width=920, height=300)

    # Formulario para agregar/editar ventas
    ttkb.Label(frame_formulario, text="Fecha (YYYY-MM-DD):", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
    entry_fecha = ttkb.Entry(frame_formulario, width=30)
    entry_fecha.grid(row=0, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Total de Venta:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w")
    entry_total = ttkb.Entry(frame_formulario, width=30)
    entry_total.grid(row=1, column=1, padx=5, pady=5)

    ttkb.Label(frame_formulario, text="Método de Pago:", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w")
    entry_metodo = ttkb.Entry(frame_formulario, width=30)
    entry_metodo.grid(row=2, column=1, padx=5, pady=5)

    # Tabla para mostrar ventas
    tabla = ttkb.Treeview(frame_tabla, columns=("ID", "Fecha", "Total", "Método de Pago"), show="headings", height=15)
    tabla.heading("ID", text="ID")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Total", text="Total de Venta")
    tabla.heading("Método de Pago", text="Método de Pago")
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Fecha", width=150, anchor="center")
    tabla.column("Total", width=150, anchor="center")
    tabla.column("Método de Pago", width=150, anchor="center")
    tabla.pack(fill="both", expand=True)

    actualizar_tabla_venta(tabla, obtener_ventas())

    # Botones de acción
    btn_agregar = ttkb.Button(
        frame_botones,
        text="Agregar 🟢",
        command=lambda: (
            agregar_venta(entry_fecha.get(), entry_total.get(), entry_metodo.get()),
            actualizar_tabla_venta(tabla, obtener_ventas())
        ),
        bootstyle="success-outline", width=18
    )
    btn_agregar.grid(row=0, column=0, padx=5, pady=5)

    btn_editar = ttkb.Button(
        frame_botones,
        text="Editar 🟡",
        command=lambda: editar_venta(tabla, entry_fecha, entry_total, entry_metodo),
        bootstyle="warning-outline", width=18
    )
    btn_editar.grid(row=0, column=1, padx=5, pady=5)

    btn_eliminar = ttkb.Button(
        frame_botones,
        text="Eliminar 🔴",
        command=lambda: (
            eliminar_venta(tabla.item(tabla.focus())["values"][0]),
            actualizar_tabla_venta(tabla, obtener_ventas())
        ),
        bootstyle="danger-outline", width=18
    )
    btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

    # Campo de búsqueda
    entry_buscar = ttkb.Entry(frame_busqueda, width=50)
    entry_buscar.grid(row=0, column=0, padx=5, pady=5)
    btn_buscar = ttkb.Button(
        frame_busqueda,
        text="Buscar 🔎",
        command=lambda: actualizar_tabla_venta(tabla, buscar_venta(entry_buscar.get())),
        bootstyle="primary-outline", width=18
    )
    btn_buscar.grid(row=0, column=1, padx=5, pady=5)

    # Botón para regresar al menú principal
    btn_volver_menu = ttkb.Button(
        frame_botones,
        text="Menú Principal 🏡",
        command=lambda: (ventana_venta.destroy(), ventana_principal.deiconify()),
        bootstyle="secondary-outline", width=18
    )
    btn_volver_menu.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

    ventana_venta.mainloop()
