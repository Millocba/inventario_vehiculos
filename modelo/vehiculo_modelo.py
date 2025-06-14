# modelo/vehiculo_modelo.py

from base_datos.conexion import obtener_conexion

class VehiculoModelo:
    def __init__(self, modelo, anio, color, marca_id):
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.marca_id = marca_id

    # Crear un nuevo vehículo
    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO vehiculos (modelo, anio, color, marca_id)
            VALUES (?, ?, ?, ?)
        """, (self.modelo, self.anio, self.color, self.marca_id))
        conexion.commit()
        conexion.close()

    # Obtener todos los vehículos
    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT vehiculos.id, modelo, anio, color, marcas.nombre
            FROM vehiculos
            JOIN marcas ON vehiculos.marca_id = marcas.id
        """)
        vehiculos = cursor.fetchall()
        conexion.close()
        return vehiculos

    # Actualizar vehículo por ID
    @staticmethod
    def actualizar(vehiculo_id, modelo, anio, color, marca_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE vehiculos
            SET modelo = ?, anio = ?, color = ?, marca_id = ?
            WHERE id = ?
        """, (modelo, anio, color, marca_id, vehiculo_id))
        conexion.commit()
        conexion.close()

    # Eliminar vehículo por ID
    @staticmethod
    def eliminar(vehiculo_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM vehiculos WHERE id = ?", (vehiculo_id,))
        conexion.commit()
        conexion.close()

    # Buscar vehículos por modelo o color
    @staticmethod
    def buscar(texto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT vehiculos.id, modelo, anio, color, marcas.nombre
            FROM vehiculos
            JOIN marcas ON vehiculos.marca_id = marcas.id
            WHERE modelo LIKE ? OR color LIKE ?
        """, (f"%{texto}%", f"%{texto}%"))
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    
    # Obtener vehículos por marca
    @staticmethod
    def obtener_por_marca(marca_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT vehiculos.id, modelo, anio, color, marcas.nombre
            FROM vehiculos
            JOIN marcas ON vehiculos.marca_id = marcas.id
            WHERE vehiculos.marca_id = ?
        """, (marca_id,))
        vehiculos = cursor.fetchall()
        conexion.close()
        return vehiculos
