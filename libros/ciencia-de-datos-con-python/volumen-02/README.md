# Ciencia de Datos con Python - Vol II

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python\&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)


🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) · 📚 [Ver la colección](../README.md) · 🏠 [Volver al inicio](../../../README.md)

----

<table align="center">
  <tr>
    <td align="center">
      <a href="https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada2.png" alt="Ciencia de Datos con Python - Vol 2">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link">Descargar PDF Volumen II</a></strong>
      <br>
      Primeros pasos con datos
    </td>
  </tr>
</table>


Este directorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo del trabajo con datos usando **Python** y **Pandas**, correspondientes al PDF **[Ciencia de Datos con Python - Vol II](https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link)**.

[Ir al índice de Cuadernos Colab](#listado-de-cuadernos-colab)

---

# Introducción

Después de aprender a cargar, inspeccionar, seleccionar, filtrar, ordenar y limpiar datos, aparece una nueva etapa del trabajo con Python: empezar a hacer preguntas más analíticas. Ya no alcanza con mirar si el dataset está ordenado o si una columna tiene el tipo correcto. Ahora necesitamos observar qué dicen los datos, qué patrones aparecen, qué diferencias existen entre grupos y qué conclusiones podemos sostener con evidencia.

[Este segundo tomo](https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link) continúa el recorrido iniciado en el **[primer volumen de Ciencia de Datos con Python](../volumen-01/README.md)**. Si el primer tomo estuvo centrado en comprender y preparar datos tabulares, este avanza hacia el análisis exploratorio: resumir variables, contar frecuencias, comparar categorías, agrupar datos, visualizar relaciones y comunicar resultados de manera clara.

El contenido de este libro proviene de una serie de cuadernos de trabajo preparados para Google Colab. En el [libro gratis en formato PDF](https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link), esos cuadernos se presentan en formato de texto, para facilitar la lectura continua, la consulta y el estudio. Sin embargo, la experiencia más completa se obtiene al trabajar también con los cuadernos originales en línea: allí es posible ejecutar el código, modificarlo, observar los resultados y experimentar con los ejemplos.

Los cuadernos están disponibles de forma gratuita en este repositorio de GitHub. Si el lector lo desea, puede acceder a ellos, abrirlos en Google Colab y usarlos como material práctico complementario al libro. Esta forma de trabajo sigue siendo especialmente recomendable, porque el análisis de datos se aprende mirando resultados, comparando salidas, cambiando preguntas y volviendo sobre el dataset con más criterio.

## Qué vas a encontrar en este tomo

Este tomo se concentra en las primeras herramientas de análisis exploratorio de datos. A lo largo de los capítulos se trabaja con preguntas iniciales sobre un dataset, resúmenes de variables numéricas, conteos de valores, frecuencias absolutas y relativas, porcentajes, tablas de resumen y comparaciones entre grupos.

También se introducen recursos fundamentales para analizar datos con Pandas, como `value_counts()`, `groupby()`, tablas agregadas, ordenamientos, rankings, comparación de categorías y búsqueda de valores extremos. Estas herramientas permiten dejar de mirar registros aislados y empezar a observar comportamientos generales dentro del conjunto de datos.

Una parte importante del recorrido está dedicada a la visualización. El objetivo no es hacer gráficos decorativos, sino aprender a elegir representaciones útiles para comparar distribuciones, observar relaciones entre variables numéricas, comunicar diferencias entre grupos y acompañar una explicación con evidencia visual.

Hacia el final se trabaja sobre la escritura de conclusiones y la construcción de un informe breve de análisis exploratorio. La idea central es que analizar datos no termina al obtener una tabla o un gráfico: también es necesario interpretar los resultados, expresar los hallazgos con cuidado y reconocer los límites de lo que los datos permiten afirmar.

## Requisitos previos

Para aprovechar este libro conviene haber trabajado previamente con [los contenidos del primer tomo](https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link) o contar con conocimientos equivalentes. En particular, se recomienda conocer:

- nociones básicas de programación en Python;
- uso general de Google Colab o notebooks;
- estructura de un DataFrame de Pandas;
- selección de filas y columnas;
- filtros con condiciones;
- ordenamiento de datos;
- creación y modificación de columnas;
- detección básica de valores faltantes, duplicados y tipos de datos.

No es necesario tener experiencia previa en estadística avanzada o visualización profesional. Los conceptos se presentan de manera progresiva y se apoyan en ejemplos concretos, pero sí se espera cierta familiaridad con la manipulación inicial de datos tabulares.

## A quién está dirigido

Este material está pensado para personas que ya dieron sus primeros pasos con Python y Pandas y quieren empezar a analizar datos con mayor profundidad. Puede ser útil para estudiantes, docentes, programadores, analistas, profesionales que trabajan con planillas o bases de datos, y cualquier persona que necesite transformar datos en preguntas, comparaciones, explicaciones y conclusiones.

El enfoque sigue siendo introductorio, pero busca construir hábitos de análisis sólidos: no quedarse con una única medida, comparar antes de concluir, mirar la distribución de los datos, revisar grupos, detectar valores extremos y comunicar los resultados de manera comprensible.

## Cómo trabajar con este libro y los cuadernos

Cada capítulo [puede leerse directamente en este PDF](https://drive.google.com/file/d/1zC0sUpQ28Chfxj_MJCXJ-yc1a2pP7VFI/view?usp=drive_link), pero fue pensado también como una serie de cuadernos ejecutables. Por eso, la recomendación es acompañar la lectura con la versión online del cuaderno correspondiente siempre que sea posible.

En los cuadernos de Google Colab, conviene ejecutar cada celda, observar la salida y preguntarse qué aporta ese resultado. Muchas veces, una tabla, un conteo o un gráfico no tienen valor por sí solos: se vuelven útiles cuando los conectamos con una pregunta y con una interpretación razonable.

También es recomendable modificar algunos ejemplos: cambiar una columna, probar otro agrupamiento, ordenar de otra manera o comparar una categoría distinta. Ese tipo de exploración ayuda a comprender mejor las herramientas y a desarrollar autonomía para aplicarlas en otros datasets.

Los capítulos fueron diseñados como una secuencia progresiva. Algunas instrucciones aparecen varias veces en contextos distintos, porque en análisis de datos una misma herramienta puede servir para responder preguntas diferentes. Esa repetición controlada permite afianzar procedimientos y, al mismo tiempo, aprender a leer los resultados con más criterio.

## Enfoque del libro

El objetivo principal de este tomo es pasar de la preparación de datos al análisis exploratorio. Esto implica aprender instrucciones nuevas, pero también construir una forma de trabajo: formular preguntas, producir resúmenes, comparar grupos, visualizar relaciones, interpretar resultados y comunicar conclusiones.

A lo largo del recorrido se priorizan tres ideas:

- analizar no es solo calcular, sino interpretar;
- una conclusión necesita apoyarse en datos observables;
- una buena visualización debe ayudar a comprender, no solo a decorar.

Con esa base, el lector queda mejor preparado para avanzar hacia etapas posteriores del trabajo con datos, donde las preguntas se vuelven más complejas y las herramientas permiten construir modelos predictivos.

---

## Listado de Cuadernos Colab

### Bloque 1: Resumir y agrupar datos
* [Capítulo 24 · Primeras preguntas de análisis](cuadernos/capitulo-024-primeras-preguntas-de-analisis.ipynb)
* [Capítulo 25 · Resumir columnas numéricas](cuadernos/capitulo-025-resumir-columnas-numericas.ipynb)
* [Capítulo 26 · Contar valores y analizar frecuencias](cuadernos/capitulo-026-contar-valores-y-analizar-frecuencias.ipynb)
* [Capítulo 27 · Primeras tablas de resumen](cuadernos/capitulo-027-primeras-tablas-de-resumen.ipynb)
* [Capítulo 28 · Agrupar datos con groupby()](cuadernos/capitulo-028-agrupar-datos-con-groupby.ipynb)
* [Capítulo 29 · Agrupaciones múltiples y varios indicadores con groupby()](cuadernos/capitulo-029-agrupaciones-multiples-y-varios-indicadores-con-groupby.ipynb)
* [Capítulo 30 · Comparar categorías](cuadernos/capitulo-030-comparar-categorias.ipynb)
* [Capítulo 31 · Rankings, valores extremos y outliers](cuadernos/capitulo-031-rankings-valores-extremos-y-outliers.ipynb)
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

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes](../../../ACERCA-DE.md)** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos y programación con Python.
