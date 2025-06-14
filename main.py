# main.py

from base_datos.conexion import crear_tablas
from modelo.marca_modelo import MarcaModelo
from controlador.vehiculo_controlador import VehiculoControlador

def insertar_marcas_iniciales():
    marcas = ["Toyota", "Ford", "Chevrolet", "Volkswagen", "Renault"]
    for nombre in marcas:
        marca = MarcaModelo(nombre)
        marca.guardar()

if __name__ == "__main__":
    # Crear tablas y datos iniciales
    crear_tablas()
    insertar_marcas_iniciales()

    # Iniciar la aplicación
    app = VehiculoControlador()
    app.vista.mainloop()
