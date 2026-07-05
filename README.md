# Ciencia de Datos con Python

🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) 🤝 

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python\&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn\&logoColor=white)


Este repositorio reúne materiales, cuadernos Colab y recursos de apoyo para aprender y enseñar programación, análisis de datos, ciencia de datos y machine learning con Python.

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/readme.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada1.png" alt="Ciencia de Datos con Python - Vol 1">
      </a>
      <br>
      <strong><a href="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/readme.md">Volumen I</a></strong>
      <br>
      Primeros pasos con datos
    </td>
  <td align="center">
      <a href="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/README2.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada2.png" alt="Ciencia de Datos con Python - Vol 2">
      </a>
      <br>
      <strong><a href="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/README2.md">Volumen II</a></strong>
      <br>
      Análisis exploratorio
    </td>
  </tr>
</table>


* [Machine Learning con Python](#machine-learning-con-python)
* [Análisis de Datos con Python](#análisis-de-datos-con-python)
* [¿Qué recorrido elegir?](#qué-recorrido-elegir)
* [Sobre las posibles superposiciones](#sobre-las-posibles-superposiciones)
* [Uso de los cuadernos](#uso-de-los-cuadernos)
* [Autor](#autor)

El material está organizado en distintos recorridos formativos. Algunos contenidos pueden superponerse parcialmente, especialmente en temas como Pandas, visualización de datos o preparación de datasets, pero cada carpeta responde a un objetivo didáctico diferente. Por eso, las secciones no deben leerse como materiales duplicados, sino como recorridos complementarios.

---

### Machine Learning con Python

Esta sección contiene cuadernos orientados a la introducción al aprendizaje automático con Python. El recorrido presupone cierta familiaridad previa con Pandas y análisis exploratorio de datos. A partir de esa base, avanza hacia la construcción, evaluación y comparación de modelos de machine learning. Fueron escritos para acompañar las clases de un curso de Machine Learning en 2026.


* [Introducción al Machine Learning: analizando el dataset](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno01_Analizando_el_dataset.ipynb) Este primer cuaderno presenta una aproximación inicial al trabajo con datasets en el contexto de machine learning. Se parte del análisis de los datos para comprender su estructura, sus variables y su posible utilidad para construir modelos.
* [Repaso de Pandas, Matplotlib, Seaborn y Plotly](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno02_Repaso_Modulos_Graficos.ipynb) Este cuaderno recupera herramientas fundamentales para explorar y visualizar datos antes de entrenar modelos. Incluye operaciones con Pandas y visualizaciones con bibliotecas habituales del ecosistema Python.
* [Transformación de datos: el primer paso hacia el modelo](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno03_Transformacion_de_datos_el_primer_paso_hacia_el_modelo.ipynb) Se trabaja sobre la preparación de los datos antes del modelado. El objetivo es mostrar que un modelo no se entrena directamente sobre cualquier tabla, sino sobre datos organizados y transformados de acuerdo con el problema a resolver.
* [División de datos y validación cruzada](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno04_Division_de_datos_y_validacion_cruzada.ipynb) Este cuaderno introduce la separación entre datos de entrenamiento y datos de prueba, junto con la idea de validación cruzada. Se busca evitar evaluaciones engañosas y construir una mirada más confiable sobre el rendimiento de los modelos.
* [Regresión lineal y métricas de evaluación: MAE, MSE, RMSE y R²](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno05_RegresionLineal_y_EvaluacionDelModelo.ipynb) Se presenta un primer modelo supervisado de regresión. Además de entrenar el modelo, se trabajan métricas de evaluación que permiten interpretar la magnitud de los errores y la calidad general de las predicciones.
* [Regresión logística y evaluación de clasificadores](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno06_RegresionLogistica_y_EvaluacionDelModelo.ipynb) Este cuaderno introduce un modelo de clasificación y las métricas utilizadas para evaluar clasificadores. Se trabaja con conceptos como matriz de confusión, accuracy, precision, recall y F1-score.
* [Clasificación con KNN (K-Nearest Neighbors)](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno07_Clasificacion_con_KNN_%28K_Nearest_Neighbors%29.ipynb) Se aborda el algoritmo KNN como modelo de clasificación basado en cercanía entre observaciones. El cuaderno permite analizar la importancia de la escala de las variables y el efecto de elegir distintos valores de `k`.
* [Árboles de decisión y Random Forest](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno08_%C3%81rboles_de_Decisi%C3%B3n_y_Random_Forest.ipynb) Este cuaderno presenta modelos basados en árboles. Se trabaja la diferencia entre un árbol individual y un ensamble como Random Forest, junto con ideas como profundidad, sobreajuste, importancia de variables y comparación de desempeño.
* [Introducción al clustering con K-Means](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno09A_K_Means_.ipynb) Introducción al aprendizaje no supervisado mediante el algoritmo K-Means.
* [K-Means en datos reales: cuando el clustering ayuda, pero no alcanza](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno09B_K_Means_Pinguinos.ipynb) Limitaciones del modelo.
* [Segmentación de clientes con K-Means](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno09C_K_Means_Consumidores.ipynb) Algoritmo K-Means en la segmentación de clientes.
* [Automatización del flujo de trabajo con Pipelines y GridSearchCV](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno10_Pipelines.ipynb) Este cuaderno está orientado a organizar el flujo completo de trabajo mediante pipelines. También introduce la búsqueda de hiperparámetros con GridSearchCV, una herramienta clave para comparar configuraciones de modelos de manera sistemática.
* [Comparación y evaluación de modelos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno11_Evaluacion_de_modelos.ipynb) Se trabaja sobre la comparación entre distintos modelos y métricas. El objetivo es reforzar que no alcanza con entrenar un modelo: también es necesario evaluar resultados, interpretar errores y elegir la alternativa más adecuada para el problema.
* [Guardar y recuperar un modelo entrenado en scikit-learn](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno12_Guardar_y_recuperar_modelos.ipynb) En este mini-cuaderno vamos a entrenar rápidamente un modelo de clasificación y luego veremos cómo guardarlo en un archivo para poder reutilizarlo más adelante sin repetir el entrenamiento.
* [Exploración y preparación de un dataset clínico](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Machine%20Learning%20con%20Python/Cuaderno13_Proyecto_Final.ipynb) Este cuaderno propone trabajar con un dataset de contexto clínico, poniendo el foco en la exploración inicial, la preparación de variables y las decisiones previas al entrenamiento de modelos.Avanza sobre el entrenamiento, evaluación y selección de modelos. La intención es integrar varias etapas del flujo de trabajo en un caso más completo.


[Ver carpeta: Machine Learning con Python](https://github.com/VintaBytes/Ciencia-de-datos/tree/main/Machine%20Learning%20con%20Python#readme)

[Volver al principio](#ciencia-de-datos-con-python)

---

### Análisis de Datos con Python

Esta sección contiene cuadernos Colab orientados al trabajo exploratorio con datos usando Python. Incluye materiales sobre Pandas, NumPy, limpieza de datos, selección y filtrado, agrupamientos, visualización y análisis descriptivo. Fueron escritos para acompañar las clases de un curso de Ciencias de Datos en 2025. Están pensadoa para quienes quieren aprender a manipular, explorar y presentar datos con herramientas habituales del ecosistema Python.

#### Cuadernos disponibles:
* [1 - Técnicas para limpiar datos con Pandas](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase05/Clase05.ipynb)
* [2A - Selecciones y filtros de datos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase06/Clase06.ipynb)  
* [2B - Actividad práctica: filtrar pasajeros sobrevivientes en el naufragio del Titanic](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase06/Clase06-Actividad-Practica.ipynb)
* [3A - Funciones de agregación y agrupamiento de datos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase07/Clase07.ipynb)
* [3B - Actividad práctica: usar `groupby()` de Pandas para segmentar el dataset](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase07/Clase07-Actividad-Practica.ipynb)
* [4A - Manejo de arrays en NumPy](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase08/Clase08.ipynb)
* [4B - Actividad práctica: integración de DataFrames](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase08/Clase08-Actividad-Practica.ipynb)
* [5A - Estadística descriptiva: análisis de tendencia central](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase09/Clase09_1.ipynb)
* [5B - Estadística descriptiva: análisis de dispersión](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase09/Clase09_2.ipynb)
* [6A - Introducción a la visualización de datos con Matplotlib](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase10/Clase10.ipynb)
* [6B - Actividad práctica: análisis exploratorio del conjunto de datos `diamonds`](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase10/Clase10-Actividad-Practica.ipynb)
* [7A - Análisis y cálculo de correlación con Pandas](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase11/Clase11.ipynb)
* [7B - Introducción a gráficos con Seaborn](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase11/Clase11-Graficos-Seaborn.ipynb)
* [7C - Actividad práctica: análisis de correlación](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase11/Clase11-Actividad-practica.ipynb)
* [8A - Consolidación de datos: análisis de ventas y productos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase12/Clase12-Actividad-practica-1.ipynb)
* [8B - Consolidación de datos: análisis de asistencia y resultados en talleres de capacitación](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase12/Clase12-Actividad-practica-2.ipynb)
* [9A - Matplotlib: análisis de ventas a lo largo del tiempo con gráficos de líneas](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase13/Clase13-Actividad-practica-1-Matplotlib.ipynb)
* [9B - Matplotlib: análisis de ventas a lo largo del tiempo con gráficos de barras](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase13/Clase13-Actividad-practica-2-Matplotlib.ipynb)
* [9C - Seaborn: análisis de ventas a lo largo del tiempo con gráficos de líneas](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase13/Clase13-Actividad-practica-1-Seaborn.ipynb)
* [9D - Seaborn: análisis de ventas a lo largo del tiempo con gráficos de barras](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase13/Clase13-Actividad-practica-2-Seaborn.ipynb)
* [10 - Gráficos con Seaborn](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase14/Clase14.ipynb)
* [11A - Dashboard con Seaborn](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase15/Clase15.ipynb) Este cuaderno debe ser visualizado en Google Colab.
* [11B - Actividad práctica: dashboard con Seaborn](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/An%C3%A1lisis%20de%20Datos%20con%20Python/Clase15/Clase15-Actividad-practica.ipynb)

[Ver carpeta: Análisis de Datos con Python](https://github.com/VintaBytes/Ciencia-de-datos/tree/main/An%C3%A1lisis%20de%20Datos%20con%20Python#readme)

[Volver al principio](#ciencia-de-datos-con-python)

---

## Qué recorrido elegir

Si estás empezando desde cero con Pandas y querés un recorrido gradual, conviene comenzar por **[Ciencia de Datos con Python](https://github.com/VintaBytes/Ciencia-de-datos/tree/main/Ciencia%20De%20Datos%20Con%20Python)**.

Si ya conocés algo de Python y querés practicar análisis exploratorio, limpieza y visualización de datos, podés entrar por **[Análisis de Datos con Python](https://github.com/VintaBytes/Ciencia-de-datos/tree/main/An%C3%A1lisis%20de%20Datos%20con%20Python#readme)**.

Si ya tenés una base de trabajo con datos y querés avanzar hacia modelos predictivos, el recorrido natural es **[Machine Learning con Python](https://github.com/VintaBytes/Ciencia-de-datos/tree/main/Machine%20Learning%20con%20Python#readme)**.

[Volver al principio](#ciencia-de-datos-con-python)

---

## Sobre las posibles superposiciones

Algunos temas aparecen en más de una sección. Esto es intencional. Por ejemplo, Pandas puede aparecer en un curso de análisis de datos, en una introducción progresiva a ciencia de datos y también como repaso previo al trabajo con modelos de machine learning. En cada caso, el tema se aborda con una profundidad y una finalidad distinta. La idea general del repositorio es ofrecer materiales reutilizables, adaptables y complementarios para distintos momentos de aprendizaje.

[Volver al principio](#ciencia-de-datos-con-python)

---

## Uso de los cuadernos

Los cuadernos están pensados para ser abiertos y ejecutados en Google Colab. Cada notebook puede leerse como material de estudio y también usarse como base para clases, prácticas guiadas o actividades de exploración.
En muchos casos, los cuadernos combinan explicación conceptual, código Python, salidas comentadas e interpretaciones de resultados.

[Volver al principio](#ciencia-de-datos-con-python)

---

## Autor

Material desarrollado por **VintaBytes** como parte de distintos recorridos formativos vinculados con programación, análisis de datos, ciencia de datos y machine learning con Python.

[Volver al principio](#ciencia-de-datos-con-python)
