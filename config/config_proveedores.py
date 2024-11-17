from db_config import conectar

def obtener_proveedores():
    """
    Devuelve todos los proveedores desde la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM proveedores"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def agregar_proveedor(nombre, telefono, descripcion):
    """
    Agrega un nuevo proveedor a la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO proveedores (nombre, telefono, descripcion) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (nombre, telefono, descripcion))
    conexion.commit()
    conexion.close()

def editar_proveedor(proveedor_id, nombre, telefono, descripcion):
    """
    Actualiza un proveedor existente en la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE proveedores SET nombre = %s, telefono = %s, descripcion = %s WHERE proveedoresID = %s"
    cursor.execute(consulta, (nombre, telefono, descripcion, proveedor_id))
    conexion.commit()
    conexion.close()

def eliminar_proveedor(proveedor_id):
    """
    Elimina un proveedor de la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "DELETE FROM proveedores WHERE proveedoresID = %s"
    cursor.execute(consulta, (proveedor_id,))
    conexion.commit()
    conexion.close()
