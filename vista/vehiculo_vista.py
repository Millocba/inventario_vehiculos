# vista/vehiculo_vista.py
import ttkbootstrap as tb
from ttkbootstrap.constants import BOTH, YES

class VehiculoVista(tb.Window):
    def __init__(self, controlador):
        super().__init__(themename="superhero")
        self.controlador = controlador
        self.title("Inventario de Vehículos")
        self.geometry("1000x700")
        self.minsize(900, 600)

        frame = tb.Frame(self, padding=15)
        frame.pack(fill=BOTH, expand=YES)

        # === FILA 0: Año, Color, Dominio ===
        self.label_anio = tb.Label(frame, text="Año:", font=("Segoe UI", 11))
        self.entry_anio = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_color = tb.Label(frame, text="Color:", font=("Segoe UI", 11))
        self.entry_color = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_dominio = tb.Label(frame, text="Dominio:", font=("Segoe UI", 11))
        self.entry_dominio = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_anio.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_anio.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.label_color.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.entry_color.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
        self.label_dominio.grid(row=0, column=4, sticky="e", padx=5, pady=5)
        self.entry_dominio.grid(row=0, column=5, sticky="ew", padx=5, pady=5)

        # === FILA 1: Marca, Modelo ===
        self.label_marca = tb.Label(frame, text="Marca:", font=("Segoe UI", 11))
        self.combobox_marca = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_modelo = tb.Label(frame, text="Modelo:", font=("Segoe UI", 11))
        self.combobox_modelo = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_marca.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.combobox_marca.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.label_modelo.grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.combobox_modelo.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 2: Versión, Combustible ===
        self.label_version = tb.Label(frame, text="Versión:", font=("Segoe UI", 11))
        self.combobox_version = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_combustible = tb.Label(frame, text="Combustible:", font=("Segoe UI", 11))
        self.combobox_combustible = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_version.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.combobox_version.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.label_combustible.grid(row=2, column=2, sticky="e", padx=5, pady=5)
        self.combobox_combustible.grid(row=2, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 3: Estado, Valor, Kms ===
        self.label_estado = tb.Label(frame, text="Estado:", font=("Segoe UI", 11))
        self.combobox_estado = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_valor = tb.Label(frame, text="Valor estimado:", font=("Segoe UI", 11))
        self.entry_valor = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_kms = tb.Label(frame, text="Kms:", font=("Segoe UI", 11))
        self.entry_kms = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_estado.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.combobox_estado.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        self.label_valor.grid(row=3, column=2, sticky="e", padx=5, pady=5)
        self.entry_valor.grid(row=3, column=3, sticky="ew", padx=5, pady=5)
        self.label_kms.grid(row=3, column=4, sticky="e", padx=5, pady=5)
        self.entry_kms.grid(row=3, column=5, sticky="ew", padx=5, pady=5)

        # === FILA 4: Ubicación, 0km, Observaciones ===
        self.label_ubicacion = tb.Label(frame, text="Ubicación física:", font=("Segoe UI", 11))
        self.entry_ubicacion = tb.Entry(frame, font=("Segoe UI", 11))

        self.check_0km_var = tb.IntVar()
        self.check_0km = tb.Checkbutton(frame, text="0 km", variable=self.check_0km_var, bootstyle="success")

        self.label_observaciones = tb.Label(frame, text="Observaciones:", font=("Segoe UI", 11))
        self.entry_observaciones = tb.Entry(frame, font=("Segoe UI", 11))  # o tb.Text si querés multilinea

        self.label_ubicacion.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_ubicacion.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        self.check_0km.grid(row=4, column=2, sticky="w", padx=5, pady=5)
        self.label_observaciones.grid(row=4, column=3, sticky="e", padx=5, pady=5)
        self.entry_observaciones.grid(row=4, column=4, columnspan=2, sticky="ew", padx=5, pady=5)

        # === FILA 5: Botones y búsqueda ===
        self.boton_agregar = tb.Button(frame, text="Agregar", bootstyle="success-outline", command=self.controlador.agregar_vehiculo)
        self.boton_actualizar = tb.Button(frame, text="Actualizar", bootstyle="warning-outline", command=self.controlador.actualizar_vehiculo)
        self.boton_eliminar = tb.Button(frame, text="Eliminar", bootstyle="danger-outline", command=self.controlador.eliminar_vehiculo)
        self.entry_busqueda = tb.Entry(frame, font=("Segoe UI", 11))
        self.boton_buscar = tb.Button(frame, text="Buscar", bootstyle="info-outline", command=self.controlador.buscar_vehiculo)

        self.boton_agregar.grid(row=5, column=0, sticky="ew", padx=5, pady=10)
        self.boton_actualizar.grid(row=5, column=1, sticky="ew", padx=5, pady=10)
        self.boton_eliminar.grid(row=5, column=2, sticky="ew", padx=5, pady=10)
        self.entry_busqueda.grid(row=5, column=3, sticky="ew", padx=5, pady=10)
        self.boton_buscar.grid(row=5, column=4, sticky="ew", padx=5, pady=10)

        # === FILA 6: Tabla ===
        self.tabla = tb.Treeview(frame, columns=("ID", "Marca", "Modelo", "Versión", "Año", "Color", "Valor", "Combustible", "Kms"), show="headings", bootstyle="dark")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=100)
        self.tabla.grid(row=6, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.controlador.seleccionar_fila)

        # === Expansión de filas y columnas ===
        frame.grid_rowconfigure(6, weight=1)
        for i in range(6):
            frame.grid_columnconfigure(i, weight=1)

        # Inicializar valores vacíos
        self.combobox_marca["values"] = []
        self.combobox_modelo["values"] = []
        self.combobox_version["values"] = []
        self.combobox_combustible["values"] = []
        self.combobox_estado["values"] = []
