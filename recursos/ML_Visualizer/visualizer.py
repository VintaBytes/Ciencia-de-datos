"""Canvas interactivo y rasterizado eficiente de los mapas del modelo."""

from __future__ import annotations

import tkinter as tk
from collections.abc import Callable

import numpy as np
from ml_utils import ResultadoEntrenamiento
from PIL import Image, ImageTk

AZUL = (64, 145, 255)
ROJO = (255, 92, 92)
FONDO = (26, 29, 38)
PLOT = (235, 238, 244)
CLUSTERS = (
    (64, 112, 190),
    (196, 72, 72),
    (55, 160, 95),
    (190, 157, 55),
    (155, 75, 175),
    (55, 165, 170),
)


class LienzoML(tk.Canvas):
    """Canvas con fondo rasterizado y capas vectoriales para la interacción."""

    MARGEN_IZQ = 54
    MARGEN_DER = 18
    MARGEN_SUP = 20
    MARGEN_INF = 42

    # -------------------------------------------------------------------------
    # Inicializa el Canvas, su estado gráfico y los eventos de mouse y redimensión.
    # -------------------------------------------------------------------------
    def __init__(
        self,
        master,
        al_agregar: Callable[[float, float, int], None],
        al_quitar: Callable[[float, float], None],
        **kwargs,
    ):
        super().__init__(master, background="#1a1d26", highlightthickness=0, **kwargs)
        self.al_agregar = al_agregar
        self.al_quitar = al_quitar
        self.resultado: ResultadoEntrenamiento | None = None
        self.modo_sin_modelo: str | None = None
        self.X_sin_modelo: np.ndarray | None = None
        self.y_sin_modelo: np.ndarray | None = None
        self.limites = (-5.0, 5.0, -5.0, 5.0)
        self.mapa_clases: np.ndarray | None = None
        self.mapa_prob: np.ndarray | None = None
        self.modo_mapa = "Normal"
        self.ver_detalles = True
        self._imagen_tk: ImageTk.PhotoImage | None = None
        self._redibujo_pendiente: str | None = None
        self._ultimo_mouse: tuple[int, int] | None = None

        self.bind("<Configure>", self._programar_redibujo)
        self.bind("<Motion>", self._mover_mouse)
        self.bind("<Leave>", lambda _e: self.delete("hover"))
        self.bind("<Button-1>", self._click_izquierdo)
        self.bind("<Button-3>", self._click_derecho)

    # -------------------------------------------------------------------------
    # Recibe un resultado entrenado y actualiza todas las capas de visualización.
    # -------------------------------------------------------------------------
    def establecer_datos(
        self,
        resultado: ResultadoEntrenamiento,
        limites: tuple[float, float, float, float],
        mapa_clases: np.ndarray | None,
        mapa_prob: np.ndarray | None,
        modo_mapa: str,
        ver_detalles: bool,
    ) -> None:
        self.resultado = resultado
        self.modo_sin_modelo = None
        self.X_sin_modelo = None
        self.y_sin_modelo = None
        self.limites = limites
        self.mapa_clases = mapa_clases
        self.mapa_prob = mapa_prob
        self.modo_mapa = modo_mapa
        self.ver_detalles = ver_detalles
        self.redibujar()

    # -------------------------------------------------------------------------
    # Presenta observaciones sin modelo, predicciones ni agrupamientos sugeridos.
    # -------------------------------------------------------------------------
    def establecer_solo_datos(
        self,
        modo: str,
        X: np.ndarray,
        y: np.ndarray | None,
        limites: tuple[float, float, float, float],
    ) -> None:
        """Muestra el dataset sin entrenar ni consultar ningún estimador."""

        self.resultado = None
        self.modo_sin_modelo = modo
        self.X_sin_modelo = X
        self.y_sin_modelo = y
        self.limites = limites
        self.mapa_clases = None
        self.mapa_prob = None
        self.modo_mapa = "Normal"
        self.redibujar()

    # -------------------------------------------------------------------------
    # Obtiene el rectángulo útil del gráfico descontando márgenes y rótulos.
    # -------------------------------------------------------------------------
    def _area_plot(self) -> tuple[int, int, int, int]:
        ancho = max(100, self.winfo_width())
        alto = max(100, self.winfo_height())
        return (
            self.MARGEN_IZQ,
            self.MARGEN_SUP,
            max(self.MARGEN_IZQ + 1, ancho - self.MARGEN_DER),
            max(self.MARGEN_SUP + 1, alto - self.MARGEN_INF),
        )

    # -------------------------------------------------------------------------
    # Convierte coordenadas de los datos en coordenadas de píxeles del Canvas.
    # -------------------------------------------------------------------------
    def mundo_a_pantalla(self, x: float, y: float) -> tuple[float, float]:
        x0, y0, x1, y1 = self._area_plot()
        xmin, xmax, ymin, ymax = self.limites
        px = x0 + (x - xmin) / (xmax - xmin) * (x1 - x0)
        py = y1 - (y - ymin) / (ymax - ymin) * (y1 - y0)
        return px, py

    # -------------------------------------------------------------------------
    # Convierte una posición del Canvas en coordenadas del espacio de datos.
    # -------------------------------------------------------------------------
    def pantalla_a_mundo(self, px: float, py: float) -> tuple[float, float]:
        x0, y0, x1, y1 = self._area_plot()
        xmin, xmax, ymin, ymax = self.limites
        x = xmin + (px - x0) / (x1 - x0) * (xmax - xmin)
        y = ymin + (y1 - py) / (y1 - y0) * (ymax - ymin)
        return x, y

    # -------------------------------------------------------------------------
    # Comprueba si una posición del mouse pertenece al área útil del gráfico.
    # -------------------------------------------------------------------------
    def _dentro_plot(self, px: float, py: float) -> bool:
        x0, y0, x1, y1 = self._area_plot()
        return x0 <= px <= x1 and y0 <= py <= y1

    # -------------------------------------------------------------------------
    # Agrupa eventos de redimensión para evitar redibujos costosos consecutivos.
    # -------------------------------------------------------------------------
    def _programar_redibujo(self, _event=None) -> None:
        if self._redibujo_pendiente:
            self.after_cancel(self._redibujo_pendiente)
        self._redibujo_pendiente = self.after(70, self.redibujar)

    # -------------------------------------------------------------------------
    # Reconstruye el fondo, los ejes y las capas correspondientes al modo actual.
    # -------------------------------------------------------------------------
    def redibujar(self) -> None:
        self._redibujo_pendiente = None
        self.delete("all")
        if self.resultado is None and self.modo_sin_modelo is None:
            return
        self._dibujar_fondo()
        self._dibujar_ejes()
        if self.resultado is None:
            self._dibujar_puntos_sin_modelo()
            return
        if self.resultado.modo == "Regresión":
            self._dibujar_regresion()
        else:
            self._dibujar_puntos_2d()
            if self.resultado.modo == "Clasificación":
                self._dibujar_frontera_lineal()
            elif self.ver_detalles:
                self._dibujar_centroides()

    # -------------------------------------------------------------------------
    # Dibuja los datos crudos con una codificación adecuada para cada problema.
    # -------------------------------------------------------------------------
    def _dibujar_puntos_sin_modelo(self) -> None:
        """Dibuja observaciones crudas sin sugerir clusters ni predicciones."""

        assert self.modo_sin_modelo is not None and self.X_sin_modelo is not None
        if self.modo_sin_modelo == "Regresión":
            assert self.y_sin_modelo is not None
            coordenadas = zip(self.X_sin_modelo[:, 0], self.y_sin_modelo)
            etiquetas = np.zeros(len(self.X_sin_modelo), dtype=int)
        else:
            coordenadas = self.X_sin_modelo
            etiquetas = self.y_sin_modelo

        for i, (x_val, y_val) in enumerate(coordenadas):
            px, py = self.mundo_a_pantalla(float(x_val), float(y_val))
            if self.modo_sin_modelo == "Clasificación" and etiquetas is not None:
                color = AZUL if int(etiquetas[i]) == 0 else ROJO
            elif self.modo_sin_modelo == "Regresión":
                color = AZUL
            else:
                color = (118, 132, 151)
            self.create_oval(
                px - 5,
                py - 5,
                px + 5,
                py + 5,
                fill=self._hex(color),
                outline="#f4f6fa",
                width=1,
                tags="datos",
            )

    # -------------------------------------------------------------------------
    # Rasteriza el mapa normal, de probabilidad o de incertidumbre como una imagen.
    # -------------------------------------------------------------------------
    def _dibujar_fondo(self) -> None:
        x0, y0, x1, y1 = self._area_plot()
        ancho, alto = max(1, x1 - x0), max(1, y1 - y0)
        if (
            self.resultado is None
            or self.resultado.modo == "Regresión"
            or self.mapa_clases is None
        ):
            rgb = np.full((4, 4, 3), PLOT, dtype=np.uint8)
        elif self.resultado.modo == "Agrupamiento":
            rgb = np.empty((*self.mapa_clases.shape, 3), dtype=np.uint8)
            for clase in np.unique(self.mapa_clases):
                base = np.array(CLUSTERS[int(clase) % len(CLUSTERS)])
                rgb[self.mapa_clases == clase] = (base * 0.62).astype(np.uint8)
        elif self.modo_mapa == "Probabilidad" and self.mapa_prob is not None:
            p = self.mapa_prob
            rgb = np.stack(
                (45 + 175 * p, np.full_like(p, 45), 45 + 175 * (1 - p)), axis=2
            )
            rgb = rgb.astype(np.uint8)
        elif self.modo_mapa == "Incertidumbre" and self.mapa_prob is not None:
            incertidumbre = 1 - np.abs(self.mapa_prob - 0.5) * 2
            valor = (65 + 180 * incertidumbre).astype(np.uint8)
            rgb = np.stack((valor, valor, valor), axis=2)
        else:
            rgb = np.empty((*self.mapa_clases.shape, 3), dtype=np.uint8)
            rgb[self.mapa_clases == 0] = (42, 68, 122)
            rgb[self.mapa_clases != 0] = (122, 45, 48)

        imagen = Image.fromarray(np.flipud(rgb), mode="RGB")
        imagen = imagen.resize((ancho, alto), Image.Resampling.BILINEAR)
        # La referencia debe conservarse: Tk elimina la imagen si Python la libera.
        self._imagen_tk = ImageTk.PhotoImage(imagen)
        self.create_image(x0, y0, image=self._imagen_tk, anchor="nw", tags="base")

    # -------------------------------------------------------------------------
    # Traza el marco, las marcas y los valores numéricos de ambos ejes.
    # -------------------------------------------------------------------------
    def _dibujar_ejes(self) -> None:
        x0, y0, x1, y1 = self._area_plot()
        self.create_rectangle(x0, y0, x1, y1, outline="#9ba4b5", width=1, tags="base")
        xmin, xmax, ymin, ymax = self.limites
        for i in range(6):
            f = i / 5
            px = x0 + f * (x1 - x0)
            py = y1 - f * (y1 - y0)
            xv = xmin + f * (xmax - xmin)
            yv = ymin + f * (ymax - ymin)
            self.create_line(px, y1, px, y1 + 5, fill="#b7bfcc", tags="base")
            self.create_text(
                px,
                y1 + 17,
                text=f"{xv:.1f}",
                fill="#cbd1dc",
                font=("TkDefaultFont", 8),
                tags="base",
            )
            self.create_line(x0 - 5, py, x0, py, fill="#b7bfcc", tags="base")
            self.create_text(
                x0 - 8,
                py,
                text=f"{yv:.1f}",
                fill="#cbd1dc",
                anchor="e",
                font=("TkDefaultFont", 8),
                tags="base",
            )

    # -------------------------------------------------------------------------
    # Dibuja puntos de clasificación o agrupamiento con sus colores correspondientes.
    # -------------------------------------------------------------------------
    def _dibujar_puntos_2d(self) -> None:
        assert self.resultado is not None
        X = self.resultado.X
        if self.resultado.modo == "Agrupamiento":
            etiquetas = self.resultado.modelo.labels_
        else:
            etiquetas = self.resultado.y
        for punto, etiqueta in zip(X, etiquetas):
            px, py = self.mundo_a_pantalla(punto[0], punto[1])
            color = (
                CLUSTERS[int(etiqueta) % len(CLUSTERS)]
                if self.resultado.modo == "Agrupamiento"
                else (AZUL if etiqueta == 0 else ROJO)
            )
            borde = "#f8f9fb" if self.resultado.modo == "Agrupamiento" else "#e9edf3"
            self.create_oval(
                px - 5,
                py - 5,
                px + 5,
                py + 5,
                fill=self._hex(color),
                outline=borde,
                width=1,
                tags="datos",
            )

    # -------------------------------------------------------------------------
    # Superpone la recta de decisión explícita de la regresión logística.
    # -------------------------------------------------------------------------
    def _dibujar_frontera_lineal(self) -> None:
        assert self.resultado is not None
        if self.resultado.nombre_modelo != "Regresión logística":
            return
        modelo = self.resultado.modelo
        w = modelo.coef_[0]
        if abs(w[1]) < 1e-12:
            return
        xmin, xmax, _ymin, _ymax = self.limites
        y_a = -(w[0] * xmin + modelo.intercept_[0]) / w[1]
        y_b = -(w[0] * xmax + modelo.intercept_[0]) / w[1]
        p_a = self.mundo_a_pantalla(xmin, y_a)
        p_b = self.mundo_a_pantalla(xmax, y_b)
        self.create_line(*p_a, *p_b, fill="#ffffff", width=3, tags="datos")

    # -------------------------------------------------------------------------
    # Señala los centroides calculados por K-Means y muestra sus identificadores.
    # -------------------------------------------------------------------------
    def _dibujar_centroides(self) -> None:
        assert self.resultado is not None
        for i, centro in enumerate(self.resultado.modelo.cluster_centers_):
            px, py = self.mundo_a_pantalla(centro[0], centro[1])
            self.create_oval(
                px - 10,
                py - 10,
                px + 10,
                py + 10,
                fill="#ffe066",
                outline="#161821",
                width=2,
                tags="datos",
            )
            self.create_text(
                px,
                py,
                text=str(i),
                fill="#161821",
                font=("TkDefaultFont", 9, "bold"),
                tags="datos",
            )

    # -------------------------------------------------------------------------
    # Dibuja observaciones, curva estimada y residuos opcionales de la regresión.
    # -------------------------------------------------------------------------
    def _dibujar_regresion(self) -> None:
        assert self.resultado is not None and self.resultado.y is not None
        X, y = self.resultado.X, self.resultado.y
        modelo = self.resultado.modelo
        xmin, xmax, ymin, ymax = self.limites
        if self.ver_detalles:
            pred = modelo.predict(X)
            for x_val, real, estimado in zip(X[:, 0], y, pred):
                p_real = self.mundo_a_pantalla(x_val, real)
                p_est = self.mundo_a_pantalla(
                    x_val, float(np.clip(estimado, ymin, ymax))
                )
                self.create_line(
                    *p_real, *p_est, fill="#f0b44d", width=1, dash=(3, 2), tags="datos"
                )
        for x_val, y_val in zip(X[:, 0], y):
            px, py = self.mundo_a_pantalla(x_val, y_val)
            self.create_oval(
                px - 5,
                py - 5,
                px + 5,
                py + 5,
                fill=self._hex(AZUL),
                outline="#f4f6fa",
                tags="datos",
            )
        x_curva = np.linspace(xmin, xmax, 700)
        y_curva = modelo.predict(x_curva.reshape(-1, 1))
        y_curva = np.clip(y_curva, ymin, ymax)
        coordenadas: list[float] = []
        for x_val, y_val in zip(x_curva, y_curva):
            px, py = self.mundo_a_pantalla(float(x_val), float(y_val))
            coordenadas.extend((px, py))
        self.create_line(
            *coordenadas,
            fill="#ff5c5c",
            width=4,
            smooth=False,
            tags="datos",
        )

    # -------------------------------------------------------------------------
    # Actualiza la predicción y los detalles locales al desplazar el cursor.
    # -------------------------------------------------------------------------
    def _mover_mouse(self, event) -> None:
        self.delete("hover")
        self._ultimo_mouse = (event.x, event.y)
        if not self._dentro_plot(event.x, event.y):
            return
        x, y = self.pantalla_a_mundo(event.x, event.y)
        if self.resultado is None:
            if self.modo_sin_modelo is not None:
                self.create_oval(
                    event.x - 5,
                    event.y - 5,
                    event.x + 5,
                    event.y + 5,
                    outline="#4b5563",
                    width=2,
                    tags="hover",
                )
                self._etiqueta_hover(event.x, event.y, f"x={x:.3f}  ·  y={y:.3f}")
            return
        if self.resultado.modo == "Regresión":
            punto_x = np.array([[x]])
            pred = float(self.resultado.modelo.predict(punto_x)[0])
            _xmin, _xmax, ymin, ymax = self.limites
            pred_visual = float(np.clip(pred, ymin, ymax))
            px_linea, py_linea = self.mundo_a_pantalla(x, pred_visual)
            self.create_line(
                event.x,
                event.y,
                px_linea,
                py_linea,
                fill="#4b5563",
                dash=(4, 3),
                tags="hover",
            )
            self.create_oval(
                px_linea - 6,
                py_linea - 6,
                px_linea + 6,
                py_linea + 6,
                outline="#374151",
                width=2,
                tags="hover",
            )
            texto = f"ŷ = {pred:.3f}"
            if self.ver_detalles and self.resultado.nombre_modelo == "KNN regresión":
                texto += self._dibujar_vecinos_knn_regresion(
                    punto_x, px_linea, py_linea
                )
            elif (
                self.ver_detalles
                and self.resultado.nombre_modelo == "Árbol de regresión"
            ):
                hoja = int(self.resultado.modelo.apply(punto_x)[0])
                muestras = int(self.resultado.modelo.tree_.n_node_samples[hoja])
                texto += f"  ·  hoja {hoja}, {muestras} muestras"
            elif (
                self.ver_detalles
                and self.resultado.nombre_modelo == "Regresión polinómica"
            ):
                grado = self.resultado.modelo.named_steps["polynomialfeatures"].degree
                texto += f"  ·  grado {grado}"
            self._etiqueta_hover(event.x, event.y, texto)
            return

        punto = np.array([[x, y]])
        pred = int(self.resultado.modelo.predict(punto)[0])
        color = (
            CLUSTERS[pred % len(CLUSTERS)]
            if self.resultado.modo == "Agrupamiento"
            else (AZUL if pred == 0 else ROJO)
        )
        self.create_oval(
            event.x - 8,
            event.y - 8,
            event.x + 8,
            event.y + 8,
            outline=self._hex(color),
            width=3,
            tags="hover",
        )
        texto = (
            f"Grupo {pred}"
            if self.resultado.modo == "Agrupamiento"
            else f"Clase {pred}"
        )

        if self.resultado.modo == "Clasificación":
            probs = self.resultado.modelo.predict_proba(punto)[0]
            texto += f"  ·  P(1)={probs[1]:.3f}"
            if self.ver_detalles and self.resultado.nombre_modelo == "KNN":
                texto += self._dibujar_vecinos_knn(punto, event.x, event.y)
            elif self.ver_detalles and self.resultado.nombre_modelo == "Random Forest":
                votos = np.array(
                    [
                        int(arbol.predict(punto)[0])
                        for arbol in self.resultado.modelo.estimators_
                    ]
                )
                v0, v1 = int(np.sum(votos == 0)), int(np.sum(votos == 1))
                texto += f"  ·  votos {v0}/{v1}"
            elif (
                self.ver_detalles
                and self.resultado.nombre_modelo == "Árbol de decisión"
            ):
                hoja = int(self.resultado.modelo.apply(punto)[0])
                muestras = int(self.resultado.modelo.tree_.n_node_samples[hoja])
                texto += f"  ·  hoja {hoja}, {muestras} muestras"
        elif self.ver_detalles and self.resultado.silhouette_muestras is not None:
            dist = np.linalg.norm(self.resultado.X - punto[0], axis=1)
            idx = int(np.argmin(dist))
            texto += (
                f"  ·  silhouette cercano={self.resultado.silhouette_muestras[idx]:.3f}"
            )

        self._etiqueta_hover(event.x, event.y, texto)

    # -------------------------------------------------------------------------
    # Destaca los vecinos usados por KNN clasificación y su radio de búsqueda.
    # -------------------------------------------------------------------------
    def _dibujar_vecinos_knn(self, punto: np.ndarray, px: float, py: float) -> str:
        assert self.resultado is not None
        distancias, indices = self.resultado.modelo.kneighbors(punto)
        for idx in indices[0]:
            vecino = self.resultado.X_train[idx]
            vx, vy = self.mundo_a_pantalla(vecino[0], vecino[1])
            self.create_line(px, py, vx, vy, fill="#ffffff", width=1, tags="hover")
            self.create_oval(
                vx - 9, vy - 9, vx + 9, vy + 9, outline="#ffffff", width=2, tags="hover"
            )
        xmin, xmax, _ymin, _ymax = self.limites
        x0, _y0, x1, _y1 = self._area_plot()
        # El vecino más lejano determina el radio visual de la consulta KNN.
        radio_px = distancias[0][-1] / (xmax - xmin) * (x1 - x0)
        self.create_oval(
            px - radio_px,
            py - radio_px,
            px + radio_px,
            py + radio_px,
            outline="#d9dde5",
            tags="hover",
        )
        return f"  ·  k={len(indices[0])}"

    # -------------------------------------------------------------------------
    # Destaca las observaciones cuyo promedio forma la predicción KNN de regresión.
    # -------------------------------------------------------------------------
    def _dibujar_vecinos_knn_regresion(
        self,
        punto: np.ndarray,
        px: float,
        py: float,
    ) -> str:
        """Destaca los puntos cuyo promedio produce la predicción KNN."""

        assert self.resultado is not None and self.resultado.y_train is not None
        _distancias, indices = self.resultado.modelo.kneighbors(punto)
        for idx in indices[0]:
            vecino_x = float(self.resultado.X_train[idx, 0])
            vecino_y = float(self.resultado.y_train[idx])
            vx, vy = self.mundo_a_pantalla(vecino_x, vecino_y)
            self.create_line(px, py, vx, vy, fill="#374151", width=1, tags="hover")
            self.create_oval(
                vx - 9,
                vy - 9,
                vx + 9,
                vy + 9,
                outline="#374151",
                width=2,
                tags="hover",
            )
        return f"  ·  promedio de {len(indices[0])} vecinos"

    # -------------------------------------------------------------------------
    # Coloca junto al cursor una etiqueta legible con la información calculada.
    # -------------------------------------------------------------------------
    def _etiqueta_hover(self, px: float, py: float, texto: str) -> None:
        x = px + 14
        y = py + 18
        item = self.create_text(
            x,
            y,
            text=texto,
            anchor="nw",
            fill="#ffffff",
            font=("TkDefaultFont", 10, "bold"),
            tags="hover",
        )
        caja = self.bbox(item)
        if caja:
            rect = self.create_rectangle(
                caja[0] - 5,
                caja[1] - 3,
                caja[2] + 5,
                caja[3] + 3,
                fill="#191c24",
                outline="#7e8797",
                tags="hover",
            )
            self.tag_lower(rect, item)

    # -------------------------------------------------------------------------
    # Traduce el clic izquierdo en la incorporación de una nueva observación.
    # -------------------------------------------------------------------------
    def _click_izquierdo(self, event) -> None:
        if (
            self.resultado is None and self.modo_sin_modelo is None
        ) or not self._dentro_plot(event.x, event.y):
            return
        x, y = self.pantalla_a_mundo(event.x, event.y)
        clase = 0
        self.al_agregar(x, y, clase)

    # -------------------------------------------------------------------------
    # Agrega clase 1 en clasificación o elimina el punto más cercano en otros modos.
    # -------------------------------------------------------------------------
    def _click_derecho(self, event) -> None:
        if (
            self.resultado is None and self.modo_sin_modelo is None
        ) or not self._dentro_plot(event.x, event.y):
            return
        x, y = self.pantalla_a_mundo(event.x, event.y)
        modo = (
            self.resultado.modo if self.resultado is not None else self.modo_sin_modelo
        )
        if modo == "Clasificación":
            self.al_agregar(x, y, 1)
        else:
            self.al_quitar(x, y)

    # -------------------------------------------------------------------------
    # Convierte una terna RGB entera en el color hexadecimal esperado por Tk.
    # -------------------------------------------------------------------------
    @staticmethod
    def _hex(color: tuple[int, int, int]) -> str:
        return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
