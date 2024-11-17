from db_config import conectar

def agregar_empleado(nombre, edad, genero, telefono):
    """
    Agrega un empleado a la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO empleados (nombre, edad, genero, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, edad, genero, telefono))
    conexion.commit()
    conexion.close()

def editar_empleado(tabla, nombre, edad, genero, telefono):
    """
    Edita un empleado seleccionado en la tabla.
    """
    try:
        item = tabla.focus()
        empleado_id = tabla.item(item)["values"][0]
        conexion = conectar()
        cursor = conexion.cursor()
        consulta = "UPDATE empleados SET nombre = %s, edad = %s, genero = %s, telefono = %s WHERE empleadosID = %s"
        cursor.execute(consulta, (nombre.get(), edad.get(), genero.get(), telefono.get(), empleado_id))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"Error al editar: {e}")

def eliminar_empleado(tabla):
    """
    Elimina un empleado seleccionado en la tabla.
    """
    try:
        item = tabla.focus()
        empleado_id = tabla.item(item)["values"][0]
        conexion = conectar()
        cursor = conexion.cursor()
        consulta = "DELETE FROM empleados WHERE empleadosID = %s"
        cursor.execute(consulta, (empleado_id,))
        conexion.commit()
        conexion.close()
    except Exception as e:
        print(f"Error al eliminar: {e}")

def mostrar_empleados(tabla):
    """
    Muestra todos los empleados en la tabla.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM empleados"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    for fila in resultados:
        tabla.insert("", "end", values=fila)
    conexion.close()

def buscar_empleado(nombre, tabla):
    """
    Busca un empleado por nombre y muestra los resultados en la tabla.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM empleados WHERE nombre LIKE %s"
    cursor.execute(consulta, (f"%{nombre}%",))
    resultados = cursor.fetchall()
    for item in tabla.get_children():
        tabla.delete(item)
    for fila in resultados:
        tabla.insert("", "end", values=fila)
    conexion.close()
