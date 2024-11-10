
---

# Proyecto de Gestión de Productos para Panadería

Este proyecto es una aplicación de gestión de productos en Python que utiliza Tkinter para la interfaz gráfica y MySQL para la base de datos.

## Tabla de Contenidos

1. [Descripción General](#descripción-general)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
6. [Uso](#uso)
7. [Funcionalidades](#funcionalidades)
8. [Capturas de Pantalla](#capturas-de-pantalla)
9. [Posibles Problemas y Soluciones](#posibles-problemas-y-soluciones)
10. [Referencias en el Código](#referencias-en-el-código)
11. [Contribuciones](#contribuciones)
12. [Licencia](#licencia)
13. [Contacto](#contacto)

---

### Descripción General

La aplicación permite a los usuarios agregar, editar, eliminar y ordenar productos en una base de datos de MySQL. También cuenta con una interfaz gráfica que facilita la interacción con la base de datos.

### Requisitos

- Python 3.x
- Tkinter (interfaz gráfica)
- MySQL (base de datos)
- Paquetes adicionales: `mysql-connector-python`, `matplotlib`, `ttkbootstrap`

---

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/proyecto_panaderia.git
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu base de datos MySQL y ajusta las credenciales en el archivo `db_config.py`.

**Nota**: Asegúrate de que MySQL esté en funcionamiento y de que tienes acceso para crear bases de datos y tablas.

---

### Estructura del Proyecto

```
/proyecto_panaderia
├── main.py                 # Código principal de la aplicación
├── db_config.py            # Configuración de conexión a la base de datos
├── gui_helpers.py          # Funciones auxiliares para la interfaz gráfica
├── README.md               # Documentación del proyecto
└── requirements.txt        # Dependencias del proyecto
```

---

### Configuración de la Base de Datos

Para crear la base de datos y las tablas, sigue estos pasos:

1. Conéctate a MySQL y crea la base de datos:

   ```sql
   CREATE DATABASE panaderia;
   USE panaderia;
   ```

2. Crea las tablas principales:

   ```sql
   CREATE TABLE productos (
       productosID INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(50) NOT NULL,
       precio DECIMAL(10, 2) NOT NULL,
       vencimiento DATE NOT NULL
   );

   -- Aquí puedes añadir las otras tablas como 'empleados', 'categoría', etc.
   ```

3. Configura las credenciales en `db_config.py` para conectar tu aplicación a esta base de datos.

---

### Uso

1. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

2. Interactúa con la interfaz gráfica para agregar, editar, eliminar y ordenar productos. 

**Ejemplo de uso**:
- Para agregar un producto, ingresa el nombre, precio y fecha de vencimiento y haz clic en "Agregar".
- Para ordenar productos, utiliza los botones de "Ordenar por Precio" o "Ordenar por Vencimiento".

---

### Funcionalidades

La aplicación permite:
- **Agregar productos**: Añade un nuevo producto a la base de datos.
- **Editar productos**: Modifica un producto existente.
- **Eliminar productos**: Elimina un producto de la base de datos.
- **Ordenar productos**: Ordena la lista de productos por precio o vencimiento en orden ascendente o descendente.
- **Graficar precios**: Muestra una gráfica con los precios de los productos (usando `matplotlib`).

---

### Capturas de Pantalla

Aquí hay un ejemplo de cómo se ve la interfaz de la aplicación:

![Interfaz de la aplicación](/ss.png)

---

### Posibles Problemas y Soluciones

1. **Error de conexión MySQL**: Asegúrate de que el servidor de MySQL esté en ejecución y que las credenciales en `db_config.py` sean correctas.
2. **Problemas con la interfaz gráfica**: Verifica que Tkinter y los paquetes necesarios (`ttkbootstrap`, `matplotlib`, `mysql-connector-python`) estén instalados correctamente.

---

### Referencias en el Código

El código está documentado para facilitar su comprensión. Las secciones clave están comentadas, y se incluyen referencias a funciones y módulos auxiliares.

**Ejemplo de comentario en el código**:

```python
# Esta función agrega un producto a la base de datos
def agregar_producto():
    ...
```

---

### Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar esta aplicación, puedes hacer un fork del repositorio, crear una nueva rama, hacer tus cambios y enviar un pull request.

1. Haz un fork del proyecto
2. Crea una rama (`git checkout -b feature/nueva_funcionalidad`)
3. Confirma tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Sube la rama (`git push origin feature/nueva_funcionalidad`)
5. Abre un pull request

---

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

### Contacto

Para preguntas o sugerencias, puedes contactarme a través de mi perfil de GitHub o por correo electrónico: [romanmdo912@gmail.com](mailto:romanmdo912@gmail.com).

---