# modelo/marca_modelo.py

import requests
from base_datos.conexion import obtener_conexion

class MarcaModelo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO marcas (id, nombre)
            VALUES (?, ?)
        """, (self.id, self.nombre))
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

    @staticmethod
    def cargar_desde_api():
        url = "https://api.acara.org.ar/api/v1/prices/brand-list?vehiculeType=1"
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            marcas = datos.get("data", [])

            for marca in marcas:
                nueva = MarcaModelo(marca["id"], marca["name"])
                nueva.guardar()

        except requests.RequestException as e:
            print("Error al conectar con la API de ACARA:", e)

