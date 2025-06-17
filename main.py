# main.py

from base_datos.conexion import crear_tablas
from modelo.marca_modelo import MarcaModelo
from controlador.vehiculo_controlador import VehiculoControlador

if __name__ == "__main__":
    # Crear tablas si no existen
    crear_tablas()

    # Cargar marcas desde la API de ACARA
    MarcaModelo.cargar_desde_api()

    # Iniciar la app
    app = VehiculoControlador()
    app.vista.mainloop()
