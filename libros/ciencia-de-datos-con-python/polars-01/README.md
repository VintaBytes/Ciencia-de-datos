# Polars para usuarios de Pandas

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)
![Polars](https://img.shields.io/badge/Polars-CD792C?logo=polars&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)

🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) · 📚 [Ver la colección](../README.md) · 🏠 [Volver al inicio](../../../README.md)

---

**Este libro está en desarrollo.** Los capítulos **1 a 11** ya se encuentran desarrollados y cuentan con sus materiales complementarios cuando corresponde. Los capítulos siguientes continuarán incorporándose de manera progresiva.

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/VintaBytes/VintaBytes.github.io/blob/main/images/PortadaPolars1.png" alt="Polars para usuarios de Pandas">
      <br>
      <strong>Polars para usuarios de Pandas<br>
      (<a href="https://drive.google.com/file/d/1M0f31seZbuAPPxjaTSHPc9hJUZZc9LE1/view?usp=drive_link">Versión preliminar del PDF</a>)</strong>
      <br>
      Una introducción progresiva a Polars para lectores<br>
      que ya trabajan con Pandas y análisis de datos en Python.
      <br>
    </td>
  </tr>
</table>

Este directorio reúne el material correspondiente al libro **Polars para usuarios de Pandas**, una propuesta orientada a lectores que ya conocen Pandas y quieren incorporar Polars comprendiendo sus ideas propias, en lugar de limitarse a traducir instrucciones de una biblioteca a otra.

El recorrido comienza con tareas familiares —crear DataFrames, seleccionar columnas, filtrar filas, transformar variables y ordenar datos— y avanza gradualmente hacia conceptos característicos de Polars, como el sistema de expresiones, los esquemas y tipos más estrictos, la ejecución eager y lazy, la optimización de consultas y el procesamiento eficiente de datos tabulares.

Los capítulos del PDF y los cuadernos de Google Colab cumplen funciones complementarias. El libro desarrolla los conceptos y explica las diferencias de enfoque, mientras que los notebooks permiten ejecutar el código, observar resultados concretos y experimentar con las expresiones.

[Ir al listado de Cuadernos Colab](#listado-de-cuadernos-colab)

---

# Introducción

Pandas ocupa un lugar central en el ecosistema de análisis de datos con Python y ha sido también una de las herramientas principales de los volúmenes anteriores de **Ciencia de Datos con Python**. Quien haya trabajado con ella ya conoce buena parte de las tareas que volverán a aparecer aquí: cargar datos, inspeccionar DataFrames, seleccionar columnas, filtrar registros, limpiar información, agrupar observaciones y combinar tablas.

Polars permite resolver muchas de esas mismas tareas, pero fue diseñado alrededor de decisiones diferentes. No utiliza un índice de filas equivalente al de Pandas, mantiene una disciplina de tipos más estricta y coloca las expresiones en el centro de la API. También puede construir consultas antes de ejecutarlas, optimizarlas y aprovechar de manera natural varios núcleos del procesador.

Por eso este libro no está planteado como una tabla de equivalencias. Durante los primeros capítulos las comparaciones con Pandas servirán como puente, pero el objetivo es que progresivamente podamos leer y escribir Polars en sus propios términos.

El recorrido comienza con operaciones sencillas y conocidas, para luego entrar en preparación y limpieza de datos. Más adelante se incorporarán resúmenes, agrupaciones, joins y cambios de forma, y finalmente se profundizará en el sistema de expresiones, la ejecución lazy y las optimizaciones que distinguen especialmente a Polars.

El enfoque busca también evitar afirmaciones simplistas sobre rendimiento. Polars puede resultar especialmente atractivo con conjuntos de datos grandes, consultas que se benefician de optimización y flujos de trabajo orientados a expresiones, pero Pandas continúa siendo una herramienta muy valiosa y ampliamente integrada con el resto del ecosistema de Python. El objetivo final es ampliar la caja de herramientas y aprender a elegir según el problema.

## Qué vas a encontrar en este libro

Los primeros capítulos presentan el modelo básico de Polars y las diferencias más importantes con Pandas. Se trabaja con `select()`, `filter()`, `with_columns()`, condiciones booleanas, transformaciones con `when()`, ordenamientos y rankings, utilizando datasets pequeños que permiten observar con claridad el efecto de cada operación.

A partir del capítulo 10 comienza una segunda etapa dedicada a la calidad de los datos. El esquema, los tipos, las conversiones con `cast()`, los valores faltantes y la diferencia entre `null` y `NaN` pasan a formar parte central del trabajo. Los capítulos siguientes continuarán con limpieza de texto, duplicados, fechas y una preparación completa del dataset.

Más adelante el recorrido avanzará hacia resúmenes y agrupaciones, combinación de DataFrames y cambio de forma de los datos. La parte final estará dedicada a comprender de manera más profunda el sistema de expresiones, la diferencia entre ejecución eager y lazy y algunas de las optimizaciones que Polars puede aplicar antes de ejecutar una consulta.

## Requisitos previos

Para aprovechar el material conviene contar con una base de Python y haber trabajado previamente con Pandas o con otra biblioteca de DataFrames. En particular, resulta útil conocer operaciones básicas de selección, filtrado, creación de columnas, valores faltantes, agrupaciones y lectura de archivos CSV.

No se requiere experiencia previa con Polars, Rust, Apache Arrow ni motores de consultas. Los conceptos específicos de la biblioteca se introducen progresivamente a medida que se vuelven necesarios.

## A quién está dirigido

El libro está pensado principalmente para estudiantes, docentes, programadores, analistas y personas que ya utilizan Pandas y quieren aprender Polars de una manera razonada. También puede resultar útil para quienes conocen el trabajo con datos tabulares y desean comprender qué cambia cuando una biblioteca adopta expresiones, tipos más estrictos y ejecución lazy como parte central de su diseño.

El enfoque es introductorio, pero busca ir más allá de la sintaxis. La intención es comprender qué representa cada operación y por qué determinadas formas de escribir una consulta son más naturales dentro del modelo de Polars.

## Cómo trabajar con el libro y los cuadernos

Los capítulos pueden leerse directamente en el PDF, pero muchos cuentan también con un cuaderno complementario. En esos notebooks conviene ejecutar cada celda y observar cuidadosamente las salidas, ya que buena parte del aprendizaje consiste en relacionar una expresión con el resultado que produce dentro de un contexto concreto.

Los cuadernos no están pensados como hojas de ejercicios. Funcionan como recorridos guiados que acompañan la explicación teórica, muestran resultados reales y permiten modificar condiciones, columnas o tipos para observar cómo cambia el DataFrame.

---

## Listado de Cuadernos Colab

> Los enlaces se completarán a medida que los cuadernos se publiquen en el repositorio.

### Parte I · De Pandas a Polars

* Capítulo 1 · ¿Por qué Polars? *(sin cuaderno independiente)*
* Capítulo 2 · Nuestro primer DataFrame con Polars
* Capítulo 3 · Un DataFrame parecido, pero no igual *(sin cuaderno independiente)*
* Capítulo 4 · Seleccionar columnas con `select()`
* Capítulo 5 · Filtrar filas con `filter()`
* Capítulo 6 · Combinar condiciones
* Capítulo 7 · Crear y transformar columnas con `with_columns()`
* Capítulo 8 · Transformaciones condicionales con `when()`, `then()` y `otherwise()`
* Capítulo 9 · Ordenar, buscar extremos y construir rankings

### Parte II · Preparar y limpiar datos

* Capítulo 10 · Tipos de datos y esquema
* Capítulo 11 · Valores faltantes: `null` no es `NaN`
* Capítulo 12 · Limpiar textos y categorías *(en desarrollo)*
* Capítulo 13 · Duplicados, valores únicos y consistencia *(en desarrollo)*
* Capítulo 14 · Fechas y datos temporales *(en desarrollo)*
* Capítulo 15 · Una limpieza completa con Polars *(en desarrollo)*

---

## Índice de capítulos

### Parte I · De Pandas a Polars

* Capítulo 1 · ¿Por qué Polars?
* Capítulo 2 · Nuestro primer DataFrame con Polars
* Capítulo 3 · Un DataFrame parecido, pero no igual
* Capítulo 4 · Seleccionar columnas con `select()`
* Capítulo 5 · Filtrar filas con `filter()`
* Capítulo 6 · Combinar condiciones
* Capítulo 7 · Crear y transformar columnas con `with_columns()`
* Capítulo 8 · Transformaciones condicionales con `when()`, `then()` y `otherwise()`
* Capítulo 9 · Ordenar, buscar extremos y construir rankings

### Parte II · Preparar y limpiar datos

* Capítulo 10 · Tipos de datos y esquema
* Capítulo 11 · Valores faltantes: `null` no es `NaN`
* Capítulo 12 · Limpiar textos y categorías
* Capítulo 13 · Duplicados, valores únicos y consistencia
* Capítulo 14 · Fechas y datos temporales
* Capítulo 15 · Una limpieza completa con Polars

### Parte III · Resumir, agrupar y combinar

* Capítulo 16 · Resumir datos con expresiones *(en desarrollo)*
* Capítulo 17 · Agrupar datos con `group_by()` *(en desarrollo)*
* Capítulo 18 · Agrupaciones múltiples y análisis por categorías *(en desarrollo)*
* Capítulo 19 · Combinar DataFrames *(en desarrollo)*
* Capítulo 20 · Cambiar la forma de los datos *(en desarrollo)*

### Parte IV · Pensar como Polars

* Capítulo 21 · Entender el sistema de expresiones *(en desarrollo)*
* Capítulo 22 · Eager y Lazy: dos maneras de ejecutar *(en desarrollo)*
* Capítulo 23 · Cómo Polars optimiza nuestro trabajo *(en desarrollo)*

### Parte V · Integrar y elegir

* Capítulo 24 · Pandas o Polars: resolver un problema completo *(en desarrollo)*

---

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes]()** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos, Machine Learning y programación con Python.
