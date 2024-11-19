from db_config import conectar

def obtener_materia_prima():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM materia_prima"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def agregar_materia_prima(marca, nombre, peso):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO materia_prima (marca, nombre, peso) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (marca, nombre, peso))
    conexion.commit()
    conexion.close()

def editar_materia_prima(materia_id, marca, nombre, peso):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE materia_prima SET marca = %s, nombre = %s, peso = %s WHERE materia_primaID = %s"
    cursor.execute(consulta, (marca, nombre, peso, materia_id))
    conexion.commit()
    conexion.close()

def eliminar_materia_prima(materia_id):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "DELETE FROM materia_prima WHERE materia_primaID = %s"
    cursor.execute(consulta, (materia_id,))
    conexion.commit()
    conexion.close()

def buscar_materia_prima(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "SELECT * FROM materia_prima WHERE nombre LIKE %s OR marca LIKE %s"
    cursor.execute(consulta, (f"%{nombre}%", f"%{nombre}%"))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados
