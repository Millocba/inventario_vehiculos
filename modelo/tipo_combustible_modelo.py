# modelo/tipo_combustible_modelo.py
from base_datos.conexion import obtener_conexion

class TipoCombustibleModelo:
    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM tipos_combustible ORDER BY nombre")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
