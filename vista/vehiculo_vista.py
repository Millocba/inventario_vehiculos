# vista/vehiculo_vista.py
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class VehiculoVista(tb.Window):
    def __init__(self, controlador):
        super().__init__(themename="darkly")
        self.controlador = controlador
        self.title("Inventario de Vehículos")
        self.geometry("800x600")
        self.minsize(700, 500)

        # Frame contenedor para orden
        frame = tb.Frame(self, padding=15)
        frame.pack(fill=BOTH, expand=YES)

        # Etiquetas y Entrys / Combobox
        self.label_modelo = tb.Label(frame, text="Modelo:", font=("Segoe UI", 11))
        self.entry_modelo = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_anio = tb.Label(frame, text="Año:", font=("Segoe UI", 11))
        self.entry_anio = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_color = tb.Label(frame, text="Color:", font=("Segoe UI", 11))
        self.entry_color = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_marca = tb.Label(frame, text="Marca:", font=("Segoe UI", 11))
        self.combobox_marca = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        # Botones con estilo bootstyle
        self.boton_agregar = tb.Button(frame, text="Agregar", bootstyle="success-outline", command=self.controlador.agregar_vehiculo)
        self.boton_actualizar = tb.Button(frame, text="Actualizar", bootstyle="warning-outline", command=self.controlador.actualizar_vehiculo)
        self.boton_eliminar = tb.Button(frame, text="Eliminar", bootstyle="danger-outline", command=self.controlador.eliminar_vehiculo)
        self.boton_buscar = tb.Button(frame, text="Buscar", bootstyle="info-outline", command=self.controlador.buscar_vehiculo)

        # Campo de búsqueda
        self.entry_busqueda = tb.Entry(frame, font=("Segoe UI", 11))

        # Tabla
        self.tabla = tb.Treeview(frame, columns=("ID", "Modelo", "Año", "Color", "Marca"), show="headings", bootstyle="dark")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=120)

        self.tabla.bind("<<TreeviewSelect>>", self.controlador.seleccionar_fila)

        # Layout con grid y paddings
        self.label_modelo.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_modelo.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        self.label_anio.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_anio.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.label_color.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_color.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.label_marca.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.combobox_marca.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        self.boton_agregar.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
        self.boton_actualizar.grid(row=4, column=1, sticky="ew", padx=5, pady=10)
        self.boton_eliminar.grid(row=4, column=2, sticky="ew", padx=5, pady=10)

        self.entry_busqueda.grid(row=4, column=3, sticky="ew", padx=5, pady=10)
        self.boton_buscar.grid(row=4, column=4, sticky="ew", padx=5, pady=10)

        self.tabla.grid(row=5, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Expansión para que tabla crezca al redimensionar
        frame.grid_rowconfigure(5, weight=1)
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)

        # Optional: Tooltip para botones (si querés te ayudo con esto también)

