# Ciencia de Datos con Python - Vol I

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python\&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)

🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/)     🏠 [Volver al comienzo del repositorio](https://github.com/VintaBytes/Ciencia-de-datos)

----

<table align="center">
  <tr>
    <td align="center">
      <a href="https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada1.png" alt="Ciencia de Datos con Python - Vol 1">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link">PDF Volumen I</a></strong>
      <br>
      Primeros pasos con datos
    </td>
  </tr>
</table>


Este directorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo del trabajo con datos usando **Python** y **Pandas**, correspondientes al PDF **[Ciencia de Datos con Python - Vol I](https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link)**.

[Ir al índice de Cuadernos Colab](#listado-de-cuadernos-colab)

---

# Introducción

Trabajar con datos se volvió una habilidad cada vez más necesaria en contextos muy distintos: educación, investigación, administración, comunicación, comercio, tecnología, salud, gestión pública y muchas otras áreas. En todos esos casos aparecen tablas, registros, archivos, planillas o bases de datos que necesitan ser explorados, ordenados, limpiados e interpretados para poder transformarse en información útil.

Este libro propone una introducción práctica al trabajo con datos usando Python. No parte de la idea de que analizar datos sea simplemente aplicar comandos, sino de una mirada más amplia: antes de calcular, graficar o construir modelos, necesitamos entender qué tenemos delante, cómo está organizado un dataset, qué preguntas podemos hacerle y qué problemas pueden aparecer en los datos reales.

El contenido proviene de una serie de cuadernos de trabajo preparados para Google Colab. En la [versión en PDF](https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link), esos cuadernos se presentan en formato de texto, para facilitar la lectura continua, la consulta y el estudio. Sin embargo, la experiencia más completa se obtiene al trabajar también con los cuadernos originales en línea: allí es posible ejecutar el código, modificarlo, observar los resultados y experimentar con los ejemplos.

Los cuadernos están disponibles de forma gratuita en este mismo repositorio. El lector puede acceder a ellos, abrirlos en Google Colab y usarlos como material práctico complementario al libro. Esta forma de trabajo es especialmente recomendable, porque en programación y análisis de datos se aprende mucho al probar, equivocarse, corregir y volver a ejecutar.

## Qué vas a encontrar en este tomo

Este primer tomo se concentra en los fundamentos del trabajo con datos tabulares en Python. A lo largo de los capítulos se introducen conceptos esenciales como dataset, DataFrame, filas, columnas, variables, observaciones, tipos de datos y valores. Luego se avanza hacia las primeras operaciones de inspección, selección, filtrado, ordenamiento y creación de columnas.

Una parte importante del recorrido está dedicada a la limpieza y preparación de datos. En los datasets reales es frecuente encontrar valores faltantes, duplicados, textos escritos de distintas maneras, tipos de datos incorrectos, fechas mal interpretadas o columnas que necesitan ser reorganizadas. Por eso, el libro no se limita a mostrar instrucciones aisladas: también propone criterios para diagnosticar problemas, decidir estrategias de limpieza y verificar los resultados obtenidos.

Hacia el final del tomo, el objetivo es que el lector pueda pasar de una primera tabla cargada en Python a un dataset más ordenado, comprensible y preparado para etapas posteriores de análisis.

## Requisitos previos

Para aprovechar este contenido no es necesario tener experiencia previa en ciencia de datos, estadística avanzada o machine learning. Sí conviene contar con una base inicial de programación en Python, especialmente:

- uso de variables;
- llamadas a funciones;
- lectura de resultados en pantalla;
- listas y diccionarios a nivel introductorio;
- nociones básicas de condicionales y ciclos;
- familiaridad general con notebooks o disposición para aprender a usarlos.

También resulta útil tener una idea general de qué es una tabla de datos, una fila, una columna o una planilla, aunque estos conceptos se retoman desde el comienzo.

El material utiliza principalmente Python, Pandas y Google Colab. No hace falta instalar un entorno de desarrollo local para seguir los capítulos, ya que los cuadernos pueden ejecutarse desde el navegador a partir de los archivos disponibles en este repositorio.

## A quién está dirigido

Este material está pensado para cualquier persona que necesite empezar a trabajar con datos usando Python. Puede ser útil para estudiantes, docentes, profesionales, analistas, personas que trabajan con planillas, programadores que quieren acercarse al análisis de datos o lectores que se preparan para estudiar ciencia de datos, visualización, inteligencia artificial o machine learning.

El enfoque es introductorio, pero no superficial. Se busca construir una base sólida, con explicaciones claras y ejemplos progresivos, evitando saltar demasiado rápido a herramientas más complejas sin haber desarrollado antes los criterios necesarios para entender y preparar los datos.

## Cómo trabajar con este libro y los cuadernos

Cada capítulo puede leerse directamente [en este PDF](https://drive.google.com/file/d/1a4udSL7svFQUgukpKiqX_eAU3WDCaojL/view?usp=drive_link), pero fue pensado originalmente como un cuaderno ejecutable. Por eso, la recomendación es acompañar la lectura con la versión online del cuaderno correspondiente siempre que sea posible.

En los cuadernos de Google Colab, conviene no limitarse a mirar el código: es preferible ejecutar cada celda, observar la salida, comparar resultados y probar pequeñas modificaciones. En análisis de datos, muchas veces la comprensión aparece al mirar con atención qué devuelve cada instrucción y cómo cambia el DataFrame después de cada operación.

También es importante leer las explicaciones que acompañan al código. En varios momentos, el foco no está solamente en aprender una instrucción de Pandas, sino en entender por qué se usa, qué pregunta ayuda a responder y qué precauciones conviene tener al interpretar el resultado.

Los capítulos fueron diseñados como una secuencia progresiva. Algunos conceptos aparecen primero de manera simple y luego se retoman en situaciones más complejas. Esa repetición controlada forma parte del aprendizaje: permite afianzar herramientas, reconocer patrones y ganar autonomía. El PDF puede servir como guía de lectura y consulta; los cuadernos online, como espacio de práctica, exploración y experimentación.

## Enfoque del libro

El objetivo principal de este tomo es desarrollar una primera alfabetización práctica en datos con Python. Esto implica aprender instrucciones, pero también aprender a mirar un dataset, hacer preguntas, detectar problemas, justificar decisiones y verificar cambios.

A lo largo del recorrido se priorizan tres ideas:

- comprender antes de transformar;
- trabajar paso a paso, verificando cada resultado;
- preparar datos de manera cuidadosa antes de avanzar hacia análisis más complejos.

Con esa base, el lector queda mejor preparado para continuar con temas como análisis exploratorio, visualización, agrupaciones, conclusiones a partir de datos y, más adelante, machine learning.

---

## Listado de Cuadernos Colab

### Primer contacto con datos y DataFrames

* [Capítulo 001 · Primer contacto con el trabajo con datos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo001_Primer_contacto_con_el_trabajo_con_datos.ipynb)
* [Capítulo 002 · Primeras inspecciones de un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo002_Primeras_inspecciones_de_un_DataFrame.ipynb)

### Selección, filtros y ordenamiento

* [Capítulo 003 · Selección de columnas en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo003_Selecci%C3%B3n_de_columnas_en_un_DataFrame.ipynb)
* [Capítulo 004 · Selección de filas en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo004_Selecci%C3%B3n_de_filas_en_un_DataFrame.ipynb)
* [Capítulo 005 · Selección con etiquetas usando `loc`](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo005_Selecci%C3%B3n_con_etiquetas_usando_loc.ipynb)
* [Capítulo 006 · Filtros con condiciones](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo006_Filtros_con_condiciones.ipynb)
* [Capítulo 007 · Combinar condiciones en filtros](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo007_Combinar_condiciones_en_filtros.ipynb)
* [Capítulo 008 · Ordenar datos en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo008_Ordenar_datos_en_un_DataFrame.ipynb)
* [Capítulo 009 · Valores extremos y primeros rankings](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo009_Valores_extremos_y_primeros_rankings.ipynb)

### Creación y organización de columnas

* [Capítulo 010 · Crear nuevas columnas en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo010_Crear_nuevas_columnas_en_un_DataFrame.ipynb)
* [Capítulo 011 · Modificar columnas existentes en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo011_Modificar_columnas_existentes_en_un_DataFrame.ipynb)
* [Capítulo 012 · Organizar columnas en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo012_Organizar_columnas_en_un_DataFrame.ipynb)

### Limpieza de datos

* [Capítulo 013 · Qué significa limpiar datos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo013_Qu%C3%A9_significa_limpiar_datos.ipynb)
* [Capítulo 014 · Valores faltantes](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo014_Valores_faltantes.ipynb)
* [Capítulo 015 · Eliminar, imputar o reconstruir valores faltantes](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo015_Eliminar_imputar_o_reconstruir_valores_faltantes.ipynb)
* [Capítulo 016 · Duplicados en un DataFrame](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo016_Duplicados_en_un_DataFrame.ipynb)
* [Capítulo 017 · Limpieza de textos y categorías](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo017_Limpieza_de_textos_y_categor%C3%ADas.ipynb)
* [Capítulo 018 · Conversión de tipos de datos](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo018_Conversi%C3%B3n_de_tipos_de_datos.ipynb)
* [Capítulo 019 · Fechas y datos temporales](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo019_Fechas_y_datos_temporales.ipynb)
* [Capítulo 020 · Estandarizar nombres y crear nuevas columnas](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo020_Estandarizar_nombres_y_crear_nuevas_columnas.ipynb)
* [Capítulo 021 · Limpieza encadenada paso a paso](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo021_Limpieza_encadenada_paso_a_paso.ipynb)
* [Capítulo 022 · Validación posterior a la limpieza](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo022_Validaci%C3%B3n_posterior_a_la_limpieza.ipynb)
* [Capítulo 023 · Del primer DataFrame al dataset preparado](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/CuadernosColab/CienciaDeDatos_Cap%C3%ADtulo023_Del_primer_DataFrame_al_dataset_preparado.ipynb)


---

## Autor

Material desarrollado por **VintaByte** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos y programación con Python.
