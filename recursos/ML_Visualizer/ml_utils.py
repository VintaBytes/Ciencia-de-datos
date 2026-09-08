"""Datos, modelos y métricas para ML Visualizer.

Este módulo no contiene código de interfaz. Puede importarse desde pruebas,
cuadernos o desde la aplicación de escritorio.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import (
    make_blobs,
    make_circles,
    make_classification,
    make_gaussian_quantiles,
    make_moons,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    silhouette_samples,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

MODOS = ("Clasificación", "Regresión", "Agrupamiento")

DATASETS = {
    "Clasificación": (
        "Blobs",
        "Grupos",
        "Lunas",
        "Círculos",
        "Clasificación",
        "Gaussianos",
        "Espiral",
        "Aleatorio",
    ),
    "Regresión": (
        "Lineal",
        "Con ruido",
        "Con atípicos",
        "No lineal",
    ),
    "Agrupamiento": (
        "Tres grupos",
        "Grupos desiguales",
        "Lunas",
        "Círculos",
        "Aleatorio",
    ),
}

MODELOS = {
    "Clasificación": (
        "Regresión logística",
        "KNN",
        "Árbol de decisión",
        "Random Forest",
    ),
    "Regresión": (
        "Regresión lineal",
        "Regresión polinómica",
        "KNN regresión",
        "Árbol de regresión",
    ),
    "Agrupamiento": ("K-Means",),
}


@dataclass
class ResultadoEntrenamiento:
    """Reúne el modelo entrenado y los datos usados para evaluarlo."""

    modo: str
    nombre_modelo: str
    modelo: object
    X: np.ndarray
    y: np.ndarray | None
    X_train: np.ndarray
    X_test: np.ndarray | None = None
    y_train: np.ndarray | None = None
    y_test: np.ndarray | None = None
    metricas: dict[str, float] = field(default_factory=dict)
    silhouette_muestras: np.ndarray | None = None


# -----------------------------------------------------------------------------
# Genera internamente las dos ramas entrelazadas del dataset de espirales.
# -----------------------------------------------------------------------------
def _make_spiral(n: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Genera dos espirales entrelazadas con un total aproximado de ``n`` puntos."""

    n_brazo = max(2, n // 2)
    r = np.linspace(0.15, 5.0, n_brazo)
    t = np.linspace(0, 3.5 * np.pi, n_brazo)
    ruido = rng.normal(0, 0.12, size=(n_brazo, 2))
    brazo_0 = np.c_[r * np.cos(t), r * np.sin(t)] + ruido
    brazo_1 = np.c_[r * np.cos(t + np.pi), r * np.sin(t + np.pi)] - ruido
    X = np.vstack((brazo_0, brazo_1))
    y = np.r_[np.zeros(n_brazo, dtype=int), np.ones(n_brazo, dtype=int)]
    return X, y


# -----------------------------------------------------------------------------
# Crea el dataset sintético solicitado según el tipo de problema seleccionado.
# -----------------------------------------------------------------------------
def generar_dataset(
    modo: str,
    nombre: str,
    n_muestras: int = 120,
    seed: int | None = None,
) -> tuple[np.ndarray, np.ndarray | None]:
    """Genera un dataset adecuado para el modo seleccionado."""

    rng = np.random.default_rng(seed)
    random_state = int(rng.integers(0, 2**31 - 1))

    # Cada rama devuelve la forma de datos que espera su familia de modelos:
    # dos coordenadas y etiquetas, una coordenada y objetivo, o puntos sin etiqueta.
    if modo == "Clasificación":
        if nombre == "Blobs":
            X, y = make_blobs(
                n_samples=n_muestras,
                centers=2,
                cluster_std=1.25,
                random_state=random_state,
            )
        elif nombre == "Grupos":
            X, grupos = make_blobs(
                n_samples=n_muestras,
                centers=4,
                cluster_std=1.0,
                random_state=random_state,
            )
            y = np.where(np.isin(grupos, (0, 2)), 0, 1)
        elif nombre == "Lunas":
            X, y = make_moons(
                n_samples=n_muestras, noise=0.22, random_state=random_state
            )
        elif nombre == "Círculos":
            X, y = make_circles(
                n_samples=n_muestras,
                noise=0.14,
                factor=0.48,
                random_state=random_state,
            )
        elif nombre == "Clasificación":
            X, y = make_classification(
                n_samples=n_muestras,
                n_features=2,
                n_redundant=0,
                n_informative=2,
                n_clusters_per_class=1,
                class_sep=0.85,
                flip_y=0.06,
                random_state=random_state,
            )
        elif nombre == "Gaussianos":
            X, y = make_gaussian_quantiles(
                n_samples=n_muestras,
                n_features=2,
                n_classes=2,
                random_state=random_state,
            )
        elif nombre == "Espiral":
            X, y = _make_spiral(n_muestras, rng)
        elif nombre == "Aleatorio":
            X = rng.uniform(-5, 5, size=(n_muestras, 2))
            y = rng.integers(0, 2, size=n_muestras)
        else:
            raise ValueError(f"Dataset de clasificación desconocido: {nombre}")
        return np.asarray(X, dtype=float), np.asarray(y, dtype=int)

    if modo == "Regresión":
        x = np.sort(rng.uniform(-5, 5, n_muestras))
        if nombre == "Lineal":
            y = 1.3 + 1.8 * x + rng.normal(0, 0.65, n_muestras)
        elif nombre == "Con ruido":
            y = -0.5 + 1.45 * x + rng.normal(0, 2.25, n_muestras)
        elif nombre == "Con atípicos":
            y = 1.0 + 1.65 * x + rng.normal(0, 0.7, n_muestras)
            cantidad = max(3, n_muestras // 12)
            indices = rng.choice(n_muestras, size=cantidad, replace=False)
            y[indices] += rng.choice((-1, 1), size=cantidad) * rng.uniform(
                6, 10, cantidad
            )
        elif nombre == "No lineal":
            y = 0.65 * x**2 - 2.0 + rng.normal(0, 1.0, n_muestras)
        else:
            raise ValueError(f"Dataset de regresión desconocido: {nombre}")
        return np.c_[x], np.asarray(y, dtype=float)

    if modo == "Agrupamiento":
        if nombre == "Tres grupos":
            X, _ = make_blobs(
                n_samples=n_muestras,
                centers=3,
                cluster_std=0.9,
                random_state=random_state,
            )
        elif nombre == "Grupos desiguales":
            centros = np.array([[-3.0, -2.0], [0.5, 2.5], [3.4, -1.2]])
            cantidades = [
                n_muestras // 4,
                n_muestras // 2,
                n_muestras - 3 * n_muestras // 4,
            ]
            dispersiones = [0.42, 1.25, 0.72]
            partes = [
                rng.normal(centro, dispersion, size=(cantidad, 2))
                for centro, dispersion, cantidad in zip(
                    centros, dispersiones, cantidades
                )
            ]
            X = np.vstack(partes)
        elif nombre == "Lunas":
            X, _ = make_moons(
                n_samples=n_muestras, noise=0.13, random_state=random_state
            )
        elif nombre == "Círculos":
            X, _ = make_circles(
                n_samples=n_muestras,
                noise=0.09,
                factor=0.42,
                random_state=random_state,
            )
        elif nombre == "Aleatorio":
            X = rng.uniform(-5, 5, size=(n_muestras, 2))
        else:
            raise ValueError(f"Dataset de agrupamiento desconocido: {nombre}")
        return np.asarray(X, dtype=float), None

    raise ValueError(f"Modo desconocido: {modo}")


# -----------------------------------------------------------------------------
# Construye, entrena y evalúa el estimador elegido con sus hiperparámetros.
# -----------------------------------------------------------------------------
def entrenar_modelo(
    modo: str,
    nombre_modelo: str,
    X: np.ndarray,
    y: np.ndarray | None,
    parametros: dict[str, float | int] | None = None,
) -> ResultadoEntrenamiento:
    """Entrena y evalúa un modelo sin utilizar los datos de prueba durante el ajuste."""

    parametros = parametros or {}

    if modo == "Clasificación":
        if y is None:
            raise ValueError("Los modelos de clasificación necesitan etiquetas.")
        # La evaluación es genuina: el 25 % de prueba no participa del ajuste.
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.25,
            random_state=42,
            stratify=y,
        )
        if nombre_modelo == "Regresión logística":
            modelo = LogisticRegression(
                C=float(parametros.get("C", 1.0)), max_iter=1000
            )
        elif nombre_modelo == "KNN":
            k = min(int(parametros.get("vecinos", 5)), len(X_train))
            modelo = KNeighborsClassifier(n_neighbors=max(1, k))
        elif nombre_modelo == "Árbol de decisión":
            modelo = DecisionTreeClassifier(
                max_depth=int(parametros.get("profundidad", 4)),
                random_state=42,
            )
        elif nombre_modelo == "Random Forest":
            modelo = RandomForestClassifier(
                n_estimators=int(parametros.get("arboles", 50)),
                max_depth=int(parametros.get("profundidad", 5)),
                random_state=42,
                n_jobs=-1,
            )
        else:
            raise ValueError(f"Modelo de clasificación desconocido: {nombre_modelo}")

        modelo.fit(X_train, y_train)
        metricas = {
            "Accuracy entrenamiento": accuracy_score(y_train, modelo.predict(X_train)),
            "Accuracy prueba": accuracy_score(y_test, modelo.predict(X_test)),
        }
        return ResultadoEntrenamiento(
            modo,
            nombre_modelo,
            modelo,
            X,
            y,
            X_train,
            X_test,
            y_train,
            y_test,
            metricas,
        )

    if modo == "Regresión":
        if y is None:
            raise ValueError("La regresión necesita una variable objetivo.")
        # Se mantiene la misma partición al comparar modelos sobre estos datos.
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=42
        )
        if nombre_modelo == "Regresión lineal":
            modelo = LinearRegression()
        elif nombre_modelo == "Regresión polinómica":
            grado = int(parametros.get("grado", 2))
            modelo = make_pipeline(
                PolynomialFeatures(degree=grado, include_bias=False),
                LinearRegression(),
            )
        elif nombre_modelo == "KNN regresión":
            k = min(int(parametros.get("vecinos", 5)), len(X_train))
            modelo = KNeighborsRegressor(n_neighbors=max(1, k))
        elif nombre_modelo == "Árbol de regresión":
            modelo = DecisionTreeRegressor(
                max_depth=int(parametros.get("profundidad", 4)),
                random_state=42,
            )
        else:
            raise ValueError(f"Modelo de regresión desconocido: {nombre_modelo}")
        modelo.fit(X_train, y_train)
        pred_test = modelo.predict(X_test)
        metricas = {
            "R² prueba": r2_score(y_test, pred_test),
            "MAE prueba": mean_absolute_error(y_test, pred_test),
            "RMSE prueba": np.sqrt(mean_squared_error(y_test, pred_test)),
        }
        return ResultadoEntrenamiento(
            modo,
            nombre_modelo,
            modelo,
            X,
            y,
            X_train,
            X_test,
            y_train,
            y_test,
            metricas,
        )

    if modo == "Agrupamiento":
        if nombre_modelo != "K-Means":
            raise ValueError(f"Modelo de agrupamiento desconocido: {nombre_modelo}")
        clusters = min(max(2, int(parametros.get("clusters", 3))), len(X) - 1)
        modelo = KMeans(n_clusters=clusters, n_init=10, random_state=42)
        labels = modelo.fit_predict(X)
        metricas: dict[str, float] = {}
        sil_muestras = None
        if 1 < len(np.unique(labels)) < len(X):
            metricas["Silhouette"] = silhouette_score(X, labels)
            sil_muestras = silhouette_samples(X, labels)
        metricas["Inercia"] = modelo.inertia_
        return ResultadoEntrenamiento(
            modo,
            nombre_modelo,
            modelo,
            X,
            None,
            X,
            metricas=metricas,
            silhouette_muestras=sil_muestras,
        )

    raise ValueError(f"Modo desconocido: {modo}")


# -----------------------------------------------------------------------------
# Calcula los límites visibles y añade un margen proporcional alrededor de los datos.
# -----------------------------------------------------------------------------
def calcular_limites(
    modo: str,
    X: np.ndarray,
    y: np.ndarray | None,
) -> tuple[float, float, float, float]:
    """Devuelve límites con margen para el gráfico actual."""

    if modo == "Regresión":
        if y is None:
            raise ValueError("Falta la variable objetivo de la regresión.")
        xmin, xmax = float(X[:, 0].min()), float(X[:, 0].max())
        ymin, ymax = float(y.min()), float(y.max())
    else:
        xmin, xmax = float(X[:, 0].min()), float(X[:, 0].max())
        ymin, ymax = float(X[:, 1].min()), float(X[:, 1].max())

    margen_x = max(0.5, (xmax - xmin) * 0.12)
    margen_y = max(0.5, (ymax - ymin) * 0.12)
    return xmin - margen_x, xmax + margen_x, ymin - margen_y, ymax + margen_y


# -----------------------------------------------------------------------------
# Evalúa un modelo bidimensional sobre una grilla para rasterizar su mapa de fondo.
# -----------------------------------------------------------------------------
def calcular_mapa(
    resultado: ResultadoEntrenamiento,
    limites: tuple[float, float, float, float],
    resolucion: int = 180,
) -> tuple[np.ndarray, np.ndarray | None, np.ndarray, np.ndarray]:
    """Calcula clases y probabilidades sobre una grilla 2D."""

    if resultado.modo == "Regresión":
        raise ValueError("Los modelos de regresión no utilizan un mapa 2D.")
    xmin, xmax, ymin, ymax = limites
    xs = np.linspace(xmin, xmax, resolucion)
    ys = np.linspace(ymin, ymax, resolucion)
    xx, yy = np.meshgrid(xs, ys)
    puntos = np.c_[xx.ravel(), yy.ravel()]
    clases = resultado.modelo.predict(puntos).reshape(xx.shape)
    probabilidades = None
    if resultado.modo == "Clasificación" and hasattr(resultado.modelo, "predict_proba"):
        probabilidades = resultado.modelo.predict_proba(puntos)[:, 1].reshape(xx.shape)
    return clases, probabilidades, xs, ys
