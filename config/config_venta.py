from db_config import conectar

def obtener_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM venta"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def agregar_venta(fecha, total, metodo_de_pago):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO venta (fecha, total_de_venta, metodo_de_pago) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (fecha, total, metodo_de_pago))
    conexion.commit()
    conexion.close()

def editar_venta(venta_id, fecha, total, metodo_de_pago):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE venta SET fecha = %s, total_de_venta = %s, metodo_de_pago = %s WHERE ventaID = %s"
    cursor.execute(consulta, (fecha, total, metodo_de_pago, venta_id))
    conexion.commit()
    conexion.close()

def eliminar_venta(venta_id):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "DELETE FROM venta WHERE ventaID = %s"
    cursor.execute(consulta, (venta_id,))
    conexion.commit()
    conexion.close()

def buscar_venta(criterio):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM venta WHERE fecha LIKE %s OR metodo_de_pago LIKE %s"
    cursor.execute(consulta, (f"%{criterio}%", f"%{criterio}%"))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
