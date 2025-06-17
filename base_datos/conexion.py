# base_datos/conexion.py

import sqlite3

# Función para conectar a la base de datos
def obtener_conexion():
    return sqlite3.connect("datos/inventario.db")

# Función para crear todas las tablas necesarias
def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Crear tabla marcas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (
            id INTEGER PRIMARY KEY,  -- Usamos ID oficial de ACARA
            nombre TEXT NOT NULL UNIQUE
        );
    """)

    # Crear tabla modelos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS modelos (
            id INTEGER PRIMARY KEY,  -- ID de ACARA
            nombre TEXT NOT NULL,
            marca_id INTEGER NOT NULL,
            FOREIGN KEY (marca_id) REFERENCES marcas(id)
        );
    """)

    # Crear tabla versiones
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS versiones (
            id INTEGER PRIMARY KEY,  -- ID de ACARA
            nombre TEXT NOT NULL,
            modelo_id INTEGER NOT NULL,
            FOREIGN KEY (modelo_id) REFERENCES modelos(id)
        );
    """)

    # Crear tabla tipos de combustible
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipos_combustible (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        );
    """)

    # Insertar tipos comunes si no existen
    tipos_combustible = ['NAFTA', 'DIESEL', 'GNC', 'NAFTA/GNC', 'ELÉCTRICO', 'HÍBRIDO']
    for tipo in tipos_combustible:
        cursor.execute("INSERT OR IGNORE INTO tipos_combustible (nombre) VALUES (?)", (tipo,))

    # Crear tabla estados del vehículo
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estados_vehiculo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        );
    """)

    # Insertar estados posibles
    estados = ['Disponible', 'Reservado', 'Vendido']
    for estado in estados:
        cursor.execute("INSERT OR IGNORE INTO estados_vehiculo (nombre) VALUES (?)", (estado,))

    # Crear tabla principal de vehículos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            version_id INTEGER NOT NULL,
            anio INTEGER NOT NULL,
            tipo_combustible_id INTEGER NOT NULL,
            valor_estimado INTEGER,
            color TEXT,
            dominio TEXT,
            estado_id INTEGER DEFAULT 'Disponible',
            observaciones TEXT,
            fecha_ingreso DATE DEFAULT CURRENT_DATE,
            ubicacion_fisica TEXT,
            kms INTEGER,
            es_0km INTEGER DEFAULT 1,

            FOREIGN KEY (version_id) REFERENCES versiones(id)
            FOREIGN KEY (tipo_combustible_id) REFERENCES tipos_combustible(id),
            FOREIGN KEY (estado_id) REFERENCES estados_vehiculo(id)
        );
    """)

    conexion.commit()
    conexion.close()
