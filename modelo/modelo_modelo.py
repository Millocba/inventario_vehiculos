# modelo/modelo_modelo.py
from base_datos.conexion import obtener_conexion

class ModeloModelo:
    def __init__(self, id, nombre, marca_id):
        self.id = id
        self.nombre = nombre
        self.marca_id = marca_id

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO modelos (id, nombre, marca_id)
            VALUES (?, ?, ?)
        """, (self.id, self.nombre, self.marca_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def guardar_si_no_existe(id, nombre, marca_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM modelos WHERE id = ?", (id,))
        existe = cursor.fetchone()
        if not existe:
            cursor.execute("""
                INSERT INTO modelos (id, nombre, marca_id)
                VALUES (?, ?, ?)
            """, (id, nombre, marca_id))
            conexion.commit()
        conexion.close()

    @staticmethod
    def obtener_por_marca(marca_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM modelos WHERE marca_id = ? ORDER BY nombre", (marca_id,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
