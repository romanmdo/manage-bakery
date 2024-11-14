create database panaderia;
use panaderia;

CREATE TABLE empleados(
empleadosID INT auto_increment PRIMARY KEY COMMENT   'CLAVE PRIMARIA',
nombre VARCHAR (25) NOT NULL   COMMENT 'NOMBRE DEL EMPLEADO, DATO NO NULO ',
edad INT (2)   NOT NULL COMMENT 'LA EDAD  ',
genero VARCHAR(20)   COMMENT 'PUEDE SER NULO ',
telefono INT (10) NOT NULL
);

CREATE TABLE productos(
productosID  INT  auto_increment PRIMARY KEY  ,
nombre VARCHAR (50) NOT NULL,       
precio DECIMAL  NOT NULL COMMENT 'el precio de los productos',
vencimiento DATE  NOT NULL COMMENT  ' FECHAS DE VENCIMIENTO '
);
CREATE TABLE categoria(
categoriaID INT auto_increment PRIMARY KEY   ,
descripcion VARCHAR(50) NOT NULL  COMMENT  'DATO NECESARIO ',
nombre VARCHAR (25) NOT NULL
);

CREATE TABLE proveedores(
proveedoresID INT auto_increment PRIMARY KEY  ,
nombre VARCHAR (25) NOT NULL,
telefono INT (10)  NOT NULL,
descripcion VARCHAR(50) NOT NULL

);
CREATE TABLE materia_prima(
materia_primaID INT auto_increment PRIMARY KEY ,
marca VARCHAR(15) NOT NULL,
nombre VARCHAR (25) NOT NULL,
peso DECIMAL
);
CREATE TABLE cliente (
clienteID INT auto_increment PRIMARY KEY ,
nombre VARCHAR (25) NOT NULL,
apellido VARCHAR(50) NOT NULL,
telefono INT (10),
DNI INT (10)
);
CREATE TABLE venta(
ventaID INT auto_increment PRIMARY KEY ,
fecha DATE,
total_de_venta DECIMAL,
metodo_de_pago VARCHAR(15) NOT NULL
);


