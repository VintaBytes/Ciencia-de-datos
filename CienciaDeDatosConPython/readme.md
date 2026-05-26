# Ciencia de Datos con Python

Este repositorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo del trabajo con datos usando Python y Pandas.

El proyecto está pensado como un material de estudio autónomo, con un enfoque gradual y explicativo. No se limita a presentar instrucciones aisladas, sino que busca construir una forma de pensar el trabajo con datos: observar, seleccionar, transformar, limpiar, validar y, más adelante, analizar e interpretar información.

[Ir al Indice General del repositorio](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/CienciaDeDatosConPython/indice.md)

## Objetivo del proyecto

El objetivo principal es acompañar a estudiantes, desarrolladores y personas interesadas en ciencia de datos en sus primeros pasos con el análisis de datos usando Python.

La serie comienza desde conceptos básicos, como la estructura de un `DataFrame`, y avanza progresivamente hacia tareas más complejas, como selección de datos, filtros, creación de columnas, limpieza de datos, conversión de tipos, trabajo con fechas y validación posterior a la preparación.

El enfoque prioriza la comprensión conceptual antes que la memorización de comandos. Cada herramienta de Pandas se presenta dentro de un contexto de uso, explicando no solo cómo se aplica, sino también por qué puede ser necesaria y qué decisiones implica.

## Enfoque didáctico

Los cuadernos están escritos con una lógica narrativa y progresiva. Cada capítulo retoma brevemente lo trabajado antes y desarrolla un nuevo conjunto de ideas de manera ordenada.

El código se utiliza como herramienta para resolver problemas concretos, no como una colección de ejemplos desconectados. A medida que avanza la serie, el material deja de funcionar como una simple guía de sintaxis y comienza a mostrar un proceso de trabajo más cercano al análisis real de datos.

## Contenido desarrollado hasta el momento

Hasta el momento, la serie cubre una primera gran etapa de trabajo con `DataFrames` y preparación de datos.

### Primer contacto con DataFrames

Los primeros capítulos introducen el uso de Pandas y la estructura de un `DataFrame`. Se trabaja con la idea de filas, columnas, índices, nombres de columnas, dimensiones del dataset y primeras herramientas de inspección.

Se utilizan instrucciones como:

- `head()`
- `tail()`
- `shape`
- `columns`
- `info()`
- `type()`

El objetivo de esta etapa es aprender a observar un dataset antes de modificarlo.

### Selección, filtros y ordenamientos

Luego se avanza hacia la selección de información dentro del `DataFrame`.

Se trabajan temas como:

- selección de columnas;
- selección de filas;
- uso de `loc` e `iloc`;
- filtros con condiciones;
- combinación de condiciones;
- ordenamiento de datos;
- construcción de rankings.

Esta etapa permite pasar de mirar una tabla completa a formular preguntas más específicas sobre los datos.

### Creación, modificación y organización de columnas

La serie continúa con capítulos dedicados a transformar la estructura del `DataFrame`.

Se desarrollan temas como:

- creación de nuevas columnas;
- columnas calculadas;
- columnas con valores constantes;
- columnas creadas a partir de condiciones;
- modificación de columnas existentes;
- limpieza básica de textos;
- renombrado de columnas;
- eliminación de columnas;
- reordenamiento de variables.

El objetivo es mostrar que un dataset no es una estructura fija: puede transformarse para representar mejor el problema de análisis.

### Preparación y limpieza de datos

A partir de una segunda etapa, el proyecto comienza a trabajar de manera más metodológica sobre la preparación de datos.

Se abordan problemas frecuentes en datasets reales:

- qué significa limpiar datos;
- valores faltantes;
- eliminación, imputación y reconstrucción de valores faltantes;
- duplicados;
- limpieza de textos y categorías;
- valores como `UNKNOWN` y `ERROR`;
- conversión de tipos de datos;
- columnas numéricas cargadas como texto;
- fechas y datos temporales;
- creación de columnas de validación;
- limpieza encadenada paso a paso;
- validación posterior a la limpieza.

En esta etapa se trabaja con datasets reales de Kaggle y también con datasets sintéticos pequeños, según convenga para explicar cada problema con claridad.

## Estado actual de la serie

La primera gran etapa del proyecto ya está desarrollada: desde el primer contacto con un `DataFrame` hasta la construcción y validación de una versión preparada de un dataset.

El recorrido culmina con un capítulo de balance:

**Del primer DataFrame al dataset preparado**

Este cierre recupera lo trabajado y ordena las ideas centrales de la etapa: inspeccionar, seleccionar, transformar, limpiar, validar y documentar decisiones.

## Próximos ejes de trabajo

A partir de esta base, los siguientes capítulos avanzarán hacia el análisis de datos propiamente dicho.

Los ejes generales previstos son:

- resumir información;
- calcular indicadores;
- agrupar datos;
- comparar variables;
- construir tablas de resumen;
- visualizar resultados;
- interpretar hallazgos.

La idea será pasar gradualmente de preparar datasets a usarlos para responder preguntas.

## Requisitos

Los cuadernos están pensados para ejecutarse en Google Colab.

Las bibliotecas principales utilizadas son:

- Python
- Pandas
- KaggleHub, para descargar algunos datasets desde Kaggle
- otras bibliotecas que podrán incorporarse más adelante según las necesidades de análisis y visualización

En Google Colab, muchas de estas herramientas ya se encuentran disponibles por defecto.

## Uso del material

Cada capítulo está diseñado como un cuaderno independiente, pero forma parte de una progresión más amplia. Se recomienda recorrerlos en orden, especialmente durante las primeras etapas, porque los conceptos se construyen de manera acumulativa.

El material puede usarse como:

- guía de estudio personal;
- apoyo para cursos introductorios de ciencia de datos;
- base para clases prácticas;
- material complementario para estudiantes que estén comenzando a trabajar con Pandas.

## Filosofía del proyecto

Este proyecto parte de una idea central:

> Trabajar con datos no consiste solamente en ejecutar comandos, sino en construir un proceso razonado para comprender, transformar y analizar información.

Por eso, cada capítulo busca combinar código, explicación conceptual e interpretación de resultados. La meta no es solo aprender Pandas, sino desarrollar criterios para trabajar con datos de manera clara, responsable y progresiva.
```
