# Machine Learning con Python

### Ariel Palazzesi · 2026

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python\&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn\&logoColor=white)


🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) · 🏠 [Volver al inicio del repositorio](../../README.md)


----

Este directorio reúne cuadernos Colab creados como material de apoyo para un recorrido introductorio de **Machine Learning con Python**.

> **Estado del material:** curso finalizado. Los cuadernos se conservan como recursos de consulta y práctica.

El material está pensado para estudiantes que ya tienen una base inicial en Python y cierto contacto previo con el trabajo con datos usando Pandas. A partir de esa base, los cuadernos avanzan hacia la preparación de datasets, la división de datos, el entrenamiento de modelos, la evaluación de resultados y la comparación entre distintas técnicas de aprendizaje automático.

Este recorrido forma parte del repositorio general **Ciencia de Datos con Python**, pero tiene un objetivo específico: introducir los principales conceptos y procedimientos del machine learning supervisado y no supervisado mediante ejemplos prácticos en Google Colab.

---

## Sobre este recorrido

Los cuadernos están pensados para ser abiertos y ejecutados en **Google Colab**.

Cada notebook combina explicación conceptual, código Python, análisis de salidas y comentarios sobre la interpretación de los resultados. El foco no está solamente en ejecutar modelos, sino también en comprender qué problema estamos resolviendo, qué decisiones tomamos durante el proceso y cómo evaluar si un modelo es adecuado.

A lo largo del recorrido se trabajan modelos de regresión, clasificación y clustering. También se incorporan herramientas habituales del flujo de trabajo en machine learning, como partición de datos, validación cruzada, métricas de evaluación, pipelines y búsqueda de hiperparámetros.

---

## Índice de contenidos
<table>
  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 1" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 1 · Introducción al Machine Learning</strong><br><br>
      <a href="cuadernos/cuaderno-01-analizando-el-dataset.ipynb">Introducción al Machine Learning: analizando el dataset</a><br><br>
      Este primer cuaderno presenta una aproximación inicial al trabajo con datasets en el contexto de machine learning. Se parte del análisis de los datos para comprender su estructura, sus variables y su posible utilidad para construir modelos.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 2" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 2 · Repaso de herramientas para análisis de datos</strong><br><br>
      <a href="cuadernos/cuaderno-02-repaso-modulos-graficos.ipynb">Repaso de Pandas, Matplotlib, Seaborn y Plotly</a><br><br>
      Este cuaderno recupera herramientas fundamentales para explorar y visualizar datos antes de entrenar modelos. Incluye operaciones con Pandas y visualizaciones con bibliotecas habituales del ecosistema Python.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 3" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 3 · Transformación de datos</strong><br><br>
      <a href="cuadernos/cuaderno-03-transformacion-de-datos-el-primer-paso-hacia-el-modelo.ipynb">Transformación de datos: el primer paso hacia el modelo</a><br><br>
      Se trabaja sobre la preparación de los datos antes del modelado. El objetivo es mostrar que un modelo no se entrena directamente sobre cualquier tabla, sino sobre datos organizados y transformados de acuerdo con el problema a resolver.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 4" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 4 · División de datos y validación cruzada</strong><br><br>
      <a href="cuadernos/cuaderno-04-division-de-datos-y-validacion-cruzada.ipynb">División de datos y validación cruzada</a><br><br>
      Este cuaderno introduce la separación entre datos de entrenamiento y datos de prueba, junto con la idea de validación cruzada. Se busca evitar evaluaciones engañosas y construir una mirada más confiable sobre el rendimiento de los modelos.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 5" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 5 · Regresión lineal y evaluación de modelos</strong><br><br>
      <a href="cuadernos/cuaderno-05-regresion-lineal-y-evaluacion-del-modelo.ipynb">Regresión lineal y métricas de evaluación: MAE, MSE, RMSE y R²</a><br><br>
      Se presenta un primer modelo supervisado de regresión. Además de entrenar el modelo, se trabajan métricas de evaluación que permiten interpretar la magnitud de los errores y la calidad general de las predicciones.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 6" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 6 · Regresión logística y clasificación</strong><br><br>
      <a href="cuadernos/cuaderno-06-regresion-logistica-y-evaluacion-del-modelo.ipynb">Regresión logística y evaluación de clasificadores</a><br><br>
      Este cuaderno introduce un modelo de clasificación y las métricas utilizadas para evaluar clasificadores. Se trabaja con conceptos como matriz de confusión, accuracy, precision, recall y F1-score.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 7" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 7 · Clasificación con KNN</strong><br><br>
      <a href="cuadernos/cuaderno-07-clasificacion-con-knn-k-nearest-neighbors.ipynb">Clasificación con KNN (K-Nearest Neighbors)</a><br><br>
      Se aborda el algoritmo KNN como modelo de clasificación basado en cercanía entre observaciones. El cuaderno permite analizar la importancia de la escala de las variables y el efecto de elegir distintos valores de <code>k</code>.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 8" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 8 · Árboles de decisión y Random Forest</strong><br><br>
      <a href="cuadernos/cuaderno-08-arboles-de-decision-y-random-forest.ipynb">Árboles de decisión y Random Forest</a><br><br>
      Este cuaderno presenta modelos basados en árboles. Se trabaja la diferencia entre un árbol individual y un ensamble como Random Forest, junto con ideas como profundidad, sobreajuste, importancia de variables y comparación de desempeño.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 9A" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 9A · Introducción al clustering</strong><br><br>
      <a href="cuadernos/cuaderno-09a-k-means.ipynb">Introducción al clustering con K-Means</a><br><br>
      Introducción al aprendizaje no supervisado mediante el algoritmo K-Means, utilizando datos preparados para comprender la lógica del algoritmo y la formación de grupos.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 9B" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 9B · K-Means con datos reales</strong><br><br>
      <a href="cuadernos/cuaderno-09b-k-means-pinguinos.ipynb">K-Means en datos reales: cuando el clustering ayuda, pero no alcanza</a><br><br>
      Aplicación de K-Means sobre datos reales para analizar cómo puede ayudar el clustering y reconocer las limitaciones que aparecen cuando los grupos no están claramente separados.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 9C" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 9C · Segmentación de clientes</strong><br><br>
      <a href="cuadernos/cuaderno-09c-k-means-consumidores.ipynb">Segmentación de clientes con K-Means</a><br><br>
      Uso de K-Means en un caso de segmentación de clientes, integrando la preparación de los datos, la identificación de grupos y la interpretación de los segmentos obtenidos.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 10" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 10 · Pipelines y GridSearchCV</strong><br><br>
      <a href="cuadernos/cuaderno-10-pipelines.ipynb">Automatización del flujo de trabajo con Pipelines y GridSearchCV</a><br><br>
      Este cuaderno está orientado a organizar el flujo completo de trabajo mediante pipelines. También introduce la búsqueda de hiperparámetros con GridSearchCV, una herramienta clave para comparar configuraciones de modelos de manera sistemática.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 11" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 11 · Comparación y evaluación de modelos</strong><br><br>
      <a href="cuadernos/cuaderno-11-evaluacion-de-modelos.ipynb">Comparación y evaluación de modelos</a><br><br>
      Se trabaja sobre la comparación entre distintos modelos y métricas. El objetivo es reforzar que no alcanza con entrenar un modelo: también es necesario evaluar resultados, interpretar errores y elegir la alternativa más adecuada para el problema.
    </td>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 12" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 12 · Guardar y recuperar un modelo entrenado</strong><br><br>
      <a href="cuadernos/cuaderno-12-guardar-y-recuperar-modelos.ipynb">Guardar y recuperar un modelo entrenado en scikit-learn</a><br><br>
      En este mini-cuaderno vamos a entrenar rápidamente un modelo de clasificación y luego veremos cómo guardarlo en un archivo para poder reutilizarlo más adelante sin repetir el entrenamiento.
    </td>
  </tr>

  <tr>
    <td valign="top" width="12%" align="center">
      <img src="../../recursos/imagenes/imagen-cuaderno.png" alt="Imagen del Cuaderno 13" width="60">
    </td>
    <td valign="top" width="38%">
      <strong>Cuaderno 13 · Exploración y preparación de un dataset clínico</strong><br><br>
      <a href="cuadernos/cuaderno-13-proyecto-final.ipynb">Exploración y preparación de un dataset clínico</a><br><br>
      Este cuaderno propone trabajar con un dataset de contexto clínico, poniendo el foco en la exploración inicial, la preparación de variables y las decisiones previas al entrenamiento de modelos. Avanza sobre el entrenamiento, la evaluación y la selección de modelos para integrar varias etapas del flujo de trabajo en un caso más completo.
    </td>
    <td valign="top" width="12%"></td>
    <td valign="top" width="38%"></td>
  </tr>
</table>

---

## Versión en PDF

La carpeta de exportaciones PDF fue retirada del repositorio para evitar duplicar archivos pesados. La versión compilada del material podrá descargarse desde Google Drive.

<!-- Agregar aquí el enlace de Google Drive cuando esté disponible. -->

---

## Herramientas principales

A lo largo del recorrido se utilizan principalmente:

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* scikit-learn

También se trabajan conceptos generales de análisis exploratorio de datos, preparación de datasets, evaluación de modelos y comunicación de resultados.

---

## Relación con otros recorridos del repositorio

Este directorio se relaciona especialmente con las secciones **[Análisis de Datos con Python](../analisis-de-datos-python/README.md)** y **[Ciencia de Datos con Python](../../libros/ciencia-de-datos-con-python/README.md)**.

La diferencia principal está en el foco. Mientras que otros recorridos se concentran en la manipulación, inspección, limpieza y análisis exploratorio de datos, esta sección utiliza esas herramientas como base para avanzar hacia modelos de machine learning.

Por eso, algunos temas pueden aparecer nuevamente, como Pandas, visualización o preparación de datos, pero aquí se los retoma desde la perspectiva del modelado predictivo y la evaluación de modelos.

---

## Requisitos sugeridos

Para aprovechar mejor estos cuadernos, conviene tener conocimientos básicos de:

* Sintaxis general de Python
* Listas, diccionarios y funciones
* Uso básico de Pandas
* Lectura e interpretación de tablas
* Nociones iniciales de gráficos y análisis exploratorio

No es necesario tener experiencia previa en machine learning. El recorrido introduce los conceptos principales de manera gradual.

---

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes](../../ACERCA-DE.md)** como apoyo para clases de programación, análisis de datos y Machine Learning con Python.
