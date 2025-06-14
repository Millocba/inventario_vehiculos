# vista/vehiculo_vista.py

import tkinter as tk
from tkinter import ttk, messagebox

class VehiculoVista(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.title("Inventario de Vehículos")
        self.geometry("700x500")
        self.controlador = controlador

        # Widgets de entrada
        self.label_modelo = tk.Label(self, text="Modelo:")
        self.entry_modelo = tk.Entry(self)

        self.label_anio = tk.Label(self, text="Año:")
        self.entry_anio = tk.Entry(self)

        self.label_color = tk.Label(self, text="Color:")
        self.entry_color = tk.Entry(self)

        self.label_marca = tk.Label(self, text="Marca:")
        self.combobox_marca = ttk.Combobox(self, state="readonly")

        # Botones
        self.boton_agregar = tk.Button(self, text="Agregar", command=self.controlador.agregar_vehiculo)
        self.boton_actualizar = tk.Button(self, text="Actualizar", command=self.controlador.actualizar_vehiculo)
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.controlador.eliminar_vehiculo)
        self.boton_buscar = tk.Button(self, text="Buscar", command=self.controlador.buscar_vehiculo)

        # Campo de búsqueda
        self.entry_busqueda = tk.Entry(self)

        # Tabla de resultados
        self.tabla = ttk.Treeview(self, columns=("ID", "Modelo", "Año", "Color", "Marca"), show="headings")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)

        self.tabla.bind("<<TreeviewSelect>>", self.controlador.seleccionar_fila)

        # Posicionar widgets con grid
        self.label_modelo.grid(row=0, column=0, sticky="e")
        self.entry_modelo.grid(row=0, column=1)

        self.label_anio.grid(row=1, column=0, sticky="e")
        self.entry_anio.grid(row=1, column=1)

        self.label_color.grid(row=2, column=0, sticky="e")
        self.entry_color.grid(row=2, column=1)

        self.label_marca.grid(row=3, column=0, sticky="e")
        self.combobox_marca.grid(row=3, column=1)

        self.boton_agregar.grid(row=4, column=0, pady=10)
        self.boton_actualizar.grid(row=4, column=1)
        self.boton_eliminar.grid(row=4, column=2)
        self.boton_buscar.grid(row=4, column=4)
        self.entry_busqueda.grid(row=4, column=3)

        self.tabla.grid(row=5, column=0, columnspan=5, padx=10, pady=20, sticky="nsew")

        # Expandir tabla con resize
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(1, weight=1)
