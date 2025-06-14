# modelo/marca_modelo.py

from base_datos.conexion import obtener_conexion

class MarcaModelo:
    def __init__(self, nombre):
        self.nombre = nombre

    # Guardar una nueva marca
    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO marcas (nombre)
            VALUES (?)
        """, (self.nombre,))
        conexion.commit()
        conexion.close()

    # Obtener todas las marcas
    @staticmethod
    def obtener_todas():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM marcas")
        marcas = cursor.fetchall()
        conexion.close()
        return marcas
