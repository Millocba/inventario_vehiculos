# controlador/vehiculo_controlador.py

from modelo.vehiculo_modelo import VehiculoModelo
from modelo.marca_modelo import MarcaModelo
from vista.vehiculo_vista import VehiculoVista

class VehiculoControlador:
    def __init__(self):
        self.vista = VehiculoVista(self)
        self.marcas = {}
        self.vehiculo_id_seleccionado = None
        self.inicializar()

    # Cargar marcas en el Combobox
    def inicializar(self):
        marcas = MarcaModelo.obtener_todas()
        nombres_marcas = [m[1] for m in marcas]
        self.marcas = {m[1]: m[0] for m in marcas}
        self.vista.combobox_marca["values"] = nombres_marcas
        self.refrescar_tabla()

    # Agregar vehículo nuevo
    def agregar_vehiculo(self):
        modelo = self.vista.entry_modelo.get()
        anio = self.vista.entry_anio.get()
        color = self.vista.entry_color.get()
        marca_nombre = self.vista.combobox_marca.get()

        if not (modelo and anio.isdigit() and color and marca_nombre):
            return

        marca_id = self.marcas.get(marca_nombre)
        vehiculo = VehiculoModelo(modelo, int(anio), color, marca_id)
        vehiculo.guardar()
        self.limpiar_formulario()
        self.refrescar_tabla()

    # Actualizar vehículo seleccionado
    def actualizar_vehiculo(self):
        if not self.vehiculo_id_seleccionado:
            return

        modelo = self.vista.entry_modelo.get()
        anio = self.vista.entry_anio.get()
        color = self.vista.entry_color.get()
        marca_nombre = self.vista.combobox_marca.get()

        if not (modelo and anio.isdigit() and color and marca_nombre):
            return

        marca_id = self.marcas.get(marca_nombre)
        VehiculoModelo.actualizar(self.vehiculo_id_seleccionado, modelo, int(anio), color, marca_id)
        self.limpiar_formulario()
        self.refrescar_tabla()

    # Eliminar vehículo seleccionado
    def eliminar_vehiculo(self):
        if not self.vehiculo_id_seleccionado:
            return
        VehiculoModelo.eliminar(self.vehiculo_id_seleccionado)
        self.limpiar_formulario()
        self.refrescar_tabla()

    # Buscar vehículos por texto
    def buscar_vehiculo(self):
        texto = self.vista.entry_busqueda.get()
        resultados = VehiculoModelo.buscar(texto)
        self.mostrar_tabla(resultados)

    # Mostrar todos los vehículos
    def refrescar_tabla(self):
        datos = VehiculoModelo.obtener_todos()
        self.mostrar_tabla(datos)

    # Cargar datos seleccionados al formulario
    def seleccionar_fila(self, event):
        seleccion = self.vista.tabla.selection()
        if seleccion:
            valores = self.vista.tabla.item(seleccion[0], "values")
            self.vehiculo_id_seleccionado = valores[0]
            self.vista.entry_modelo.delete(0, "end")
            self.vista.entry_modelo.insert(0, valores[1])
            self.vista.entry_anio.delete(0, "end")
            self.vista.entry_anio.insert(0, valores[2])
            self.vista.entry_color.delete(0, "end")
            self.vista.entry_color.insert(0, valores[3])
            self.vista.combobox_marca.set(valores[4])

    # Mostrar lista de vehículos en la tabla
    def mostrar_tabla(self, datos):
        for fila in self.vista.tabla.get_children():
            self.vista.tabla.delete(fila)
        for fila in datos:
            self.vista.tabla.insert("", "end", values=fila)

    # Limpiar formulario y selección
    def limpiar_formulario(self):
        self.vista.entry_modelo.delete(0, "end")
        self.vista.entry_anio.delete(0, "end")
        self.vista.entry_color.delete(0, "end")
        self.vista.combobox_marca.set("")
        self.vista.entry_busqueda.delete(0, "end")
        self.vehiculo_id_seleccionado = None
