# Ciencia de Datos con Python

### Serie de cuadernos Colab

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python\&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)

🏠 [Volver al inicio del repositorio](../../README.md) · 🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/)

----

Este directorio contiene una serie de cuadernos Colab sobre **Ciencia de Datos con Python**, pensada como un recorrido progresivo, narrativo y autocontenido.

A diferencia de otros materiales organizados por clases, esta serie está estructurada como capítulos de estudio. Cada cuaderno desarrolla un tema específico y busca acompañar al lector paso a paso, combinando explicación conceptual, código Python, salidas comentadas e interpretación de resultados.

El recorrido comienza con los primeros contactos con datos tabulares y avanza gradualmente hacia tareas habituales del trabajo con datos: inspección de `DataFrame`, selección de filas y columnas, filtros, ordenamiento, creación de nuevas columnas, limpieza, tratamiento de valores faltantes, conversión de tipos y validación posterior a la preparación del dataset.

Este material forma parte del repositorio general **Ciencia de Datos con Python** y se encuentra actualmente en desarrollo.

## Volúmenes de la colección

<table align="center">
  <tr>
    <td align="center" valign="top" width="33%">
      <a href="volumen-01/README.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada1.png" alt="Ciencia de Datos con Python - Volumen I">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link">Descargar PDF del Volumen I</a></strong>
      <br>
      Introducción práctica al trabajo con datos usando Python.
      <br>
      <a href="volumen-01/README.md">Ver cuadernos Colab del libro.</a>
    </td>
    <td align="center" valign="top" width="33%">
      <a href="volumen-02/README.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada2.png" alt="Ciencia de Datos con Python - Volumen II">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link">Descargar PDF del Volumen II</a></strong>
      <br>
      Análisis exploratorio y visualización de datos con Python
      <br>
      <a href="volumen-02/README.md">Ver cuadernos Colab del libro.</a>
    </td>
    <td align="center" valign="top" width="33%">
      <a href="volumen-03/README.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada3.png" alt="Ciencia de Datos con Python - Volumen III">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1rGDPSz8Ggy9xMjGUS_Vynr4_rzejMfdt/view?usp=drive_link">Descargar PDF del Volumen III</a></strong>
      <br>
      Fundamentos de Machine Learning: construir modelos capaces de aprender patrones a partir de datos.
      <br>
      <a href="volumen-03/README.md">Ver cuadernos Colab del libro.</a>
    </td>
  </tr>
</table>

---

## Sobre este recorrido

Los cuadernos están pensados para ser abiertos y ejecutados en **Google Colab**.

El enfoque está dirigido a personas que ya conocen los fundamentos de Python y quieren comenzar a trabajar con datos usando Pandas. No se asume experiencia previa en ciencia de datos ni en análisis exploratorio.

La propuesta prioriza una progresión cuidadosa: cada capítulo introduce pocas ideas nuevas, las desarrolla con ejemplos concretos y las conecta con lo trabajado anteriormente. El objetivo no es solo mostrar instrucciones de Pandas, sino construir una forma de pensar el trabajo con datos.

---

# Parte I - Fundamentos de Pandas
## Índice de capítulos

### Primer contacto con datos y DataFrames

* [Capítulo 001 · Primer contacto con el trabajo con datos](volumen-01/cuadernos/capitulo-001-primer-contacto-con-el-trabajo-con-datos.ipynb)
* [Capítulo 002 · Primeras inspecciones de un DataFrame](volumen-01/cuadernos/capitulo-002-primeras-inspecciones-de-un-dataframe.ipynb)

### Selección, filtros y ordenamiento

* [Capítulo 003 · Selección de columnas en un DataFrame](volumen-01/cuadernos/capitulo-003-seleccion-de-columnas-en-un-dataframe.ipynb)
* [Capítulo 004 · Selección de filas en un DataFrame](volumen-01/cuadernos/capitulo-004-seleccion-de-filas-en-un-dataframe.ipynb)
* [Capítulo 005 · Selección con etiquetas usando `loc`](volumen-01/cuadernos/capitulo-005-seleccion-con-etiquetas-usando-loc.ipynb)
* [Capítulo 006 · Filtros con condiciones](volumen-01/cuadernos/capitulo-006-filtros-con-condiciones.ipynb)
* [Capítulo 007 · Combinar condiciones en filtros](volumen-01/cuadernos/capitulo-007-combinar-condiciones-en-filtros.ipynb)
* [Capítulo 008 · Ordenar datos en un DataFrame](volumen-01/cuadernos/capitulo-008-ordenar-datos-en-un-dataframe.ipynb)
* [Capítulo 009 · Valores extremos y primeros rankings](volumen-01/cuadernos/capitulo-009-valores-extremos-y-primeros-rankings.ipynb)

### Creación y organización de columnas

* [Capítulo 010 · Crear nuevas columnas en un DataFrame](volumen-01/cuadernos/capitulo-010-crear-nuevas-columnas-en-un-dataframe.ipynb)
* [Capítulo 011 · Modificar columnas existentes en un DataFrame](volumen-01/cuadernos/capitulo-011-modificar-columnas-existentes-en-un-dataframe.ipynb)
* [Capítulo 012 · Organizar columnas en un DataFrame](volumen-01/cuadernos/capitulo-012-organizar-columnas-en-un-dataframe.ipynb)

### Limpieza de datos

* [Capítulo 013 · Qué significa limpiar datos](volumen-01/cuadernos/capitulo-013-que-significa-limpiar-datos.ipynb)
* [Capítulo 014 · Valores faltantes](volumen-01/cuadernos/capitulo-014-valores-faltantes.ipynb)
* [Capítulo 015 · Eliminar, imputar o reconstruir valores faltantes](volumen-01/cuadernos/capitulo-015-eliminar-imputar-o-reconstruir-valores-faltantes.ipynb)
* [Capítulo 016 · Duplicados en un DataFrame](volumen-01/cuadernos/capitulo-016-duplicados-en-un-dataframe.ipynb)
* [Capítulo 017 · Limpieza de textos y categorías](volumen-01/cuadernos/capitulo-017-limpieza-de-textos-y-categorias.ipynb)
* [Capítulo 018 · Conversión de tipos de datos](volumen-01/cuadernos/capitulo-018-conversion-de-tipos-de-datos.ipynb)
* [Capítulo 019 · Fechas y datos temporales](volumen-01/cuadernos/capitulo-019-fechas-y-datos-temporales.ipynb)
* [Capítulo 020 · Estandarizar nombres y crear nuevas columnas](volumen-01/cuadernos/capitulo-020-estandarizar-nombres-y-crear-nuevas-columnas.ipynb)
* [Capítulo 021 · Limpieza encadenada paso a paso](volumen-01/cuadernos/capitulo-021-limpieza-encadenada-paso-a-paso.ipynb)
* [Capítulo 022 · Validación posterior a la limpieza](volumen-01/cuadernos/capitulo-022-validacion-posterior-a-la-limpieza.ipynb)
* [Capítulo 023 · Del primer DataFrame al dataset preparado](volumen-01/cuadernos/capitulo-023-del-primer-dataframe-al-dataset-preparado.ipynb)

---

# Parte II - Análisis exploratorio y resumen de datos
## Índice de capítulos

### Bloque 1: Resumir y agrupar datos
* [Capítulo 24 · Primeras preguntas de análisis](volumen-02/cuadernos/capitulo-024-primeras-preguntas-de-analisis.ipynb)
* [Capítulo 25 · Resumir columnas numéricas](volumen-02/cuadernos/capitulo-025-resumir-columnas-numericas.ipynb)
* [Capítulo 26 · Contar valores y analizar frecuencias](volumen-02/cuadernos/capitulo-026-contar-valores-y-analizar-frecuencias.ipynb)
* [Capítulo 27 · Primeras tablas de resumen](volumen-02/cuadernos/capitulo-027-primeras-tablas-de-resumen.ipynb)
* [Capítulo 28 · Agrupar datos con groupby()](volumen-02/cuadernos/capitulo-028-agrupar-datos-con-groupby.ipynb)
* [Capítulo 29 · Agrupaciones múltiples y varios indicadores con groupby()](volumen-02/cuadernos/capitulo-029-agrupaciones-multiples-y-varios-indicadores-con-groupby.ipynb)
* [Capítulo 30 · Comparar categorías](volumen-02/cuadernos/capitulo-030-comparar-categorias.ipynb)
* [Capítulo 31 · Rankings, valores extremos y outliers](volumen-02/cuadernos/capitulo-031-rankings-valores-extremos-y-outliers.ipynb)
* [Capítulo 32 · Organizar resúmenes con tablas dinámicas](cuadernos/CienciaDeDatos_Cap%C3%ADtulo032_Organizar_res%C3%BAmenes_con_tablas_din%C3%A1micas.ipynb)

### Bloque 2: Visualizar e interpretar resultados (En construcción)

* [Capítulo 33 · Análisis temporal básico](cuadernos/CienciaDeDatos_Cap%C3%ADtulo033_An%C3%A1lisis_temporal_b%C3%A1sico.ipynb)
* [Capítulo 34 · Visualizar distribuciones](cuadernos/CienciaDeDatos_Cap%C3%ADtulo034_Visualizar_distribuciones.ipynb)
* [Capítulo 35 · Visualizar distribuciones por grupos](cuadernos/CienciaDeDatos_Cap%C3%ADtulo035_Comparar_distribuciones_por_grupos.ipynb)
* [Capítulo 36 · Visualizar relaciones entre variables numéricas](cuadernos/CienciaDeDatos_Cap%C3%ADtulo036_Visualizar_relaciones_entre_variables_num%C3%A9ricas.ipynb)
* [Capítulo 37 · Comunicar resultados con visualizaciones claras](cuadernos/CienciaDeDatos_Cap%C3%ADtulo037_Comunicar_resultados_con_visualizaciones_claras.ipynb)
* [Capítulo 38 · Integrar un análisis exploratorio completo](cuadernos/CienciaDeDatos_Cap%C3%ADtulo038_Integrar_un_an%C3%A1lisis_exploratorio_completo.ipynb)
* [Capítulo 39 · Escribir conclusiones a partir de los datos](cuadernos/CienciaDeDatos_Cap%C3%ADtulo039_Escribir_conclusiones_a_partir_de_los_datos.ipynb)
* [Capítulo 40 · Armar un informe breve de análisis exploratorio](cuadernos/CienciaDeDatos_Cap%C3%ADtulo040_Armar_un_informe_breve_de_an%C3%A1lisis_exploratorio.ipynb)
* [capítulo 41 · Cerrar el análisis exploratorio](cuadernos/CienciaDeDatos_Cap%C3%ADtulo041_Cerrar_el_an%C3%A1lisis_exploratorio.ipynb)

---

# Parte III - Machine Learning
#### (Esta parte está en construcción, y el contenido puede variar)

## Índice de capítulos

### Parte I · Comprender qué es Machine Learning

* Capítulo 1 · ¿Qué es Machine Learning?
* Capítulo 2 · Problemas, datos y tipos de aprendizaje
* Capítulo 3 · El flujo general de un proyecto de Machine Learning

### Parte II · Preparar datos para aprender

* Capítulo 4 · Variables de entrada y variable objetivo
* Capítulo 5 · Entrenamiento, prueba y datos no vistos
* Capítulo 6 · Limpieza y transformación de datos

### Parte III · Primeros modelos de clasificación

* Capítulo 7 · Clasificación: predecir categorías
* Capítulo 8 · K-Nearest Neighbors
* Capítulo 9 · Regresión Logística
* Capítulo 10 · Árboles de Decisión

### Parte IV · Evaluar modelos de clasificación

* Capítulo 11 · Accuracy y matriz de confusión
* Capítulo 12 · Precision, recall y F1-score
* Capítulo 13 · Probabilidades, umbrales, ROC y AUC

### Parte V · Modelos de regresión

* Capítulo 14 · Regresión: predecir valores numéricos
* Capítulo 15 · Regresión Lineal
* Capítulo 16 · Métricas para regresión

### Parte VI · Generalización, validación y mejora

* Capítulo 17 · Sobreajuste y subajuste
* Capítulo 18 · Validación cruzada
* Capítulo 19 · Hiperparámetros y búsqueda de mejores modelos

### Parte VII · Modelos más potentes

* Capítulo 20 · Random Forest
* Capítulo 21 · Gradient Boosting
* Capítulo 22 · Support Vector Machines
* Capítulo 23 · Naive Bayes

### Parte VIII · Aprendizaje no supervisado

* Capítulo 24 · Aprender sin etiquetas
* Capítulo 25 · Clustering con K-Means
* Capítulo 26 · Reducción de dimensionalidad con PCA
* Capítulo 27 · Interpretar modelos
* Capítulo 28 · Sesgos, datos y decisiones
* Capítulo 29 · Errores comunes al construir modelos
* Capítulo 30 · Comunicar resultados de Machine Learning

### Parte X · Cierre y próximos caminos

* Capítulo 31 · Cómo seguir aprendiendo Machine Learning



---

## Herramientas principales

A lo largo del recorrido se utilizan principalmente:

* Python
* Google Colab
* Pandas
* NumPy

Más adelante pueden incorporarse otras herramientas del ecosistema de ciencia de datos, especialmente para visualización, análisis exploratorio y preparación de datasets.

---

## Relación con otros recorridos del repositorio

Este directorio se relaciona con las secciones **[Análisis de Datos con Python](../../cursos/analisis-de-datos-python/README.md)** y **[Machine Learning con Python](../../cursos/machine-learning-python/README.md)**, pero tiene un enfoque propio.

Mientras que **[Análisis de Datos con Python](../../cursos/analisis-de-datos-python/README.md)** conserva la estructura de un curso organizado por clases, esta serie está pensada como un recorrido narrativo por capítulos.

A su vez, **[Machine Learning con Python](../../cursos/machine-learning-python/README.md)** retoma muchas de estas herramientas como base para avanzar hacia modelos predictivos, evaluación de modelos y aprendizaje automático.

Por eso, algunos temas pueden aparecer en más de una sección, pero con distinta profundidad, finalidad y contexto de uso.

---

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes](../../ACERCA-DE.md)** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos y programación con Python.
