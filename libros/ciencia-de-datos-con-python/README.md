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
**EN ESTE MOMENTO GITHUB TIENE ALGUN PROBLEMA PARA RENDERIZAR LOS CUADERNOS COLAB. SIN EMBARGO, LOS MISMOS ESTÁN CORRECTOS Y PUEDES USARLOS NORMALMENTE EN GOOGLE COLAB.**

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
      <strong><a href="volumen-01/README.md">Volumen I</a></strong>
      <br>
      Primeros pasos con datos
    </td>
    <td align="center" valign="top" width="33%">
      <a href="volumen-02/README.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada2.png" alt="Ciencia de Datos con Python - Volumen II">
      </a>
      <br>
      <strong><a href="volumen-02/README.md">Volumen II</a></strong>
      <br>
      Análisis exploratorio y visualización
    </td>
    <td align="center" valign="top" width="33%">
      <a href="volumen-03/README.md">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada3.png" alt="Ciencia de Datos con Python - Volumen III">
      </a>
      <br>
      <strong><a href="volumen-03/README.md">Volumen III</a></strong>
      <br>
      Fundamentos de Machine Learning
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
* Capítulo 32 · Tablas dinámicas con pivot_table()

### Bloque 2: Visualizar e interpretar resultados

* Capítulo 33 · Análisis temporal básico
* Capítulo 34 · Visualizar distribuciones
* Capítulo 35 · Visualizar comparaciones
* Capítulo 36 · Del cálculo al hallazgo
* Capítulo 37 · Mini análisis exploratorio completo

---

## Estado del material

Esta serie está en construcción.

Los capítulos con enlace ya están publicados en el repositorio. Los capítulos sin enlace forman parte del plan de trabajo y se irán incorporando progresivamente.

El índice puede modificarse a medida que el recorrido avance, especialmente si resulta necesario agregar capítulos intermedios, reorganizar temas o dividir algún contenido para mantener una progresión más clara.

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
