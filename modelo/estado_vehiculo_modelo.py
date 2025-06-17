# modelo/estado_vehiculo_modelo.py
from base_datos.conexion import obtener_conexion

class EstadoVehiculoModelo:
    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM estados_vehiculo ORDER BY nombre")
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
