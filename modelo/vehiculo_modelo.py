# modelo/vehiculo_modelo.py

from base_datos.conexion import obtener_conexion

class VehiculoModelo:
    def __init__(self, version_id, anio, tipo_combustible_id, valor_estimado, color, dominio, estado_id, observaciones, ubicacion_fisica, kms, es_0km):
        self.version_id = version_id
        self.anio = anio
        self.tipo_combustible_id = tipo_combustible_id
        self.valor_estimado = valor_estimado
        self.color = color
        self.dominio = dominio
        self.estado_id = estado_id
        self.observaciones = observaciones
        self.ubicacion_fisica = ubicacion_fisica
        self.kms = kms
        self.es_0km = es_0km

    def guardar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        print(f"Guardando vehículo: {self.version_id}, {self.anio}, {self.tipo_combustible_id}, {self.valor_estimado}, {self.color}, {self.dominio}, {self.estado_id}, {self.observaciones}, {self.ubicacion_fisica}, {self.kms}, {self.es_0km}")
        # Insertar vehículo en la base de datos
        cursor.execute("""
            INSERT INTO vehiculos (
                version_id, anio, tipo_combustible_id, valor_estimado, color,
                dominio, estado_id, observaciones, fecha_ingreso,
                ubicacion_fisica, kms, es_0km
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, DATE('now'), ?, ?, ?)
        """, (
            self.version_id, self.anio, self.tipo_combustible_id, self.valor_estimado,
            self.color, self.dominio, self.estado_id, self.observaciones,
            self.ubicacion_fisica, self.kms, self.es_0km
        ))
        conexion.commit()
        conexion.close()

    # Obtener todos los vehículos
    @staticmethod
    def obtener_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT vehiculos.id, marcas.nombre, modelos.nombre, versiones.nombre, vehiculos.anio, vehiculos.color, vehiculos.valor_estimado, tipos_combustible.nombre, vehiculos.kms
            FROM vehiculos
            JOIN versiones ON vehiculos.version_id = versiones.id
            JOIN modelos ON versiones.modelo_id = modelos.id
            JOIN marcas ON modelos.marca_id = marcas.id
            JOIN tipos_combustible ON vehiculos.tipo_combustible_id = tipos_combustible.id
            JOIN estados_vehiculo ON vehiculos.estado_id = estados_vehiculo.id
            WHERE estados_vehiculo.nombre = 'Disponible'

        """)
        vehiculos = cursor.fetchall()
        conexion.close()
        return vehiculos
    
    # Obtener vehículo por ID para editar
    @staticmethod
    def obtener_por_id(vehiculo_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT vehiculos.id, marcas.nombre, modelos.nombre, versiones.nombre, vehiculos.anio, tipos_combustible.nombre, vehiculos.valor_estimado, vehiculos.color, vehiculos.dominio, estados_vehiculo.nombre, vehiculos.observaciones, vehiculos.ubicacion_fisica, vehiculos.kms, vehiculos.es_0km
            FROM vehiculos
            JOIN versiones ON vehiculos.version_id = versiones.id
            JOIN modelos ON versiones.modelo_id = modelos.id
            JOIN marcas ON modelos.marca_id = marcas.id
            JOIN tipos_combustible ON vehiculos.tipo_combustible_id = tipos_combustible.id
            JOIN estados_vehiculo ON vehiculos.estado_id = estados_vehiculo.id
            WHERE vehiculos.id = ?
        """, (vehiculo_id,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado

    # Actualizar vehículo por ID
    @staticmethod
    def actualizar(vehiculo_id, version_id, anio, tipo_combustible_id, valor_estimado, color, dominio, estado_id, observaciones, ubicacion_fisica, kms, es_0km):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE vehiculos
                       set version_id = ?, anio = ?, tipo_combustible_id = ?, valor_estimado = ?, color = ?, dominio = ?, estado_id = ?, observaciones = ?, ubicacion_fisica = ?, kms = ?, es_0km = ?
            WHERE id = ?
        """, (version_id, anio, tipo_combustible_id, valor_estimado, color, dominio, estado_id, observaciones, ubicacion_fisica, kms, es_0km, vehiculo_id))
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
            SELECT vehiculos.id, marcas.nombre, modelos.nombre, versiones.nombre, vehiculos.anio, vehiculos.color, vehiculos.valor_estimado, tipos_combustible.nombre, vehiculos.kms
            FROM vehiculos
            JOIN versiones ON vehiculos.version_id = versiones.id
            JOIN modelos ON versiones.modelo_id = modelos.id
            JOIN marcas ON modelos.marca_id = marcas.id
            JOIN tipos_combustible ON vehiculos.tipo_combustible_id = tipos_combustible.id
            WHERE modelos.nombre LIKE ? OR vehiculos.color LIKE ?
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
            SELECT vehiculos.id, marcas.nombre, modelos.nombre, versiones.nombre, vehiculos.anio, vehiculos.color, vehiculos.valor_estimado, tipos_combustible.nombre, vehiculos.kms
            FROM vehiculos
            JOIN versiones ON vehiculos.version_id = versiones.id
            JOIN modelos ON versiones.modelo_id = modelos.id
            JOIN marcas ON modelos.marca_id = marcas.id
            JOIN tipos_combustible ON vehiculos.tipo_combustible_id = tipos_combustible.id
            WHERE modelos.marca_id = ?
        """, (marca_id,))
        vehiculos = cursor.fetchall()
        conexion.close()
        return vehiculos
