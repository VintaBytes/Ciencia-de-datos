"""Ventanas auxiliares independientes del tema visual seleccionado."""

# ruff: noqa: ISC004

from __future__ import annotations

import tkinter as tk
import webbrowser

URL_PROYECTO = "https://github.com/VintaBytes/Ciencia-de-datos"


MANUAL = (
    ("ML Visualizer 2.0", "titulo"),
    (
        "ML Visualizer es una aplicación didáctica para explorar el comportamiento de modelos "
        "sencillos de Machine Learning. Permite generar datos sintéticos, entrenar modelos y "
        "observar de forma interactiva sus predicciones, fronteras y métricas.",
        "normal",
    ),
    ("Panel de configuración", "seccion"),
    (
        "Tipo de problema\n"
        "Define la clase de tarea que se desea estudiar. Clasificación asigna cada punto a una "
        "clase; Regresión estima un valor numérico continuo; Agrupamiento busca grupos sin usar "
        "etiquetas conocidas.",
        "normal",
    ),
    (
        "Dataset sintético\n"
        "Selecciona la distribución de los datos. Cada tipo de problema ofrece ejemplos adecuados: "
        "grupos separados, lunas, círculos, espirales, relaciones lineales, datos con ruido, valores "
        "atípicos y otras situaciones útiles para comparar modelos.",
        "normal",
    ),
    (
        "Número de muestras\n"
        "Indica cuántos puntos se generarán al crear un nuevo dataset. Una cantidad pequeña facilita "
        "el seguimiento de cada observación; una cantidad mayor permite apreciar mejor la tendencia "
        "general. Al modificar este valor se genera nuevamente el conjunto de datos.",
        "normal",
    ),
    (
        "Modelo\n"
        "La opción Ninguno — solo datos permite observar primero la distribución sin entrenar ningún "
        "algoritmo. Al seleccionar luego un modelo, se entrena automáticamente con esos mismos datos. "
        "Cambiar de modelo nunca genera ni reemplaza el dataset visible. "
        "Los modelos disponibles dependen del tipo de "
        "problema seleccionado. La clasificación incluye regresión logística, KNN, árbol de decisión "
        "y Random Forest; la regresión incluye regresión lineal, polinómica, KNN y árbol de regresión; "
        "el agrupamiento utiliza K-Means.",
        "normal",
    ),
    (
        "Parámetros del modelo\n"
        "Muestra únicamente los hiperparámetros relevantes para el modelo actual: regularización, "
        "cantidad de vecinos, profundidad, número de árboles o cantidad de clusters. Al modificar un "
        "parámetro, el modelo vuelve a entrenarse.",
        "normal",
    ),
    (
        "Representación del mapa\n"
        "En clasificación puede alternarse entre el mapa Normal, el mapa de Probabilidad y el mapa "
        "de Incertidumbre. Este control se desactiva en regresión y agrupamiento porque esas tareas "
        "utilizan otras representaciones.",
        "normal",
    ),
    (
        "Visualización didáctica (V)\n"
        "Agrega información específica del modelo: vecinos de KNN, hoja activa del árbol, votos de "
        "Random Forest, centroides y silhouette de K-Means, residuos de los modelos de regresión y "
        "detalles del cálculo bajo el cursor.",
        "normal",
    ),
    ("Botones y gráfico interactivo", "seccion"),
    (
        "Nuevo dataset genera otra realización aleatoria con la distribución seleccionada. Reentrenar "
        "vuelve a ajustar el modelo sobre los puntos actuales sin reemplazarlos; permanece desactivado "
        "cuando no hay un modelo seleccionado.\n\n"
        "Al mover el cursor sobre el gráfico se muestra la predicción local y, cuando corresponde, "
        "probabilidades, vecinos, votos, hojas o silhouette. Sin modelo se muestran solamente las "
        "coordenadas.\n\n"
        "En Clasificación, el clic izquierdo agrega un punto de clase 0 y el clic derecho uno de clase 1. "
        "En Regresión y Agrupamiento, el clic izquierdo agrega un punto y el derecho elimina el punto "
        "más cercano.",
        "normal",
    ),
    ("Métricas", "seccion"),
    (
        "Los clasificadores muestran accuracy de entrenamiento y de prueba. Los modelos de regresión "
        "muestran R², MAE y RMSE sobre el conjunto de prueba; esas métricas permiten comparar los cuatro "
        "modelos de regresión. K-Means informa silhouette e inercia. Random Forest "
        "también muestra la importancia calculada para cada variable.",
        "normal",
    ),
    ("Menú Archivo", "seccion"),
    (
        "Abrir carga una configuración JSON previamente guardada. Guardar actualiza el archivo de "
        "configuración actual y Guardar como permite elegir un archivo nuevo. La configuración conserva "
        "el tipo de problema, dataset, cantidad de muestras, modelo, hiperparámetros, representación, "
        "visualización didáctica, tema y semilla del dataset. Los puntos agregados o eliminados "
        "manualmente no se guardan en el archivo JSON.",
        "normal",
    ),
    ("Menú Apariencia", "seccion"),
    (
        "Permite elegir el tema de ttkbootstrap. El tema modifica la apariencia de los controles y "
        "ventanas, pero no cambia la paleta utilizada dentro del gráfico. Los temas nativos están "
        "organizados en variantes claras y oscuras.",
        "normal",
    ),
    ("Atajos", "seccion"),
    (
        "Ctrl+O: abrir configuración\n"
        "Ctrl+S: guardar configuración\n"
        "Ctrl+Mayús+S: guardar como\n"
        "F1: abrir este manual\n"
        "V: activar u ocultar la visualización didáctica\n"
        "B: cambiar la representación del mapa\n"
        "R: generar un nuevo dataset",
        "normal",
    ),
)


# -----------------------------------------------------------------------------
# Construye y muestra la ventana desplazable que contiene el manual integrado.
# -----------------------------------------------------------------------------
def mostrar_ayuda(parent: tk.Misc) -> None:
    """Abre un mini manual desplazable con colores fijos y tipografía liviana."""

    ventana = tk.Toplevel(parent, background="#ffffff")
    ventana.title("Manual de uso · ML Visualizer")
    ventana.geometry("780x680")
    ventana.minsize(600, 450)
    ventana.transient(parent)

    contenedor = tk.Frame(ventana, background="#ffffff", padx=22, pady=18)
    contenedor.pack(fill="both", expand=True)
    contenedor.rowconfigure(0, weight=1)
    contenedor.columnconfigure(0, weight=1)

    texto = tk.Text(
        contenedor,
        wrap="word",
        background="#ffffff",
        foreground="#3f4650",
        insertbackground="#3f4650",
        selectbackground="#dce7f5",
        selectforeground="#303640",
        relief="flat",
        borderwidth=0,
        padx=8,
        pady=6,
        font=("DejaVu Sans", 11),
        spacing1=2,
        spacing3=8,
        cursor="arrow",
    )
    barra = tk.Scrollbar(contenedor, orient="vertical", command=texto.yview)
    texto.configure(yscrollcommand=barra.set)
    texto.grid(row=0, column=0, sticky="nsew")
    barra.grid(row=0, column=1, sticky="ns")

    texto.tag_configure(
        "titulo",
        font=("DejaVu Sans", 20),
        foreground="#28323d",
        spacing1=2,
        spacing3=14,
    )
    texto.tag_configure(
        "seccion",
        font=("DejaVu Sans", 13),
        foreground="#34495e",
        spacing1=14,
        spacing3=6,
    )
    texto.tag_configure(
        "normal", font=("DejaVu Sans", 11), foreground="#454b54", lmargin2=0
    )

    # Cada bloque se inserta con una etiqueta propia para mantener una lectura liviana.
    for contenido, estilo in MANUAL:
        texto.insert("end", contenido + "\n", estilo)
    texto.configure(state="disabled")
    texto.focus_set()

    pie = tk.Frame(ventana, background="#ffffff", padx=22, pady=(0, 18))
    pie.pack(fill="x")
    tk.Button(
        pie,
        text="Cerrar",
        command=ventana.destroy,
        background="#e8edf3",
        foreground="#343a43",
        activebackground="#dce3eb",
        activeforeground="#252a31",
        relief="flat",
        padx=22,
        pady=7,
        cursor="hand2",
    ).pack(side="right")
    ventana.bind("<Escape>", lambda _e: ventana.destroy())


# -----------------------------------------------------------------------------
# Construye la ventana con la versión, la autoría y el enlace del proyecto.
# -----------------------------------------------------------------------------
def mostrar_acerca_de(parent: tk.Misc) -> None:
    """Muestra la identificación, autoría y vínculo del proyecto."""

    ventana = tk.Toplevel(parent, background="#ffffff")
    ventana.title("Acerca de ML Visualizer")
    ventana.geometry("560x340")
    ventana.resizable(False, False)
    ventana.transient(parent)
    ventana.grab_set()

    tk.Label(
        ventana,
        text="ML Visualizer",
        background="#ffffff",
        foreground="#28323d",
        font=("DejaVu Sans", 22),
    ).pack(pady=(34, 4))
    tk.Label(
        ventana,
        text="Versión 2.0",
        background="#ffffff",
        foreground="#59636f",
        font=("DejaVu Sans", 11),
    ).pack()
    tk.Label(
        ventana,
        text="Creado por Ariel Palazzesi\ncon ayuda de IA (ChatGPT).",
        background="#ffffff",
        foreground="#414851",
        font=("DejaVu Sans", 11),
        justify="center",
    ).pack(pady=(24, 18))
    tk.Label(
        ventana,
        text="Más material sobre Machine Learning:",
        background="#ffffff",
        foreground="#59636f",
        font=("DejaVu Sans", 10),
    ).pack()
    enlace = tk.Label(
        ventana,
        text=URL_PROYECTO,
        background="#ffffff",
        foreground="#2869a8",
        activeforeground="#174d7c",
        font=("DejaVu Sans", 10, "underline"),
        cursor="hand2",
    )
    enlace.pack(pady=(4, 22))
    enlace.bind("<Button-1>", lambda _e: webbrowser.open_new_tab(URL_PROYECTO))
    tk.Button(
        ventana,
        text="Cerrar",
        command=ventana.destroy,
        background="#e8edf3",
        foreground="#343a43",
        relief="flat",
        padx=22,
        pady=7,
        cursor="hand2",
    ).pack()
    ventana.bind("<Escape>", lambda _e: ventana.destroy())
