"""ML Visualizer 2.0: interfaz didáctica basada en ttkbootstrap."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

import numpy as np
import ttkbootstrap as ttk
from configuracion import cargar_json, guardar_json
from dialogos import mostrar_acerca_de, mostrar_ayuda
from ml_utils import (
    DATASETS,
    MODELOS,
    MODOS,
    calcular_limites,
    calcular_mapa,
    entrenar_modelo,
    generar_dataset,
)
from ttkbootstrap.constants import DISABLED, EW, LEFT, NSEW
from visualizer import LienzoML

NOMBRE_APP = "ML Visualizer"
VERSION_APP = "2.0"
SIN_MODELO = "Ninguno — solo datos"
TEMA_INICIAL = "nord-dark"
MIGRACION_TEMAS = {
    "flatly": "bootstrap-light",
    "cosmo": "bootstrap-light",
    "litera": "one-light",
    "minty": "minty-light",
    "journal": "bootstrap-light",
    "darkly": "bootstrap-dark",
    "superhero": "nord-dark",
    "cyborg": "one-dark",
    "solar": "solarized-dark",
}

PARAMETROS_INICIALES = {
    "Regresión logística": {"C": 1.0},
    "KNN": {"vecinos": 5},
    "Árbol de decisión": {"profundidad": 4},
    "Random Forest": {"arboles": 50, "profundidad": 5},
    "Regresión lineal": {},
    "Regresión polinómica": {"grado": 2},
    "KNN regresión": {"vecinos": 5},
    "Árbol de regresión": {"profundidad": 4},
    "K-Means": {"clusters": 3},
}

PARAMETROS_UI = {
    "Regresión logística": (("C", "Regularización C", 0.1, 10.0, 0.1),),
    "KNN": (("vecinos", "Cantidad de vecinos", 1, 30, 1),),
    "Árbol de decisión": (("profundidad", "Profundidad máxima", 1, 20, 1),),
    "Random Forest": (
        ("arboles", "Cantidad de árboles", 5, 300, 5),
        ("profundidad", "Profundidad máxima", 1, 20, 1),
    ),
    "Regresión lineal": (),
    "Regresión polinómica": (("grado", "Grado del polinomio", 2, 10, 1),),
    "KNN regresión": (("vecinos", "Cantidad de vecinos", 1, 30, 1),),
    "Árbol de regresión": (("profundidad", "Profundidad máxima", 1, 20, 1),),
    "K-Means": (("clusters", "Cantidad de clusters", 2, 6, 1),),
}


class AplicacionML:
    # -------------------------------------------------------------------------
    # Inicializa la ventana, el estado de datos y las variables enlazadas a la GUI.
    # -------------------------------------------------------------------------
    def __init__(self) -> None:
        self.root = ttk.Window(themename=TEMA_INICIAL)
        self.root.minsize(1040, 650)
        try:
            self.root.state("zoomed")
        except tk.TclError:
            self.root.geometry("1280x720")

        self.rng = np.random.default_rng()
        self.seed_actual = int(self.rng.integers(0, 2**31 - 1))
        self.X = np.empty((0, 2))
        self.y: np.ndarray | None = None
        self.resultado = None
        self.limites = (-5.0, 5.0, -5.0, 5.0)
        self.mapa_clases = None
        self.mapa_prob = None
        self.parametros = {
            nombre: valores.copy() for nombre, valores in PARAMETROS_INICIALES.items()
        }
        self.variables_parametros: dict[str, tk.Variable] = {}
        self.ruta_configuracion: Path | None = None
        self.modificado = False
        self._cargando = True

        self.modo_var = tk.StringVar(value="Clasificación")
        self.dataset_var = tk.StringVar(value="Lunas")
        self.n_muestras_var = tk.IntVar(value=120)
        self.n_muestras_aplicadas = 120
        self.modelo_var = tk.StringVar(value=SIN_MODELO)
        self.mapa_var = tk.StringVar(value="Normal")
        self.detalles_var = tk.BooleanVar(value=True)
        self.tema_var = tk.StringVar(value=TEMA_INICIAL)
        self.metricas_var = tk.StringVar(value="")
        self.estado_var = tk.StringVar(value="Listo")
        self.prediccion_var = tk.StringVar(
            value="Mueva el cursor sobre el gráfico para explorar el modelo."
        )

        disponibles = set(self.root.theme_names())
        self.temas_claros = tuple(
            sorted(t for t in disponibles if t.endswith("-light"))
        )
        self.temas_oscuros = tuple(
            sorted(t for t in disponibles if t.endswith("-dark"))
        )
        self.temas_otros = tuple(
            sorted(disponibles - set(self.temas_claros) - set(self.temas_oscuros))
        )
        self.temas_disponibles = (
            self.temas_claros + self.temas_oscuros + self.temas_otros
        )
        if TEMA_INICIAL not in self.temas_disponibles:
            tema_respaldo = next(
                iter(self.temas_oscuros or self.temas_claros or self.temas_otros)
            )
            self.tema_var.set(tema_respaldo)
            self.root.theme_use(tema_respaldo)

        self._construir_menu()
        self._construir_interfaz()
        self._configurar_atajos()
        self._cambiar_modo(marcar=False)
        self._cargando = False
        self.modificado = False
        self._actualizar_titulo()
        self.root.protocol("WM_DELETE_WINDOW", self._cerrar)

    # -------------------------------------------------------------------------
    # Construye los menús Archivo, Apariencia y Ayuda de la ventana principal.
    # -------------------------------------------------------------------------
    def _construir_menu(self) -> None:
        barra = tk.Menu(self.root)

        archivo = tk.Menu(barra, tearoff=False)
        archivo.add_command(
            label="Abrir…", accelerator="Ctrl+O", command=self._abrir_configuracion
        )
        archivo.add_command(
            label="Guardar", accelerator="Ctrl+S", command=self._guardar_configuracion
        )
        archivo.add_command(
            label="Guardar como…",
            accelerator="Ctrl+Mayús+S",
            command=self._guardar_configuracion_como,
        )
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self._cerrar)
        barra.add_cascade(label="Archivo", menu=archivo)

        apariencia = tk.Menu(barra, tearoff=False)
        if self.temas_claros:
            claros = tk.Menu(apariencia, tearoff=False)
            self._agregar_temas_al_menu(claros, self.temas_claros)
            apariencia.add_cascade(label="Temas claros", menu=claros)
        if self.temas_oscuros:
            oscuros = tk.Menu(apariencia, tearoff=False)
            self._agregar_temas_al_menu(oscuros, self.temas_oscuros)
            apariencia.add_cascade(label="Temas oscuros", menu=oscuros)
        if self.temas_otros:
            otros = tk.Menu(apariencia, tearoff=False)
            self._agregar_temas_al_menu(otros, self.temas_otros, mostrar_variante=True)
            apariencia.add_cascade(label="Otros temas", menu=otros)
        barra.add_cascade(label="Apariencia", menu=apariencia)

        ayuda = tk.Menu(barra, tearoff=False)
        ayuda.add_command(
            label="Manual de uso",
            accelerator="F1",
            command=lambda: mostrar_ayuda(self.root),
        )
        ayuda.add_separator()
        ayuda.add_command(
            label="Acerca de…", command=lambda: mostrar_acerca_de(self.root)
        )
        barra.add_cascade(label="Ayuda", menu=ayuda)
        self.root.configure(menu=barra)

    # -------------------------------------------------------------------------
    # Añade al menú los temas disponibles y los vincula con la variable de selección.
    # -------------------------------------------------------------------------
    def _agregar_temas_al_menu(
        self,
        menu: tk.Menu,
        temas: tuple[str, ...],
        mostrar_variante: bool = False,
    ) -> None:
        for tema in temas:
            base = (
                tema
                if mostrar_variante
                else tema.removesuffix("-light").removesuffix("-dark")
            )
            etiqueta = base.replace("-", " ").title()
            menu.add_radiobutton(
                label=etiqueta,
                value=tema,
                variable=self.tema_var,
                command=self._tema_cambiado,
            )

    # -------------------------------------------------------------------------
    # Organiza el panel lateral de controles y el lienzo interactivo central.
    # -------------------------------------------------------------------------
    def _construir_interfaz(self) -> None:
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        lateral = ttk.Frame(self.root, padding=14)
        lateral.grid(row=0, column=0, sticky=NSEW)
        lateral.columnconfigure(0, weight=1)

        ttk.Label(
            lateral,
            text="ML VISUALIZER",
            font=("TkDefaultFont", 18, "bold"),
            bootstyle="info",
        ).grid(row=0, column=0, sticky="w", pady=(0, 14))

        ttk.Label(lateral, text="Tipo de problema").grid(row=1, column=0, sticky="w")
        self.combo_modo = ttk.Combobox(
            lateral,
            textvariable=self.modo_var,
            values=MODOS,
            state="readonly",
            width=27,
        )
        self.combo_modo.grid(row=2, column=0, sticky=EW, pady=(3, 10))
        self.combo_modo.bind("<<ComboboxSelected>>", lambda _e: self._cambiar_modo())

        ttk.Label(lateral, text="Dataset sintético").grid(row=3, column=0, sticky="w")
        self.combo_dataset = ttk.Combobox(
            lateral, textvariable=self.dataset_var, state="readonly"
        )
        self.combo_dataset.grid(row=4, column=0, sticky=EW, pady=(3, 10))
        self.combo_dataset.bind(
            "<<ComboboxSelected>>", lambda _e: self._generar_y_entrenar()
        )

        muestras = ttk.Frame(lateral)
        muestras.grid(row=5, column=0, sticky=EW, pady=(0, 10))
        muestras.columnconfigure(1, weight=1)
        ttk.Label(muestras, text="Número de muestras").grid(
            row=0, column=0, sticky="w", padx=(0, 10)
        )
        self.spin_muestras = ttk.Spinbox(
            muestras,
            from_=20,
            to=2000,
            increment=10,
            textvariable=self.n_muestras_var,
            width=9,
            command=self._numero_muestras_cambiado,
        )
        self.spin_muestras.grid(row=0, column=1, sticky="e")
        self.spin_muestras.bind("<Return>", lambda _e: self._numero_muestras_cambiado())
        self.spin_muestras.bind(
            "<FocusOut>", lambda _e: self._numero_muestras_cambiado()
        )

        ttk.Label(lateral, text="Modelo").grid(row=6, column=0, sticky="w")
        self.combo_modelo = ttk.Combobox(
            lateral, textvariable=self.modelo_var, state="readonly"
        )
        self.combo_modelo.grid(row=7, column=0, sticky=EW, pady=(3, 10))
        self.combo_modelo.bind(
            "<<ComboboxSelected>>", lambda _e: self._cambiar_modelo()
        )

        self.frame_parametros = ttk.Labelframe(
            lateral, text="Parámetros del modelo", padding=10
        )
        self.frame_parametros.grid(row=8, column=0, sticky=EW, pady=(0, 10))
        self.frame_parametros.columnconfigure(1, weight=1)

        ttk.Label(lateral, text="Representación del mapa").grid(
            row=9, column=0, sticky="w"
        )
        self.combo_mapa = ttk.Combobox(
            lateral,
            textvariable=self.mapa_var,
            values=("Normal", "Probabilidad", "Incertidumbre"),
            state="readonly",
        )
        self.combo_mapa.grid(row=10, column=0, sticky=EW, pady=(3, 8))
        self.combo_mapa.bind("<<ComboboxSelected>>", lambda _e: self._mapa_cambiado())

        self.check_detalles = ttk.Checkbutton(
            lateral,
            text="Visualización didáctica (V)",
            variable=self.detalles_var,
            command=self._detalles_cambiados,
            bootstyle="round-toggle",
        )
        self.check_detalles.grid(row=11, column=0, sticky="w", pady=(2, 10))

        botones = ttk.Frame(lateral)
        botones.grid(row=12, column=0, sticky=EW)
        botones.columnconfigure((0, 1), weight=1)
        ttk.Button(
            botones,
            text="Nuevo dataset",
            command=self._generar_y_entrenar,
            bootstyle="primary",
        ).grid(row=0, column=0, sticky=EW, padx=(0, 4))
        self.boton_reentrenar = ttk.Button(
            botones,
            text="Reentrenar",
            command=self._entrenar,
            bootstyle="secondary",
        )
        self.boton_reentrenar.grid(row=0, column=1, sticky=EW, padx=(4, 0))

        metricas = ttk.Labelframe(lateral, text="Métricas", padding=10)
        metricas.grid(row=13, column=0, sticky=EW, pady=(12, 8))
        ttk.Label(
            metricas,
            textvariable=self.metricas_var,
            justify=LEFT,
            wraplength=265,
            font=("DejaVu Sans Mono", 10),
        ).pack(anchor="w")

        ttk.Label(
            lateral,
            textvariable=self.prediccion_var,
            wraplength=275,
            justify=LEFT,
            bootstyle="secondary",
        ).grid(row=14, column=0, sticky=EW, pady=(4, 8))
        lateral.rowconfigure(15, weight=1)
        ttk.Label(lateral, textvariable=self.estado_var, bootstyle="secondary").grid(
            row=16,
            column=0,
            sticky="sw",
            pady=(12, 0),
        )

        centro = ttk.Frame(self.root, padding=(0, 10, 10, 10))
        centro.grid(row=0, column=1, sticky=NSEW)
        centro.rowconfigure(0, weight=1)
        centro.columnconfigure(0, weight=1)
        self.lienzo = LienzoML(centro, self._agregar_punto, self._quitar_punto)
        self.lienzo.grid(row=0, column=0, sticky=NSEW)

    # -------------------------------------------------------------------------
    # Cambia la familia de problema y carga sus datasets y modelos compatibles.
    # -------------------------------------------------------------------------
    def _cambiar_modo(self, marcar: bool = True) -> None:
        modo = self.modo_var.get()
        datasets = DATASETS[modo]
        modelos = (SIN_MODELO,) + MODELOS[modo]
        self.combo_dataset.configure(values=datasets)
        self.combo_modelo.configure(values=modelos)
        self.dataset_var.set(datasets[0])
        self.modelo_var.set(SIN_MODELO)
        self.mapa_var.set("Normal")
        self._reconstruir_parametros()
        self._actualizar_estado_controles_modelo()
        self._generar_y_entrenar(marcar=marcar)

    # -------------------------------------------------------------------------
    # Selecciona y entrena otro modelo conservando exactamente el dataset visible.
    # -------------------------------------------------------------------------
    def _cambiar_modelo(self, marcar: bool = True) -> None:
        # Este flujo llama sólo a _entrenar: nunca vuelve a generar los puntos.
        self._reconstruir_parametros()
        self._actualizar_estado_controles_modelo()
        self._entrenar()
        if marcar:
            self._marcar_modificado()

    # -------------------------------------------------------------------------
    # Regenera únicamente los controles de hiperparámetros del modelo activo.
    # -------------------------------------------------------------------------
    def _reconstruir_parametros(self) -> None:
        for widget in self.frame_parametros.winfo_children():
            widget.destroy()
        self.variables_parametros.clear()
        modelo = self.modelo_var.get()
        if modelo == SIN_MODELO:
            ttk.Label(
                self.frame_parametros,
                text="Seleccione un modelo para configurar sus hiperparámetros.",
                wraplength=245,
                justify=LEFT,
            ).grid(row=0, column=0, columnspan=2, sticky="w")
            return
        definiciones = PARAMETROS_UI[modelo]
        if not definiciones:
            ttk.Label(self.frame_parametros, text="Sin hiperparámetros").grid(
                row=0,
                column=0,
                sticky="w",
            )
            return
        for fila, (clave, etiqueta, minimo, maximo, paso) in enumerate(definiciones):
            ttk.Label(self.frame_parametros, text=etiqueta).grid(
                row=fila,
                column=0,
                sticky="w",
                padx=(0, 8),
                pady=3,
            )
            valor = self.parametros[modelo][clave]
            variable: tk.Variable
            variable = (
                tk.IntVar(value=valor)
                if isinstance(valor, int)
                else tk.DoubleVar(value=valor)
            )
            control = ttk.Spinbox(
                self.frame_parametros,
                from_=minimo,
                to=maximo,
                increment=paso,
                textvariable=variable,
                width=9,
                command=self._parametro_cambiado,
            )
            control.grid(row=fila, column=1, sticky="e", pady=3)
            control.bind("<Return>", lambda _e: self._parametro_cambiado())
            control.bind("<FocusOut>", lambda _e: self._parametro_cambiado())
            self.variables_parametros[clave] = variable

    # -------------------------------------------------------------------------
    # Habilita o bloquea los controles que dependen de tener un modelo seleccionado.
    # -------------------------------------------------------------------------
    def _actualizar_estado_controles_modelo(self) -> None:
        """Activa sólo los controles que tienen sentido con un modelo entrenado."""

        sin_modelo = self.modelo_var.get() == SIN_MODELO
        self.boton_reentrenar.configure(state=DISABLED if sin_modelo else "normal")
        self.check_detalles.configure(state=DISABLED if sin_modelo else "normal")
        if sin_modelo or self.modo_var.get() != "Clasificación":
            self.mapa_var.set("Normal")
            self.combo_mapa.configure(state=DISABLED)
        else:
            self.combo_mapa.configure(state="readonly")

    # -------------------------------------------------------------------------
    # Lee los hiperparámetros visibles y reentrena sin modificar las observaciones.
    # -------------------------------------------------------------------------
    def _parametro_cambiado(self) -> None:
        modelo = self.modelo_var.get()
        try:
            for clave, variable in self.variables_parametros.items():
                self.parametros[modelo][clave] = variable.get()
        except tk.TclError:
            return
        self._entrenar()
        self._marcar_modificado()

    # -------------------------------------------------------------------------
    # Valida la cantidad de muestras y regenera datos sólo si el valor cambió.
    # -------------------------------------------------------------------------
    def _numero_muestras_cambiado(self) -> None:
        try:
            cantidad = int(self.n_muestras_var.get())
        except (tk.TclError, ValueError):
            return
        cantidad = max(20, min(2000, cantidad))
        self.n_muestras_var.set(cantidad)
        # FocusOut también dispara este método; esta guarda evita cambios accidentales.
        if cantidad == self.n_muestras_aplicadas:
            return
        self._generar_y_entrenar()

    # -------------------------------------------------------------------------
    # Genera una realización sintética y, si corresponde, entrena el modelo activo.
    # -------------------------------------------------------------------------
    def _generar_y_entrenar(self, seed: int | None = None, marcar: bool = True) -> None:
        try:
            self.seed_actual = (
                seed if seed is not None else int(self.rng.integers(0, 2**31 - 1))
            )
            cantidad = int(self.n_muestras_var.get())
            self.X, self.y = generar_dataset(
                self.modo_var.get(),
                self.dataset_var.get(),
                n_muestras=cantidad,
                seed=self.seed_actual,
            )
            self.n_muestras_aplicadas = cantidad
            self._entrenar()
            if marcar:
                self._marcar_modificado()
        except Exception as exc:  # noqa: BLE001 - frontera de errores de la GUI
            self._mostrar_error(exc)

    # -------------------------------------------------------------------------
    # Ajusta el modelo actual o prepara el lienzo para mostrar solamente los datos.
    # -------------------------------------------------------------------------
    def _entrenar(self) -> None:
        if len(self.X) < 4:
            return
        try:
            if self.modelo_var.get() == SIN_MODELO:
                self.resultado = None
                self.mapa_clases = None
                self.mapa_prob = None
                self.limites = calcular_limites(self.modo_var.get(), self.X, self.y)
                self.metricas_var.set(
                    "Sin modelo seleccionado\n\nObserve los datos antes de elegir un algoritmo."
                )
                self._actualizar_lienzo()
                self.estado_var.set(f"{len(self.X)} muestras · sin modelo")
                return
            self.estado_var.set("Entrenando…")
            self.root.update_idletasks()
            modelo = self.modelo_var.get()
            self.resultado = entrenar_modelo(
                self.modo_var.get(),
                modelo,
                self.X,
                self.y,
                self.parametros[modelo],
            )
            self.limites = calcular_limites(self.modo_var.get(), self.X, self.y)
            if self.modo_var.get() == "Regresión":
                self.mapa_clases = None
                self.mapa_prob = None
            else:
                self.mapa_clases, self.mapa_prob, _xs, _ys = calcular_mapa(
                    self.resultado,
                    self.limites,
                    resolucion=190,
                )
            self._actualizar_metricas()
            self._actualizar_lienzo()
            self.estado_var.set(f"{len(self.X)} muestras · modelo actualizado")
        except Exception as exc:  # noqa: BLE001 - frontera de errores de la GUI
            self._mostrar_error(exc)

    # -------------------------------------------------------------------------
    # Formatea métricas y datos propios del estimador para el panel lateral.
    # -------------------------------------------------------------------------
    def _actualizar_metricas(self) -> None:
        if self.resultado is None:
            return
        lineas = []
        for nombre, valor in self.resultado.metricas.items():
            formato = f"{valor:8.2f}" if nombre == "Inercia" else f"{valor:8.3f}"
            lineas.append(f"{nombre:<23} {formato}")
        if self.resultado.nombre_modelo == "Random Forest":
            imp = self.resultado.modelo.feature_importances_
            lineas.extend(
                ("", f"Importancia X₁: {imp[0]:.3f}", f"Importancia X₂: {imp[1]:.3f}")
            )
        elif self.resultado.nombre_modelo == "Regresión lineal":
            pendiente = float(self.resultado.modelo.coef_[0])
            intercepto = float(self.resultado.modelo.intercept_)
            lineas.extend(("", f"ŷ = {intercepto:.3f} + {pendiente:.3f}x"))
        elif self.resultado.nombre_modelo == "Regresión polinómica":
            grado = int(self.parametros["Regresión polinómica"]["grado"])
            lineas.extend(("", f"Grado del polinomio: {grado}"))
        elif self.resultado.nombre_modelo == "KNN regresión":
            vecinos = int(self.resultado.modelo.n_neighbors)
            lineas.extend(("", f"Vecinos utilizados: {vecinos}"))
        elif self.resultado.nombre_modelo == "Árbol de regresión":
            arbol = self.resultado.modelo
            lineas.extend(
                (
                    "",
                    f"Profundidad obtenida: {arbol.get_depth()}",
                    f"Hojas: {arbol.get_n_leaves()}",
                )
            )
        self.metricas_var.set("\n".join(lineas))

    # -------------------------------------------------------------------------
    # Envía al Canvas el estado entrenado o los datos crudos, según corresponda.
    # -------------------------------------------------------------------------
    def _actualizar_lienzo(self) -> None:
        if self.resultado is None:
            if len(self.X):
                self.lienzo.establecer_solo_datos(
                    self.modo_var.get(),
                    self.X,
                    self.y,
                    self.limites,
                )
            return
        self.lienzo.establecer_datos(
            self.resultado,
            self.limites,
            self.mapa_clases,
            self.mapa_prob,
            self.mapa_var.get(),
            self.detalles_var.get(),
        )

    # -------------------------------------------------------------------------
    # Cambia la representación del fondo sin volver a entrenar el estimador.
    # -------------------------------------------------------------------------
    def _mapa_cambiado(self) -> None:
        if self.modelo_var.get() == SIN_MODELO:
            return
        self._actualizar_lienzo()
        self._marcar_modificado()

    # -------------------------------------------------------------------------
    # Muestra u oculta la capa didáctica y actualiza sólo la visualización.
    # -------------------------------------------------------------------------
    def _detalles_cambiados(self) -> None:
        if self.modelo_var.get() == SIN_MODELO:
            return
        self._actualizar_lienzo()
        self._marcar_modificado()

    # -------------------------------------------------------------------------
    # Aplica un tema de ttkbootstrap sin modificar la paleta interna del gráfico.
    # -------------------------------------------------------------------------
    def _tema_cambiado(self) -> None:
        tema = self.tema_var.get()
        if tema not in self.temas_disponibles:
            return
        self.root.theme_use(tema)
        self._marcar_modificado()

    # -------------------------------------------------------------------------
    # Incorpora al dataset el punto creado con el mouse y recalcula el resultado.
    # -------------------------------------------------------------------------
    def _agregar_punto(self, x: float, y_plot: float, clase: int) -> None:
        modo = self.modo_var.get()
        if modo == "Regresión":
            self.X = np.vstack((self.X, [[x]]))
            assert self.y is not None
            self.y = np.append(self.y, y_plot)
        else:
            self.X = np.vstack((self.X, [[x, y_plot]]))
            if modo == "Clasificación":
                assert self.y is not None
                self.y = np.append(self.y, clase)
        self._entrenar()

    # -------------------------------------------------------------------------
    # Elimina la observación más cercana al clic usando distancias normalizadas.
    # -------------------------------------------------------------------------
    def _quitar_punto(self, x: float, y_plot: float) -> None:
        if len(self.X) <= 6:
            return
        if self.modo_var.get() == "Regresión":
            assert self.y is not None
            escala_x = max(np.ptp(self.X[:, 0]), 1e-9)
            escala_y = max(np.ptp(self.y), 1e-9)
            dist = ((self.X[:, 0] - x) / escala_x) ** 2 + (
                (self.y - y_plot) / escala_y
            ) ** 2
        else:
            escala = np.maximum(np.ptp(self.X, axis=0), 1e-9)
            dist = np.sum(((self.X - [x, y_plot]) / escala) ** 2, axis=1)
        idx = int(np.argmin(dist))
        self.X = np.delete(self.X, idx, axis=0)
        if self.y is not None:
            self.y = np.delete(self.y, idx)
        self._entrenar()

    # -------------------------------------------------------------------------
    # Reúne en un diccionario serializable todas las opciones de la sesión actual.
    # -------------------------------------------------------------------------
    def _crear_configuracion(self) -> dict:
        return {
            "aplicacion": NOMBRE_APP,
            "version": VERSION_APP,
            "tema": self.tema_var.get(),
            "tipo_problema": self.modo_var.get(),
            "dataset": self.dataset_var.get(),
            "numero_muestras": int(self.n_muestras_var.get()),
            "modelo": self.modelo_var.get(),
            "parametros": self.parametros,
            "representacion_mapa": self.mapa_var.get(),
            "visualizacion_didactica": bool(self.detalles_var.get()),
            "seed_dataset": int(self.seed_actual),
        }

    # -------------------------------------------------------------------------
    # Valida una configuración externa, migra temas antiguos y limita sus valores.
    # -------------------------------------------------------------------------
    def _normalizar_configuracion(self, datos: dict) -> dict:
        modo = datos.get("tipo_problema")
        if modo not in MODOS:
            raise ValueError("El tipo de problema guardado no es válido.")
        dataset = datos.get("dataset")
        if dataset not in DATASETS[modo]:
            raise ValueError("El dataset guardado no corresponde al tipo de problema.")
        modelo = datos.get("modelo")
        if modelo != SIN_MODELO and modelo not in MODELOS[modo]:
            raise ValueError("El modelo guardado no corresponde al tipo de problema.")

        try:
            cantidad = int(datos.get("numero_muestras", 120))
            seed = int(datos.get("seed_dataset", 42))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "La cantidad de muestras o la semilla no son válidas."
            ) from exc
        if not 20 <= cantidad <= 2000:
            raise ValueError("El número de muestras debe estar entre 20 y 2000.")

        tema = datos.get("tema", self.tema_var.get())
        tema = MIGRACION_TEMAS.get(tema, tema)
        if tema not in self.temas_disponibles:
            raise ValueError(
                f"El tema '{tema}' no está disponible en esta instalación."
            )
        mapa = datos.get("representacion_mapa", "Normal")
        if mapa not in ("Normal", "Probabilidad", "Incertidumbre"):
            raise ValueError("La representación del mapa no es válida.")
        if modo != "Clasificación" or modelo == SIN_MODELO:
            mapa = "Normal"

        parametros = {
            nombre: valores.copy() for nombre, valores in PARAMETROS_INICIALES.items()
        }
        recibidos = datos.get("parametros", {})
        if isinstance(recibidos, dict):
            for nombre, definiciones in PARAMETROS_UI.items():
                valores = recibidos.get(nombre, {})
                if not isinstance(valores, dict):
                    continue
                for clave, _etiqueta, minimo, maximo, _paso in definiciones:
                    if clave not in valores:
                        continue
                    tipo = type(PARAMETROS_INICIALES[nombre][clave])
                    try:
                        valor = tipo(valores[clave])
                    except (TypeError, ValueError):
                        continue
                    parametros[nombre][clave] = max(minimo, min(maximo, valor))

        return {
            "tema": tema,
            "modo": modo,
            "dataset": dataset,
            "cantidad": cantidad,
            "modelo": modelo,
            "parametros": parametros,
            "mapa": mapa,
            "detalles": bool(datos.get("visualizacion_didactica", True)),
            "seed": seed,
        }

    # -------------------------------------------------------------------------
    # Solicita un JSON, lo valida y restaura de manera coordinada toda la interfaz.
    # -------------------------------------------------------------------------
    def _abrir_configuracion(self) -> None:
        if not self._confirmar_descartar_cambios():
            return
        ruta = filedialog.askopenfilename(
            parent=self.root,
            title="Abrir configuración",
            filetypes=(("Configuración JSON", "*.json"), ("Todos los archivos", "*.*")),
        )
        if not ruta:
            return
        try:
            config = self._normalizar_configuracion(cargar_json(ruta))
            self._cargando = True
            self.parametros = config["parametros"]
            self.tema_var.set(config["tema"])
            self.root.theme_use(config["tema"])
            self.modo_var.set(config["modo"])
            self.combo_dataset.configure(values=DATASETS[config["modo"]])
            self.combo_modelo.configure(values=(SIN_MODELO,) + MODELOS[config["modo"]])
            self.dataset_var.set(config["dataset"])
            self.n_muestras_var.set(config["cantidad"])
            self.modelo_var.set(config["modelo"])
            self.mapa_var.set(config["mapa"])
            self.detalles_var.set(config["detalles"])
            self._reconstruir_parametros()
            self._actualizar_estado_controles_modelo()
            self._generar_y_entrenar(seed=config["seed"], marcar=False)
            self.ruta_configuracion = Path(ruta)
            self.modificado = False
            self._actualizar_titulo()
            self.estado_var.set(
                f"Configuración abierta: {self.ruta_configuracion.name}"
            )
        except Exception as exc:  # noqa: BLE001 - muestra errores de archivos al usuario
            self._mostrar_error(exc)
        finally:
            self._cargando = False

    # -------------------------------------------------------------------------
    # Guarda sobre la ruta actual o deriva a Guardar como si aún no existe una.
    # -------------------------------------------------------------------------
    def _guardar_configuracion(self) -> bool:
        if self.ruta_configuracion is None:
            return self._guardar_configuracion_como()
        try:
            guardar_json(self.ruta_configuracion, self._crear_configuracion())
            self.modificado = False
            self._actualizar_titulo()
            self.estado_var.set(
                f"Configuración guardada: {self.ruta_configuracion.name}"
            )
            return True
        except Exception as exc:  # noqa: BLE001 - muestra errores de archivos al usuario
            self._mostrar_error(exc)
            return False

    # -------------------------------------------------------------------------
    # Permite elegir una ruta JSON nueva y confirma antes de reemplazar un archivo.
    # -------------------------------------------------------------------------
    def _guardar_configuracion_como(self) -> bool:
        ruta = filedialog.asksaveasfilename(
            parent=self.root,
            title="Guardar configuración como",
            defaultextension=".json",
            initialfile=(
                self.ruta_configuracion.name
                if self.ruta_configuracion
                else "configuracion_mlviz.json"
            ),
            filetypes=(("Configuración JSON", "*.json"), ("Todos los archivos", "*.*")),
        )
        if not ruta:
            return False
        destino = Path(ruta)
        if destino.exists() and destino != self.ruta_configuracion:
            reemplazar = messagebox.askyesno(
                "Confirmar reemplazo",
                f"El archivo '{destino.name}' ya existe. ¿Desea reemplazarlo?",
                parent=self.root,
            )
            if not reemplazar:
                return False
        self.ruta_configuracion = destino
        return self._guardar_configuracion()

    # -------------------------------------------------------------------------
    # Protege cambios de configuración pendientes antes de abrir o cerrar.
    # -------------------------------------------------------------------------
    def _confirmar_descartar_cambios(self) -> bool:
        if not self.modificado:
            return True
        respuesta = messagebox.askyesnocancel(
            "Configuración modificada",
            "La configuración tiene cambios sin guardar. ¿Desea guardarlos?",
            parent=self.root,
        )
        if respuesta is None:
            return False
        if respuesta:
            return self._guardar_configuracion()
        return True

    # -------------------------------------------------------------------------
    # Registra que la configuración cambió y actualiza la marca visual del título.
    # -------------------------------------------------------------------------
    def _marcar_modificado(self) -> None:
        if self._cargando:
            return
        self.modificado = True
        self._actualizar_titulo()

    # -------------------------------------------------------------------------
    # Refleja en la barra de título el archivo actual y los cambios sin guardar.
    # -------------------------------------------------------------------------
    def _actualizar_titulo(self) -> None:
        archivo = (
            self.ruta_configuracion.name if self.ruta_configuracion else "Sin guardar"
        )
        marca = " *" if self.modificado else ""
        self.root.title(f"{NOMBRE_APP} {VERSION_APP} · {archivo}{marca}")

    # -------------------------------------------------------------------------
    # Vincula los atajos de teclado con las mismas acciones disponibles en la GUI.
    # -------------------------------------------------------------------------
    def _configurar_atajos(self) -> None:
        self.root.bind("<Control-o>", lambda _e: self._abrir_configuracion())
        self.root.bind("<Control-s>", lambda _e: self._guardar_configuracion())
        self.root.bind(
            "<Control-Shift-S>", lambda _e: self._guardar_configuracion_como()
        )
        self.root.bind("<F1>", lambda _e: mostrar_ayuda(self.root))
        self.root.bind("<KeyPress-v>", lambda _e: self._alternar_detalles())
        self.root.bind("<KeyPress-r>", lambda _e: self._generar_y_entrenar())
        self.root.bind("<KeyPress-b>", lambda _e: self._alternar_mapa())

    # -------------------------------------------------------------------------
    # Invierte mediante el atajo V el estado de la visualización didáctica.
    # -------------------------------------------------------------------------
    def _alternar_detalles(self) -> None:
        if self.modelo_var.get() == SIN_MODELO:
            return
        self.detalles_var.set(not self.detalles_var.get())
        self._detalles_cambiados()

    # -------------------------------------------------------------------------
    # Recorre con el atajo B los mapas disponibles para clasificación.
    # -------------------------------------------------------------------------
    def _alternar_mapa(self) -> None:
        if (
            self.modo_var.get() != "Clasificación"
            or self.modelo_var.get() == SIN_MODELO
        ):
            return
        mapas = ("Normal", "Probabilidad", "Incertidumbre")
        actual = mapas.index(self.mapa_var.get())
        self.mapa_var.set(mapas[(actual + 1) % len(mapas)])
        self._mapa_cambiado()

    # -------------------------------------------------------------------------
    # Cierra la aplicación después de gestionar posibles cambios sin guardar.
    # -------------------------------------------------------------------------
    def _cerrar(self) -> None:
        if self._confirmar_descartar_cambios():
            self.root.destroy()

    # -------------------------------------------------------------------------
    # Presenta de forma uniforme los errores capturados en los límites de la GUI.
    # -------------------------------------------------------------------------
    def _mostrar_error(self, exc: Exception) -> None:
        self.estado_var.set("No se pudo completar la operación")
        messagebox.showerror(NOMBRE_APP, str(exc), parent=self.root)

    # -------------------------------------------------------------------------
    # Inicia el bucle de eventos de Tk y mantiene activa la aplicación.
    # -------------------------------------------------------------------------
    def ejecutar(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    AplicacionML().ejecutar()
