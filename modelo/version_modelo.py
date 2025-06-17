# modelo/version_modelo.py
from base_datos.conexion import obtener_conexion

class VersionModelo:
    def __init__(self, id, nombre, modelo_id):
        self.id = id
        self.nombre = nombre
        self.modelo_id = modelo_id

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO versiones (id, nombre, modelo_id)
            VALUES (?, ?, ?)
        """, (self.id, self.nombre, self.modelo_id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def guardar_si_no_existe(id, nombre, modelo_id, conexion=None):
        cerrar = False
        if conexion is None:
            conexion = obtener_conexion()
            cerrar = True

        cursor = conexion.cursor()
        cursor.execute("SELECT 1 FROM versiones WHERE id = ?", (id,))
        existe = cursor.fetchone()
        if not existe:
            cursor.execute("""
                INSERT INTO versiones (id, nombre, modelo_id)
                VALUES (?, ?, ?)
            """, (id, nombre, modelo_id))
            if cerrar:
                conexion.commit()

        if cerrar:
            conexion.close()

    @staticmethod
    def obtener_por_nombre(nombrev, nombrem):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT v.id FROM versiones v JOIN modelos m ON v.modelo_id = m.id WHERE v.nombre = ? AND m.nombre = ?", (nombrev, nombrem))
        resultado = cursor.fetchone()
        return resultado

    @staticmethod
    def obtener_por_modelo(modelo_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM versiones WHERE modelo_id = ? ORDER BY nombre", (modelo_id,))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
