import ttkbootstrap as tb
from ttkbootstrap.constants import BOTH, YES
from functools import partial

class VehiculoVista(tb.Window):
    def __init__(self, controlador):
        super().__init__(themename="superhero")
        self.controlador = controlador
        self.title("Inventario de Vehículos")
        self.geometry("1000x700")
        self.minsize(900, 600)

        frame = tb.Frame(self, padding=15)
        frame.pack(fill=BOTH, expand=YES)

        # === FILA 0: Marca, Combustible ===
        self.label_marca = tb.Label(frame, text="Marca:", font=("Segoe UI", 11))
        self.combobox_marca = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_combustible = tb.Label(frame, text="Combustible:", font=("Segoe UI", 11))
        self.combobox_combustible = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_marca.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.combobox_marca.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.label_combustible.grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.combobox_combustible.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 1: Modelo, Kms, ubicacion ===
        self.label_modelo = tb.Label(frame, text="Modelo:", font=("Segoe UI", 11))
        self.combobox_modelo = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_ubicacion = tb.Label(frame, text="Ubicación física:", font=("Segoe UI", 11))
        self.entry_ubicacion = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_kms = tb.Label(frame, text="Kms:", font=("Segoe UI", 11))
        self.entry_kms = tb.Entry(frame, font=("Segoe UI", 11))


        self.label_modelo.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.combobox_modelo.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.label_ubicacion.grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.entry_ubicacion.grid(row=1, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 2: Versión, Dominio ===
        self.label_version = tb.Label(frame, text="Versión:", font=("Segoe UI", 11))
        self.combobox_version = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_dominio = tb.Label(frame, text="Dominio:", font=("Segoe UI", 11))
        self.entry_dominio = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_version.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.combobox_version.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        self.label_dominio.grid(row=2, column=2, sticky="e", padx=5, pady=5)
        self.entry_dominio.grid(row=2, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 3: Año, Valor ===
        self.label_anio = tb.Label(frame, text="Año:", font=("Segoe UI", 11))
        self.entry_anio = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_valor = tb.Label(frame, text="Valor estimado:", font=("Segoe UI", 11))
        self.entry_valor = tb.Entry(frame, font=("Segoe UI", 11))

        self.label_anio.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_anio.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        self.label_valor.grid(row=3, column=2, sticky="e", padx=5, pady=5)
        self.entry_valor.grid(row=3, column=3, sticky="ew", padx=5, pady=5)

        # === FILA 4: Color, KM, Observaciones ===
        self.label_color = tb.Label(frame, text="Color:", font=("Segoe UI", 11))
        self.entry_color = tb.Entry(frame, font=("Segoe UI", 11))

        self.check_0km_var = tb.IntVar()  # Por defecto 0km seleccionado
        self.check_0km_var.set(1)  # Por defecto 0km está seleccionado
        self.check_0km = tb.Checkbutton(frame, text="0 km", variable=self.check_0km_var, bootstyle="success")

        self.label_color.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_color.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        self.label_kms.grid(row=4, column=2, sticky="e", padx=5, pady=5)
        self.entry_kms.grid(row=4, column=3, sticky="ew", padx=5, pady=5)
        self.check_0km.grid(row=4, column=4, sticky="w", padx=5, pady=5)

        self.label_observaciones = tb.Label(frame, text="Observaciones:", font=("Segoe UI", 11))
        self.label_observaciones.grid(row=0, column=4, sticky="se", padx=5, pady=5)

        self.entry_observaciones = tb.ScrolledText(frame, font=("Segoe UI", 11))
        self.entry_observaciones.grid(row=1, column=4, rowspan=3, columnspan=2, sticky="nsew", padx=5, pady=5)
        self.entry_observaciones.configure(height=5, width=30)


        # === FILA 5: Estado ===
        self.label_estado = tb.Label(frame, text="Estado:", font=("Segoe UI", 11))
        self.combobox_estado = tb.Combobox(frame, state="readonly", font=("Segoe UI", 11))

        self.label_estado.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.combobox_estado.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        # === FILA 6: Botones ===
        self.boton_agregar = tb.Button(frame, text="Agregar", bootstyle="success-outline", command=self.controlador.agregar_vehiculo)
        self.boton_actualizar = tb.Button(frame, text="Actualizar", bootstyle="warning-outline", command=self.controlador.actualizar_vehiculo)
        self.boton_eliminar = tb.Button(frame, text="Eliminar", bootstyle="danger-outline", command=self.controlador.eliminar_vehiculo)
        self.boton_limpiar =  tb.Button(frame, text="Limpiar", bootstyle="info-outline", command=self.controlador.limpiar_formulario)
        self.entry_busqueda = tb.Entry(frame, font=("Segoe UI", 11))
        self.boton_buscar = tb.Button(frame, text="Buscar", bootstyle="info-outline", command=self.controlador.buscar_vehiculo)

        self.boton_agregar.grid(row=6, column=0, sticky="ew", padx=5, pady=10)
        self.boton_actualizar.grid(row=6, column=1, sticky="ew", padx=5, pady=10)
        self.boton_eliminar.grid(row=6, column=2, sticky="ew", padx=5, pady=10)
        self.boton_limpiar.grid(row=6, column=3, sticky="ew", padx=5, pady=10)
        self.entry_busqueda.grid(row=6, column=4, sticky="ew", padx=5, pady=5)
        self.boton_buscar.grid(row=6, column=5, sticky="ew", padx=5, pady=5)

        # === FILA 7: Tabla con íconos ===
        self.tabla = tb.Treeview(
            frame,
            columns=("ID", "Marca", "Modelo", "Versión", "Año", "Color", "Valor", "Combustible", "Kms"),
            show="headings",
            bootstyle="dark"
        )
        for col in ("ID", "Marca", "Modelo", "Versión", "Año", "Color", "Valor", "Combustible", "Kms"):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=100)

        self.tabla.grid(row=7, column=0, columnspan=6, sticky="nsew", padx=10, pady=10)
        self.tabla.bind("<<TreeviewSelect>>", self.controlador.seleccionar_fila)

        # === Expansión ===
        frame.grid_rowconfigure(7, weight=1)
        for i in range(6):
            frame.grid_columnconfigure(i, weight=1)

        # === Validación dinámica ===
        self.boton_agregar.configure(state="disabled")
        self.boton_actualizar.configure(state="disabled")
        self.boton_eliminar.configure(state="disabled")

        # Orden de tabulación
        orden = [
                self.combobox_marca,
                self.combobox_modelo,
                self.combobox_version,
                self.entry_anio,
                self.entry_color,
                self.combobox_estado,
                self.combobox_combustible,
                self.entry_ubicacion,
                self.entry_dominio,
                self.entry_valor,
                self.entry_kms,
                self.entry_observaciones,
                self.boton_agregar,
                self.entry_busqueda,
                ]

        for i, widget in enumerate(orden):
                siguiente = orden[(i + 1) % len(orden)]
                widget.bind("<Tab>", partial(self._cambiar_foco, siguiente))



        # Vincular eventos de validación
        for widget in [
            self.combobox_marca,
            self.combobox_modelo,
            self.combobox_version,
            self.combobox_combustible,
            self.combobox_estado,
            self.entry_anio
        ]:
            widget.bind("<<ComboboxSelected>>", self.validar_formulario)
            widget.bind("<KeyRelease>", self.validar_formulario)
            widget.bind("<FocusOut>", self.validar_formulario)

        self.entry_anio.bind("<KeyRelease>", self.validar_formulario)
        self.entry_kms.bind("<KeyRelease>", self._on_kms_change)
        self.check_0km.configure(command=self._on_check_0km)


        # === Inicializar combos ===
        self.combobox_marca["values"] = []
        self.combobox_modelo["values"] = []
        self.combobox_version["values"] = []
        self.combobox_combustible["values"] = []
        self.combobox_estado["values"] = []

    # Validar que el formulario esté completo
    def validar_formulario(self, event=None):
        campos = [
            self.combobox_marca.get(),
            self.combobox_modelo.get(),
            self.combobox_version.get(),
            self.entry_anio.get(),
            self.combobox_combustible.get(),
            self.combobox_estado.get()
        ]
        habilitar = all(c.strip() for c in campos) and self.entry_anio.get().isdigit()
        estado = "normal" if habilitar else "disabled"
        self.boton_agregar.configure(state=estado)

    # Si se escribe kms, se desactiva el check 0km
    def _on_kms_change(self, event):
        texto = self.entry_kms.get()
        if texto.strip().isdigit() and int(texto) > 0:
            self.check_0km_var.set(0)
        

    # Si se marca 0km, se limpia el campo kms
    def _on_check_0km(self):
        if self.check_0km_var.get() == 1:
            self.entry_kms.delete(0, 'end')

    def _cambiar_foco(self, siguiente_widget, event):
        siguiente_widget.focus_set()
        return "break"
        

