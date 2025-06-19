# controlador/vehiculo_controlador.py

from base_datos.conexion import obtener_conexion
from modelo.vehiculo_modelo import VehiculoModelo
from modelo.marca_modelo import MarcaModelo
from vista.vehiculo_vista import VehiculoVista
from modelo.modelo_modelo import ModeloModelo
from modelo.version_modelo import VersionModelo
from modelo.estado_vehiculo_modelo import EstadoVehiculoModelo
from modelo.tipo_combustible_modelo import TipoCombustibleModelo
import requests

class VehiculoControlador:
    def __init__(self):
        # Se inicializa la vista y se pasa el controlador como referencia
        self.vista = VehiculoVista(self)
        self.marcas = {}  # Diccionario para mapear nombre de marca → id
        self.combustibles = {}  # Diccionario para mapear nombre de combustible → id
        self.estados_vehiculo = {}  # Diccionario para mapear nombre de estado
        self.versiones = {}  # Diccionario para mapear nombre de versión → id
        self.vehiculo_id_seleccionado = None

        # Se vincula el evento de selección de marca con el método que actualiza los modelos
        self.vista.combobox_marca.bind("<<ComboboxSelected>>", self.actualizar_modelos_por_marca)

        # Se vincula el evento de selección de modelo con el método que actualiza las versiones
        self.vista.combobox_modelo.bind("<<ComboboxSelected>>", self.actualizar_versiones_por_modelo)

        # Carga inicial de marcas y vehículos
        self.inicializar()

    # Carga marcas desde la base local y refresca la tabla con todos los vehículos
    def inicializar(self):
        marcas = MarcaModelo.obtener_todas()
        nombres_marcas = [m[1] for m in marcas]
        self.marcas = {m[1]: m[0] for m in marcas}
        self.vista.combobox_marca["values"] = nombres_marcas
        combustibles = TipoCombustibleModelo.obtener_todos()
        nombres_combustibles = [c[1] for c in combustibles]
        self.combustibles = {c[1]: c[0] for c in combustibles}
        self.vista.combobox_combustible["values"] = nombres_combustibles
        estados = EstadoVehiculoModelo.obtener_todos()   
        nombres_estados = [e[1] for e in estados]
        self.estados_vehiculo = {e[1]: e[0] for e in estados}
        self.vista.combobox_estado["values"] = nombres_estados

        self.refrescar_tabla()

    # Agrega un nuevo vehículo con los datos ingresados en el formulario
    def agregar_vehiculo(self):
        try:
            version_nombre = self.vista.combobox_version.get()
            modelo_nombre = self.vista.combobox_modelo.get()
            anio = self.vista.entry_anio.get()
            color = self.vista.entry_color.get()
            dominio = self.vista.entry_dominio.get()
            ubicacion = self.vista.entry_ubicacion.get()
            observaciones = self.vista.entry_observaciones.get("1.0", "end-1c").strip()
            kms = self.vista.entry_kms.get()
            valor_estimado = self.vista.entry_valor.get()
            combustible_nombre = self.vista.combobox_combustible.get()
            estado_nombre = self.vista.combobox_estado.get()
            es_0km = self.vista.check_0km_var.get()

            # Validación básica
            if not (version_nombre and anio.isdigit() and combustible_nombre and estado_nombre):
                print("⚠️ Faltan datos obligatorios.")
                return

            # Obtener IDs directamente desde los diccionarios en memoria
            version_id = VersionModelo.obtener_por_nombre(version_nombre, modelo_nombre)[0]
            tipo_combustible_id = self.combustibles.get(combustible_nombre)
            estado_id = self.estados_vehiculo.get(estado_nombre)

            if not version_id or not tipo_combustible_id or not estado_id:
                print(f"❌ ID faltante. version: {version_id}, combustible: {tipo_combustible_id}, estado: {estado_id}")
                return

            print(f"Agregando vehículo: {version_id}, {anio}, {tipo_combustible_id}, {valor_estimado}, {color}, {dominio}, {estado_id}, {observaciones}, {ubicacion}, {kms}, {es_0km}")
            vehiculo = VehiculoModelo(
                version_id=version_id,
                anio=int(anio),
                tipo_combustible_id=tipo_combustible_id,
                valor_estimado=int(valor_estimado) if valor_estimado else 0,
                color=color,
                dominio=dominio,
                estado_id=estado_id,
                observaciones=observaciones,
                ubicacion_fisica=ubicacion,
                kms=int(kms) if kms else 0,
                es_0km=es_0km
            )
            # Guardar el vehículo en la base de datos
            vehiculo.guardar()
            self.limpiar_formulario()
            self.refrescar_tabla()

        except Exception as e:
            print("Error al agregar vehículo:", e)


    # Actualiza los datos del vehículo seleccionado
    def actualizar_vehiculo(self):
        if not self.vehiculo_id_seleccionado:
            return

        version_nombre = self.vista.combobox_version.get()
        modelo_nombre = self.vista.combobox_modelo.get()
        anio = self.vista.entry_anio.get()
        color = self.vista.entry_color.get()
        dominio = self.vista.entry_dominio.get()
        ubicacion = self.vista.entry_ubicacion.get()
        observaciones = self.vista.entry_observaciones.get("1.0", "end-1c").strip()
        kms = self.vista.entry_kms.get()
        valor_estimado = self.vista.entry_valor.get()
        combustible_nombre = self.vista.combobox_combustible.get()
        estado_nombre = self.vista.combobox_estado.get()
        es_0km = self.vista.check_0km_var.get()

        # Validación básica
        if not (version_nombre and anio.isdigit() and combustible_nombre and estado_nombre):
            print("⚠️ Faltan datos obligatorios.")
            return

        # Obtener IDs directamente desde los diccionarios en memoria
        version_id = VersionModelo.obtener_por_nombre(version_nombre, modelo_nombre)[0]
        tipo_combustible_id = self.combustibles.get(combustible_nombre)
        estado_id = self.estados_vehiculo.get(estado_nombre)


        VehiculoModelo.actualizar(self.vehiculo_id_seleccionado,
            version_id=version_id,
            anio=int(anio),
            tipo_combustible_id=tipo_combustible_id,
            valor_estimado=int(valor_estimado) if valor_estimado else 0,
            color=color,
            dominio=dominio,
            estado_id=estado_id,
            observaciones=observaciones,
            ubicacion_fisica=ubicacion,
            kms=int(kms) if kms else 0,
            es_0km=es_0km
        )
        self.limpiar_formulario()
        self.refrescar_tabla()

    # Elimina el vehículo actualmente seleccionado
    def eliminar_vehiculo(self):
        if not self.vehiculo_id_seleccionado:
            return
        VehiculoModelo.eliminar(self.vehiculo_id_seleccionado)
        self.limpiar_formulario()
        self.refrescar_tabla()

    # Filtra la tabla por texto ingresado en el campo de búsqueda
    def buscar_vehiculo(self):
        texto = self.vista.entry_busqueda.get()
        resultados = VehiculoModelo.buscar(texto)
        self.mostrar_tabla(resultados)

    # Vuelve a cargar todos los vehículos en la tabla
    def refrescar_tabla(self):
        datos = VehiculoModelo.obtener_todos()
        self.mostrar_tabla(datos)

    def seleccionar_fila(self, event):
        seleccion = self.vista.tabla.selection()
        if not seleccion:
            return

        valores = self.vista.tabla.item(seleccion[0], "values")
        vehiculo_id = valores[0]
        self.vehiculo_id_seleccionado = vehiculo_id

        # Obtener datos completos desde la base
        datos = VehiculoModelo.obtener_por_id(vehiculo_id)
        if not datos:
            print("No se encontraron datos del vehículo.")
            return

        (
            _id,
            marca,
            modelo,
            version,
            anio,
            combustible,
            valor_estimado,
            color,
            dominio,
            estado,
            observaciones,
            ubicacion,
            kms,
            es_0km
        ) = datos

        # Cargar los campos en el formulario
        self.vista.combobox_marca.set(marca)
        self.vista.combobox_modelo.set(modelo)
        self.vista.combobox_version.set(version)

        self.vista.entry_anio.delete(0, "end")
        self.vista.entry_anio.insert(0, anio)

        self.vista.combobox_combustible.set(combustible)

        self.vista.entry_valor.delete(0, "end")
        self.vista.entry_valor.insert(0, valor_estimado if valor_estimado is not None else "")

        self.vista.entry_color.delete(0, "end")
        self.vista.entry_color.insert(0, color)

        self.vista.entry_dominio.delete(0, "end")
        self.vista.entry_dominio.insert(0, dominio)

        self.vista.combobox_estado.set(estado)

        self.vista.entry_observaciones.delete(1.0, "end")
        self.vista.entry_observaciones.insert(1.0, observaciones if observaciones else "")

        self.vista.entry_ubicacion.delete(0, "end")
        self.vista.entry_ubicacion.insert(0, ubicacion if ubicacion else "")

        self.vista.entry_kms.delete(0, "end")
        self.vista.entry_kms.insert(0, kms if kms is not None else "")

        self.vista.check_0km_var.set(es_0km or 0)
        # Actualizar el estado del botón de eliminar
        self.vista.boton_eliminar.configure(state="normal")
        # Actualizar el estado del botón de actualizar
        self.vista.boton_actualizar.configure(state="normal")
        # deshabilitar el botón de agregar
        self.vista.boton_agregar.configure(state="disabled")

    # Llena la tabla con los datos recibidos
    def mostrar_tabla(self, datos):
        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)
        for fila in datos:
            self.vista.tabla.insert("", "end", values=fila)

    # Limpia todos los campos del formulario y resetea selección
    def limpiar_formulario(self):
        self.vista.combobox_marca.set("")
        self.vista.combobox_modelo.set("")
        self.vista.combobox_version.set("")
        self.vista.entry_anio.delete(0, "end")
        self.vista.entry_color.delete(0, "end")
        self.vista.entry_dominio.delete(0, "end")
        self.vista.entry_ubicacion.delete(0, "end")
        self.vista.entry_valor.delete(0, "end")
        self.vista.entry_kms.delete(0, "end")
        self.vista.entry_observaciones.delete(1.0, "end")
        self.vista.combobox_combustible.set("")
        self.vista.combobox_estado.set("")
        self.vista.check_0km_var.set(1)
        self.vista.entry_busqueda.delete(0, "end")
        self.vehiculo_id_seleccionado = None

        # Deshabilitar botones de agregar, actualizar y eliminar
        self.vista.boton_actualizar.configure(state="disabled")
        self.vista.boton_eliminar.configure(state="disabled")
        self.vista.boton_agregar.configure(state="disabled")



    # Consulta a la API de ACARA para cargar los modelos de la marca seleccionada
    def actualizar_modelos_por_marca(self, event=None):
        marca_nombre = self.vista.combobox_marca.get()
        marca_id = self.marcas.get(marca_nombre)

        # ✅ Limpiar combos dependientes
        self.vista.combobox_modelo.set("")
        self.vista.combobox_modelo["values"] = []

        self.vista.combobox_version.set("")
        self.vista.combobox_version["values"] = []

        if not marca_id:
            return

        try:
            # 1. Consultar modelos desde API ACARA
            url = f"https://api.acara.org.ar/api/v1/prices/model-list?vehiculeType=1&vehiculeBrandId={marca_id}"
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            modelos = datos.get("data", [])

            nombres_modelos = set()

            # 2. Guardar en base local si no existen
            for modelo in modelos:
                id_modelo = modelo["id"]
                nombre_modelo = modelo["name"].strip()
                ModeloModelo.guardar_si_no_existe(id_modelo, nombre_modelo, marca_id)
                nombres_modelos.add(nombre_modelo)

            # 3. Cargar combobox
            self.vista.combobox_modelo["values"] = sorted(nombres_modelos)
            self.vista.combobox_modelo.set("")

        except requests.RequestException as e:
            print("Error al obtener modelos:", e)


    def actualizar_versiones_por_modelo(self, event=None):
        modelo_nombre = self.vista.combobox_modelo.get()
        marca_nombre = self.vista.combobox_marca.get()

        marca_id = self.marcas.get(marca_nombre)
        if not marca_id or not modelo_nombre:
            print("Marca o modelo no seleccionados.")
            return

        # Buscar ID del modelo
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id FROM modelos
            WHERE nombre = ? AND marca_id = ?
        """, (modelo_nombre, marca_id))
        fila = cursor.fetchone()

        if not fila:
            conexion.close()
            print("❌ Modelo no encontrado en la base local.")
            return

        modelo_id = fila[0]

        try:
            url = f"https://api.acara.org.ar/api/v1/prices/version-list?vehiculeType=1&vehiculeBrandId={marca_id}&vehiculeModelId={modelo_id}"
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()
            versiones = datos.get("data", [])

            nombres_versiones = set()

            # Usar conexión compartida para evitar el lock
            for version in versiones:
                id_version = version["id"]
                nombre_version = version["name"].strip()
                VersionModelo.guardar_si_no_existe(id_version, nombre_version, modelo_id, conexion)
                nombres_versiones.add(nombre_version)

            conexion.commit()  # ✅ COMMIT ÚNICO
            conexion.close()

            # Actualizar combobox de versiones
            self.vista.combobox_version["values"] = sorted(nombres_versiones)
            self.vista.combobox_version.set("")

        except requests.RequestException as e:
            print("Error al obtener versiones:", e)

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
            # 🔴 NO hacer commit aquí si se está usando una conexión compartida

        if cerrar:
            conexion.commit()
            conexion.close()