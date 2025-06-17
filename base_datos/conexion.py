# base_datos/conexion.py

import sqlite3

# Función para conectar a la base de datos
def obtener_conexion():
    return sqlite3.connect("datos/inventario.db")

# Función para crear las tablas si no existen
def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla marcas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        );
    """)

    # Crear tabla vehiculos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            color TEXT NOT NULL,
            marca_id INTEGER NOT NULL,
            FOREIGN KEY (marca_id) REFERENCES marcas(id)
        );
    """)

    conexion.commit()
    conexion.close()
