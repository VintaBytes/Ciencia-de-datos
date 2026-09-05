# Ciencia de Datos con Python - Vol V

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)


🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) · 📚 [Ver la colección](../README.md) · 🏠 [Volver al inicio](../../../README.md)

----
**Este libro está en desarrollo**. El **04/09/2026** se agregó el **Capítulo 7 · Backpropagation: aprender desde el error**. Pronto estará disponible el capítulo siguiente.

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada5.png" alt="Ciencia de Datos con Python - Vol 5">
      <br>
      <strong>Ciencia de Datos con Python - Volumen V <br>
      (<a href="https://drive.google.com/file/d/1o0cf42pVgXVXWOwSSzM64_7XsFRhgadP/view?usp=drive_link">Versión preliminar del PDF</a>)</strong>
      <br>
      Introducción al Deep Learning:<br>
      redes neuronales, entrenamiento, visión artificial,<br>
      secuencias, atención y modelos modernos.
      <br>
    </td>
  </tr>
</table>


Este directorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo de **Deep Learning** usando **Python**, **TensorFlow** y **Keras**, correspondientes al PDF **Ciencia de Datos con Python - Vol V**, actualmente en desarrollo.

[Ir al listado de Cuadernos Colab](#listado-de-cuadernos-colab)

---

# Introducción

Después de aprender a preparar datos, construir modelos de Machine Learning, evaluar su rendimiento, controlar el sobreajuste, ajustar hiperparámetros, comparar algoritmos e interpretar resultados, aparece una nueva etapa en el recorrido: trabajar con modelos capaces de aprender representaciones cada vez más complejas directamente a partir de los datos.

Este quinto tomo de **Ciencia de Datos con Python** continúa el recorrido iniciado [en los volúmenes anteriores](../README.md). En los tomos dedicados a Machine Learning estudiamos cómo un algoritmo puede aprender relaciones entre variables de entrada y una variable objetivo, cómo evaluar ese aprendizaje y cómo evitar conclusiones engañosas. Ahora avanzaremos hacia **Deep Learning**, un área del Machine Learning basada principalmente en redes neuronales con múltiples capas de procesamiento.

El cambio no consiste solamente en utilizar modelos más grandes. También cambia la manera en que pensamos la representación de la información. En muchos problemas tradicionales de Machine Learning dedicamos una parte importante del trabajo a decidir qué características utilizar como entrada. En Deep Learning, una red puede aprender progresivamente representaciones útiles a partir de datos como imágenes, texto, audio o secuencias.

Una imagen, por ejemplo, comienza siendo una colección de valores numéricos asociados con píxeles. Una red neuronal puede aprender transformaciones sucesivas que permitan detectar patrones simples, combinarlos y construir representaciones cada vez más útiles para distinguir objetos. De manera semejante, una secuencia de palabras puede convertirse en representaciones numéricas que permitan reconocer relaciones, contexto y estructuras que no aparecen explícitamente en los datos originales.

Para comprender cómo ocurre ese proceso comenzaremos desde la unidad más sencilla: la **neurona artificial**. Analizaremos entradas, pesos, bias y funciones de activación, y veremos cómo varias neuronas pueden organizarse en capas para formar una red. A partir de allí estudiaremos cómo una red produce una predicción, cómo se mide el error y cómo ese error puede utilizarse para modificar miles o millones de parámetros.

Conceptos como función de pérdida, descenso por gradiente y backpropagation permitirán comprender qué significa realmente que una red neuronal "aprenda". No se presentarán como mecanismos mágicos ocultos dentro de una biblioteca, sino como partes de un proceso que podremos interpretar paso a paso.

Una vez construida esa base, comenzaremos a trabajar con problemas concretos. El reconocimiento de dígitos será uno de nuestros primeros ejemplos porque permite observar de manera clara cómo una red transforma píxeles en una predicción. Más adelante estudiaremos redes convolucionales, diseñadas para aprovechar la estructura espacial de las imágenes, y utilizaremos datasets como MNIST, Fashion-MNIST y CIFAR-10.

También veremos cómo mejorar estos modelos mediante técnicas como data augmentation y transfer learning. En lugar de entrenar siempre una red completamente desde cero, aprenderemos a reutilizar modelos previamente entrenados y adaptarlos a nuevos problemas, una estrategia extremadamente importante en el Deep Learning actual.

El recorrido continuará luego hacia texto y secuencias. Analizaremos cómo representar información textual, cómo abordar problemas de clasificación y por qué las secuencias presentan dificultades diferentes de los datos tabulares o las imágenes. Esto nos llevará a redes recurrentes y, posteriormente, a los mecanismos de atención y a los transformers.

Estos últimos temas permiten conectar los fundamentos del libro con muchos de los modelos actuales utilizados en procesamiento de lenguaje, visión artificial y sistemas generativos. El objetivo no será estudiar exhaustivamente cada arquitectura moderna, sino comprender las ideas fundamentales que permiten interpretar cómo funcionan y por qué representan una evolución respecto de modelos anteriores.

El contenido de este libro incluye una serie de cuadernos de trabajo preparados para Google Colab. En el libro en formato PDF los temas se presentan como texto organizado para facilitar la lectura continua, la consulta y el estudio. Los cuadernos permiten complementar ese recorrido ejecutando código, modificando arquitecturas, observando resultados, comparando configuraciones y experimentando con distintos datasets.

Libro y cuadernos fueron pensados como dos partes del mismo recorrido. El texto desarrolla las ideas, explica por qué aparecen determinados problemas y construye los conceptos necesarios para comprender las decisiones que tomamos. Los cuadernos permiten llevar esas ideas a la práctica y observar su comportamiento real.

## Qué vas a encontrar en este tomo

Este volumen comienza construyendo las redes neuronales desde sus componentes más básicos. Primero analizaremos qué distingue al Deep Learning de otras formas de Machine Learning y por qué resulta especialmente útil cuando trabajamos con datos complejos como imágenes, texto o secuencias.

Luego estudiaremos la neurona artificial. Veremos cómo combina variables de entrada mediante pesos y bias, cómo produce una salida y qué relación existe entre esta estructura y modelos que ya conocemos, como la regresión lineal y la regresión logística.

A partir de una neurona construiremos redes completas. Aparecerán las capas de entrada, las capas ocultas y las capas de salida, junto con conceptos como profundidad, ancho, arquitectura y parámetros entrenables. También veremos cómo las conexiones entre neuronas pueden expresarse mediante operaciones matriciales, una representación que permite realizar eficientemente miles de cálculos simultáneos.

Las funciones de activación introducirán una pieza esencial del Deep Learning. Estudiaremos por qué una sucesión de transformaciones lineales no alcanza para construir modelos verdaderamente profundos y analizaremos funciones como ReLU, sigmoid, tanh y softmax. Veremos además que la activación de salida debe elegirse de acuerdo con el problema: regresión, clasificación binaria, clasificación multiclase o clasificación multietiqueta.

Después comenzaremos a estudiar el proceso de aprendizaje. Una red inicialmente posee parámetros que todavía no representan conocimiento útil. Para modificarlos necesitamos medir sus errores mediante una función de pérdida y determinar cómo deberían cambiar los pesos para reducirlos. Esto nos llevará al descenso por gradiente y a backpropagation.

También analizaremos conceptos prácticos fundamentales del entrenamiento: épocas, batches, learning rate, optimizadores, datos de entrenamiento y validación. Veremos que entrenar durante más tiempo o utilizar una red más grande no garantiza mejores resultados, y volveremos a encontrar problemas ya conocidos en Machine Learning, como el sobreajuste.

Con estas bases construiremos nuestras primeras redes completas y comenzaremos a trabajar con imágenes. Analizaremos cómo representa una computadora una imagen y cómo podemos utilizar los valores de sus píxeles como datos de entrada. El reconocimiento de dígitos manuscritos con MNIST servirá como primer problema de visión artificial.

Ese ejemplo permitirá introducir posteriormente las **redes neuronales convolucionales**, o CNN. Estudiaremos convoluciones, filtros, mapas de características y pooling, y veremos por qué este tipo de arquitectura aprovecha mejor la estructura espacial de una imagen que una red completamente densa.

Después aplicaremos estas ideas a conjuntos de datos progresivamente más complejos, como Fashion-MNIST y CIFAR-10. La intención no será solamente mejorar una métrica, sino observar cómo aumenta la dificultad cuando las imágenes contienen más variedad, colores, fondos y objetos visualmente semejantes.

También estudiaremos técnicas utilizadas para mejorar modelos de visión. Data augmentation permitirá generar variaciones de las imágenes de entrenamiento y reducir la dependencia de ejemplos particulares. Transfer learning nos permitirá utilizar redes previamente entrenadas y adaptar sus representaciones a nuevos problemas, incluso cuando disponemos de una cantidad limitada de datos.

Más adelante el libro se extenderá hacia texto y secuencias. Veremos cómo convertir palabras y documentos en datos que una red pueda procesar, cómo abordar problemas de clasificación de textos y qué significa que el orden de los elementos sea relevante.

Esto permitirá introducir las redes recurrentes y algunas de sus variantes, como LSTM y GRU, desde una perspectiva conceptual. El objetivo será comprender por qué surgieron, qué problema intentan resolver y cuáles son sus limitaciones.

A partir de esas dificultades llegaremos al mecanismo de atención. Esta idea modificó profundamente la manera de procesar secuencias y constituye uno de los fundamentos de los transformers. Estudiaremos sus principios antes de observar cómo estos modelos permiten relacionar diferentes partes de una entrada sin depender exclusivamente de un procesamiento secuencial.

Finalmente, nos acercaremos al ecosistema actual de modelos preentrenados. Veremos qué significa utilizar un modelo ya entrenado, qué diferencia existe entre inferencia y ajuste, qué lugar ocupa el fine-tuning y por qué repositorios y herramientas como Hugging Face se han vuelto importantes para trabajar con modelos modernos.

El cierre del libro volverá sobre una idea que atravesó toda la serie: un modelo no debe evaluarse solamente por producir una predicción. También debemos analizar sus errores, interpretar su confianza, reconocer datos diferentes de aquellos utilizados durante el entrenamiento, considerar sesgos y comprender las limitaciones del sistema.

Deep Learning amplía enormemente las posibilidades del Machine Learning, pero no elimina la necesidad de trabajar con criterio. Cuanto más poderoso es un modelo, más importante resulta comprender qué datos utiliza, qué aprendió, cómo fue evaluado y en qué condiciones podemos confiar en sus resultados.

## Requisitos previos

Para aprovechar este libro conviene haber trabajado previamente con los contenidos de **[los tomos anteriores de Ciencia de Datos con Python](../README.md)** o contar con conocimientos equivalentes.

En particular, se recomienda conocer:

* nociones de programación en Python;
* uso general de Google Colab o notebooks;
* trabajo básico con NumPy y Pandas;
* arrays, vectores y matrices a nivel introductorio;
* lectura e interpretación de gráficos;
* preparación básica de datasets;
* separación entre variables de entrada y variable objetivo;
* división entre datos de entrenamiento, validación y prueba;
* conceptos básicos de clasificación y regresión;
* entrenamiento y evaluación de modelos de Machine Learning;
* métricas habituales de clasificación y regresión;
* conceptos de sobreajuste y subajuste;
* hiperparámetros y validación;
* importancia de evitar fuga de datos.

Este tomo parte de la base conceptual construida en los volúmenes dedicados a Machine Learning. No se requiere experiencia previa con redes neuronales ni con TensorFlow o Keras: esas herramientas se introducirán progresivamente a medida que sean necesarias.

Tampoco se requiere un dominio avanzado de matemática. Sin embargo, Deep Learning utiliza algunas ideas matemáticas que conviene comprender para evitar que el entrenamiento de una red aparezca como una caja negra.

A lo largo del libro utilizaremos vectores, matrices, sumas ponderadas, funciones, derivadas y gradientes cuando sean necesarios para explicar cómo funciona un modelo. Cada concepto se introducirá conectado con un problema concreto y con una interpretación computacional.

El objetivo no es desarrollar un curso de cálculo o álgebra lineal independiente, sino utilizar la matemática como una herramienta para comprender qué está haciendo la red.

## A quién está dirigido

Este material está pensado para personas que ya poseen una base de Python, análisis de datos y Machine Learning y desean comenzar a trabajar con Deep Learning desde sus fundamentos.

Puede ser útil para estudiantes, docentes, programadores, analistas, profesionales que trabajan con datos, personas que preparan proyectos académicos y lectores interesados en comprender cómo funcionan las redes neuronales utilizadas actualmente en visión artificial, procesamiento de lenguaje y otros campos.

El enfoque es introductorio, pero no superficial. No se busca solamente aprender a escribir unas pocas líneas de Keras para entrenar un modelo. El objetivo es comprender qué representan las capas, qué ocurre durante una propagación hacia adelante, cómo se mide un error, cómo se modifican los parámetros y por qué determinadas arquitecturas son apropiadas para ciertos tipos de datos.

Al mismo tiempo, tampoco se pretende desarrollar todos los detalles matemáticos o de investigación relacionados con cada arquitectura. El propósito es construir una base sólida que permita utilizar estas herramientas con criterio y continuar posteriormente hacia bibliografía y cursos más especializados.

## Cómo trabajar con este libro y los cuadernos

Cada capítulo puede leerse directamente en el PDF, pero fue pensado también como una experiencia práctica apoyada en cuadernos ejecutables. La recomendación es acompañar la lectura con la versión online del cuaderno correspondiente siempre que sea posible.

El libro y los cuadernos cumplen funciones complementarias. El texto desarrolla las ideas, explica qué problema estamos intentando resolver, introduce los conceptos necesarios y justifica las decisiones que aparecen en cada modelo. Los cuadernos permiten ejecutar esas ideas, observar resultados reales y experimentar con diferentes configuraciones.

En los cuadernos de Google Colab conviene ejecutar cada celda y observar cuidadosamente sus resultados. Cambiar la cantidad de neuronas, modificar una función de activación, aumentar el número de épocas, cambiar el learning rate o utilizar otra arquitectura permite comprobar que el comportamiento de una red depende de muchas decisiones relacionadas entre sí.

También será importante observar el proceso de entrenamiento, y no solamente el resultado final. Las curvas de pérdida y de métricas permiten analizar cómo aprende una red, cuándo deja de mejorar y cuándo comienza a memorizar demasiado los datos de entrenamiento.

A medida que avancemos hacia visión artificial y otros tipos de datos, los cuadernos permitirán visualizar imágenes, filtros, predicciones, errores y ejemplos concretos. La intención es que el código no aparezca separado de la explicación conceptual, sino como una herramienta para comprobar y explorar lo que se desarrolla en el texto.

Los capítulos fueron diseñados como una secuencia progresiva. Algunos conceptos reaparecerán varias veces porque adquieren nuevos significados a medida que las arquitecturas se vuelven más complejas. Ideas como entrenamiento, validación, sobreajuste, parámetros, hiperparámetros y generalización continúan siendo tan importantes en Deep Learning como en los modelos estudiados anteriormente.

## Enfoque del libro

El objetivo principal de este tomo es presentar Deep Learning como una continuación natural del recorrido realizado en Machine Learning, y no como un conjunto completamente separado de técnicas.

A lo largo del libro se priorizan cinco ideas:

* una red neuronal puede entenderse como una sucesión de transformaciones que aprende a partir de datos;
* las representaciones internas son una parte fundamental de lo que aprende una red profunda;
* entrenar una red significa ajustar parámetros para reducir una función de pérdida, no simplemente ejecutar una biblioteca;
* diferentes tipos de datos requieren arquitecturas capaces de aprovechar su estructura;
* modelos más grandes y potentes continúan necesitando evaluación, análisis de errores, control del sobreajuste y criterio humano.

Con esa base podremos avanzar desde una neurona artificial hasta redes capaces de reconocer imágenes, procesar secuencias y utilizar mecanismos de atención.

El objetivo final no es memorizar una colección de arquitecturas, sino comprender las ideas que las conectan. Una vez entendidos conceptos como capas, representaciones, activaciones, pérdida, gradientes y entrenamiento, resulta mucho más sencillo interpretar modelos que inicialmente pueden parecer muy diferentes.

Deep Learning es un campo que continúa evolucionando rápidamente. Algunas arquitecturas actuales serán reemplazadas, ampliadas o combinadas con otras. Por eso este libro intenta concentrarse en fundamentos que permanezcan útiles más allá de una biblioteca, una versión particular de TensorFlow o un modelo específico.

La intención es que, al finalizar el recorrido, el lector pueda observar una arquitectura de Deep Learning, comprender sus componentes principales, ejecutar y modificar modelos sencillos, analizar su entrenamiento, interpretar sus resultados y contar con una base suficientemente sólida para continuar hacia áreas más avanzadas.

---

## Listado de Cuadernos Colab

#### (Esta parte está en construcción)

## Índice de capítulos

### Parte I · Del Machine Learning a las redes neuronales

* [Capítulo 1 · ¿Qué es Deep Learning?](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/libros/ciencia-de-datos-con-python/volumen-05/cuadernos/CienciaDeDatos_Tomo5_Cuaderno01.ipynb)
* [Capítulo 2 · La neurona artificial](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/libros/ciencia-de-datos-con-python/volumen-05/cuadernos/CienciaDeDatos_Tomo5_Cuaderno02.ipynb)
* [Capítulo 3 · De una neurona a una red](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/libros/ciencia-de-datos-con-python/volumen-05/cuadernos/CienciaDeDatos_Tomo5_Cuaderno03.ipynb)
* Capítulo 4 · Funciones de activación

### Parte II · Cómo aprende una red neuronal

* Capítulo 5 · Medir el error: funciones de pérdida
* Capítulo 6 · Descenso por gradiente
* Capítulo 7 · Backpropagation
* Capítulo 8 · Épocas, batches y optimizadores

### Parte III · Primeras redes neuronales

* Capítulo 9 · Primer modelo de Deep Learning
* Capítulo 10 · Entrenamiento y validación
* Capítulo 11 · Sobreajuste en redes neuronales

### Parte IV · Imágenes como datos

* Capítulo 12 · Cómo ve una computadora una imagen
* Capítulo 13 · Reconocimiento de dígitos con MNIST
* Capítulo 14 · De píxeles a características

### Parte V · Redes neuronales convolucionales

* Capítulo 15 · Convoluciones
* Capítulo 16 · Pooling
* Capítulo 17 · Primera red convolucional
* Capítulo 18 · Clasificar imágenes con Fashion-MNIST
* Capítulo 19 · Imágenes en color con CIFAR-10

### Parte VI · Mejorar modelos de visión

* Capítulo 20 · Data augmentation
* Capítulo 21 · Transfer learning
* Capítulo 22 · Un problema con imágenes propias

### Parte VII · Texto y secuencias

* Capítulo 23 · Texto como datos
* Capítulo 24 · Clasificar textos
* Capítulo 25 · Datos secuenciales y memoria

### Parte VIII · Atención y transformers

* Capítulo 26 · Atención
* Capítulo 27 · Transformers

### Parte IX · Modelos preentrenados

* Capítulo 28 · El ecosistema actual de modelos preentrenados

### Parte X · Evaluación, criterio y próximos caminos

* Capítulo 29 · Analizar errores, confianza y datos desconocidos
* Capítulo 30 · Datos, sesgos y decisiones
* Capítulo 31 · Guardar, cargar y utilizar un modelo entrenado
* Capítulo 32 · Cómo seguir aprendiendo Deep Learning

---

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes](../../../ACERCA-DE.md)** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos, Machine Learning, Deep Learning y programación con Python.
