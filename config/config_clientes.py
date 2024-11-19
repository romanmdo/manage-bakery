from db_config import conectar

def obtener_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM cliente"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def agregar_cliente(nombre, apellido, telefono, dni):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO cliente (nombre, apellido, telefono, DNI) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, telefono, dni))
    conexion.commit()
    conexion.close()

def editar_cliente(cliente_id, nombre, apellido, telefono, dni):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE cliente SET nombre = %s, apellido = %s, telefono = %s, DNI = %s WHERE clienteID = %s"
    cursor.execute(consulta, (nombre, apellido, telefono, dni, cliente_id))
    conexion.commit()
    conexion.close()

def eliminar_cliente(cliente_id):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "DELETE FROM cliente WHERE clienteID = %s"
    cursor.execute(consulta, (cliente_id,))
    conexion.commit()
    conexion.close()

def buscar_cliente(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM cliente WHERE nombre LIKE %s OR apellido LIKE %s"
    cursor.execute(consulta, (f"%{nombre}%", f"%{nombre}%"))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
