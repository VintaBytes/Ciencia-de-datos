# Ciencia de Datos con Python - Vol IV

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
      <a href="https://drive.google.com/file/d/1rGDPSz8Ggy9xMjGUS_Vynr4_rzejMfdt/view?usp=drive_link">
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/raw/main/images/portada4.png" alt="Ciencia de Datos con Python - Vol 4">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/14Hg7IwWqpmukbvOe-B5TR1Twz2MzRWkP/view?usp=sharing">Descargar PDF del Volumen IV</a></strong>
      <br>
      Machine Learning II<br>Este libro está en desarrollo.<br>Pasá en unos días para ver las novedades.
    </td>
  </tr>
</table>


Este directorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo de **Machine Learning** usando **Python** y **Pandas**, correspondientes al PDF **Ciencia de Datos con Python - Vol IV** que está en desarrollo.

[Ir al listado de Cuadernos Colab](#listado-de-cuadernos-colab)

---
# Introducción

Después de construir los primeros modelos de clasificación y regresión, aparece una nueva etapa en el aprendizaje de Machine Learning: comprender si esos modelos realmente generalizan, cómo pueden mejorarse, qué límites tienen y cómo deben interpretarse sus resultados. Ya no se trata solamente de entrenar un modelo y obtener una métrica inicial. Ahora comenzamos a preguntarnos si ese resultado es confiable, si se mantiene frente a nuevos datos, si el modelo está aprendiendo patrones útiles o si está ajustándose demasiado a los ejemplos que vio durante el entrenamiento.

Este cuarto tomo de **Ciencia de Datos con Python** continúa el recorrido iniciado [en los volúmenes anteriores](../README.md). El **[tercer tomo](../volumen-03/README.md)** introdujo los fundamentos del Machine Learning: qué significa aprender a partir de datos, cómo separar variables de entrada y variable objetivo, cómo preparar datos para entrenar modelos, cómo abordar problemas de clasificación y regresión, y cómo evaluar los primeros resultados. Este volumen retoma ese punto y avanza hacia una mirada más profunda, crítica y aplicada.

El objetivo de este tomo es que el lector pueda desarrollar mayor criterio al construir, evaluar, comparar, interpretar y comunicar modelos de Machine Learning. Para eso, trabajaremos temas que aparecen cuando los primeros modelos ya funcionan, pero todavía necesitamos responder preguntas más exigentes: ¿el modelo generaliza bien?, ¿está sobreajustando?, ¿la métrica es estable?, ¿cómo se comparan modelos de manera justa?, ¿qué tan confiables son sus predicciones?, ¿qué sesgos pueden arrastrar los datos?, ¿cómo comunicar resultados sin exagerar?

Machine Learning suele asociarse con la búsqueda del modelo más potente o de la métrica más alta. Sin embargo, a medida que los problemas se vuelven más reales, esa mirada resulta insuficiente. Un modelo puede obtener un buen resultado en una partición particular de los datos y, aun así, fallar en producción. Puede parecer preciso, pero estar usando información que no existiría al momento de predecir. Puede funcionar bien en promedio, pero equivocarse en los casos más importantes. Puede ser técnicamente correcto y, aun así, conducir a conclusiones mal comunicadas.

Por eso, este volumen insiste en una idea central: entrenar modelos es solo una parte del trabajo. También necesitamos evaluar con cuidado, validar con mayor robustez, revisar errores, comparar alternativas, interpretar resultados, detectar riesgos y comunicar conclusiones responsables.

El contenido de este libro incluye una serie de cuadernos de trabajo preparados para Google Colab. En el libro en formato PDF se presentan los temas como texto organizado para facilitar la lectura continua, la consulta y el estudio. Sin embargo, la experiencia más completa se obtiene al trabajar también con los cuadernos disponibles en línea: allí es posible ejecutar el código, modificarlo, observar los resultados, cambiar parámetros, comparar modelos, revisar errores y experimentar con distintos datasets.

Siempre que sea posible, los ejemplos se apoyan en situaciones reales o en datasets disponibles públicamente, incluyendo conjuntos de datos clásicos y datasets provenientes de plataformas como Kaggle. La intención no es trabajar con ejemplos artificiales demasiado simples, sino acercar al lector a problemas parecidos a los que puede encontrar en contextos de estudio, investigación, análisis profesional o proyectos personales.

## Qué vas a encontrar en este tomo

Este tomo se concentra en la profundización del trabajo con modelos de Machine Learning aplicado con Python. A lo largo de los capítulos se presentan herramientas y criterios para evaluar mejor, mejorar modelos, controlar su complejidad, trabajar con algoritmos más potentes, explorar datos no etiquetados, interpretar resultados y comunicar conclusiones con responsabilidad.

En los primeros capítulos se trabaja sobre la generalización. Esta idea es central en Machine Learning: no buscamos que un modelo funcione bien solo con los datos que ya vio, sino que pueda responder de manera razonable frente a casos nuevos. Para eso se estudian el sobreajuste y el subajuste, dos problemas fundamentales que ayudan a comprender cuándo un modelo es demasiado simple, cuándo es demasiado complejo y qué señales pueden alertarnos sobre un aprendizaje poco confiable.

Luego se introduce la validación cruzada. Una única separación entre entrenamiento y prueba puede ser útil, pero también puede depender demasiado del azar de esa partición. La validación cruzada permite evaluar modelos con más estabilidad y comparar alternativas con mayor criterio. En este tramo también se trabaja la búsqueda de hiperparámetros, incluyendo estrategias como Grid Search y Randomized Search, siempre vinculadas con la necesidad de evitar evaluaciones engañosas.

Más adelante se estudia la regularización y el control de la complejidad. Estos conceptos ayudan a entender cómo algunos modelos pueden limitar su flexibilidad para generalizar mejor. La idea no es hacer modelos cada vez más complejos, sino encontrar un equilibrio entre aprender patrones útiles y no memorizar detalles particulares del conjunto de entrenamiento.

El libro también presenta modelos más potentes que los abordados en el volumen anterior. Se estudian Random Forest, Gradient Boosting, Support Vector Machines y Naive Bayes. Cada modelo se introduce desde su idea principal, sus condiciones de uso, sus ventajas y sus limitaciones. El propósito no es agotar todos los detalles matemáticos o técnicos, sino construir una comprensión suficiente para usarlos con criterio y saber cuándo conviene profundizar.

Otro bloque importante está dedicado al aprendizaje no supervisado. Allí cambia el tipo de pregunta: ya no contamos con una variable objetivo que indique la respuesta correcta. En su lugar, buscamos explorar estructura en los datos. Se trabajan conceptos como datos no etiquetados, clustering con K-Means y reducción de dimensionalidad con PCA. Estos temas permiten ampliar la mirada más allá de la predicción supervisada y comprender que Machine Learning también puede utilizarse para agrupar, simplificar, visualizar y detectar patrones.

Hacia el final, el libro se concentra en la interpretación, los sesgos, los errores comunes y la comunicación de resultados. Un modelo no debería evaluarse únicamente por sus métricas. También debemos preguntarnos qué variables utiliza, cómo se comporta, en qué casos falla, qué sesgos pueden estar presentes en los datos, qué errores metodológicos debemos evitar y cómo presentar conclusiones sin exagerar.

En particular, se trabajan ideas como interpretación de modelos, importancia de variables, permutation importance, sesgo en los datos, variables sensibles, correlación y causalidad, decisiones automatizadas y responsabilidad humana. Estos temas son fundamentales para comprender que Machine Learning no es solo una técnica predictiva, sino también una práctica que puede influir en decisiones reales.

El cierre del tomo está dedicado a los errores frecuentes al construir modelos y a la comunicación responsable de resultados. Se revisan problemas como entrenar y evaluar con los mismos datos, fuga de datos, preprocesar antes de separar, usar variables que no existirían en producción, elegir métricas inadecuadas, comparar modelos de forma injusta, confiar en un único resultado y sobreinterpretar conclusiones. También se propone una forma básica de comunicar informes de Machine Learning, incluyendo problema, datos, enfoque, métricas, errores, limitaciones y conclusiones.

Finalmente, el último capítulo abre caminos para seguir aprendiendo. Se mencionan temas que quedan fuera de este recorrido, como Deep Learning, procesamiento de lenguaje natural, series temporales, sistemas de recomendación y MLOps. La intención no es cerrar el aprendizaje, sino mostrar que, a partir de los fundamentos construidos en estos tomos, el lector ya cuenta con una base para avanzar hacia áreas más especializadas.

## Requisitos previos

Para aprovechar este libro conviene haber trabajado previamente con los contenidos de **[los tomos anteriores de Ciencia de Datos con Python](../README.md)** o contar con conocimientos equivalentes. En particular, se recomienda conocer:

* nociones básicas de programación en Python;
* uso general de Google Colab o notebooks;
* estructura de un DataFrame de Pandas;
* selección de filas y columnas;
* filtros con condiciones;
* ordenamiento de datos;
* creación y modificación de columnas;
* detección básica de valores faltantes, duplicados y tipos de datos;
* cálculo de resúmenes estadísticos simples;
* uso básico de gráficos con Matplotlib;
* lectura e interpretación inicial de tablas, distribuciones y comparaciones;
* conceptos iniciales de Machine Learning;
* separación entre variables de entrada y variable objetivo;
* división entre datos de entrenamiento y prueba;
* preparación básica de datos para modelos;
* primeros modelos de clasificación y regresión;
* métricas iniciales para evaluar modelos.

Este tomo está pensado como continuación directa del volumen anterior. No se requiere experiencia avanzada en Machine Learning, pero sí conviene comprender las ideas básicas de entrenamiento, predicción, clasificación, regresión, evaluación y fuga de datos. Muchos de esos conceptos reaparecen aquí, pero se trabajan con mayor profundidad y en contextos más exigentes.

Tampoco se requiere un dominio avanzado de matemática, aunque sí se presentarán fundamentos matemáticos cuando sean necesarios para comprender una métrica, una penalización, una distancia, un margen, una probabilidad, una reducción de dimensionalidad o una medida de evaluación.

El objetivo no es evitar la matemática, sino incorporarla de forma gradual y conectada con problemas concretos. Cuando una fórmula aparezca, lo hará para explicar una idea útil: cómo se mide un error, cómo se controla la complejidad, cómo se evalúa un modelo, cómo se calcula una distancia o cómo se interpreta una transformación.

## A quién está dirigido

Este material está pensado para personas que ya conocen Python, han trabajado con datos tabulares y tienen una base inicial de Machine Learning. Puede ser útil para estudiantes, docentes, programadores, analistas, profesionales que trabajan con datos, personas que preparan proyectos académicos y cualquier lector que quiera avanzar desde los primeros modelos hacia una comprensión más sólida del proceso completo.

El enfoque es introductorio en relación con los temas avanzados, pero no superficial. Se busca que el lector pueda evaluar modelos con mayor cuidado, comparar alternativas, ajustar hiperparámetros, reconocer sobreajuste, interpretar resultados, detectar errores frecuentes y comunicar conclusiones con prudencia.

Este libro puede acompañar a quienes estén continuando un curso de Machine Learning, preparando un proyecto académico, explorando datasets de Kaggle o intentando mejorar sus primeros modelos predictivos. No está pensado como un manual exhaustivo de todos los algoritmos existentes, sino como una base sólida para desarrollar criterio en el uso de modelos más complejos y en la interpretación de resultados.

## Cómo trabajar con este libro y los cuadernos

Cada capítulo puede leerse directamente en el PDF, pero fue pensado también como una experiencia práctica apoyada en cuadernos ejecutables. La recomendación es acompañar la lectura con la versión online del cuaderno correspondiente siempre que sea posible.

En los cuadernos de Google Colab conviene ejecutar cada celda, observar la salida y preguntarse qué aporta ese resultado al problema que se está resolviendo. En esta etapa, muchas veces el valor no está solo en entrenar un modelo, sino en interpretar qué ocurrió: si el resultado es estable, si el modelo sobreajusta, qué hiperparámetros influyen, qué errores comete, qué variables parecen importantes y si la conclusión es razonable.

También es recomendable modificar los ejemplos. Cambiar un modelo, ajustar un hiperparámetro, alterar una métrica, comparar validación cruzada con una separación simple o revisar errores individuales ayuda a comprender que los resultados no son propiedades absolutas del algoritmo. Cada decisión del proceso puede influir en la evaluación final.

Los capítulos fueron diseñados como una secuencia progresiva. Algunos conceptos reaparecen en distintos momentos porque forman parte del trabajo cotidiano con modelos. La separación entre entrenamiento y prueba, la evaluación sobre datos no vistos, el riesgo de sobreajuste, la importancia de elegir métricas adecuadas, el cuidado frente a la fuga de datos y la necesidad de comunicar límites no se aprenden en una única aparición: se consolidan al verlos funcionar en distintos contextos.

## Enfoque del libro

El objetivo principal de este tomo es profundizar el trabajo con Machine Learning como una extensión natural del análisis de datos. Una vez que sabemos construir modelos iniciales, necesitamos aprender a evaluarlos mejor, compararlos con más criterio, detectar sus límites e interpretar sus resultados.

A lo largo del recorrido se priorizan cinco ideas:

* un modelo debe generalizar a datos nuevos, no solo funcionar sobre los datos que ya vio;
* evaluar correctamente exige más que mirar una única métrica;
* modelos más potentes requieren más cuidado, no menos;
* interpretar un modelo implica comprender su comportamiento sin exagerar sus conclusiones;
* usar Machine Learning de manera responsable exige revisar datos, errores, sesgos, decisiones y comunicación.

Con esa base, el lector queda preparado para seguir avanzando hacia temas más especializados, como Deep Learning, procesamiento de lenguaje natural, series temporales, sistemas de recomendación, modelos generativos o despliegue de modelos. Pero, sobre todo, queda mejor preparado para formular buenas preguntas, elegir herramientas con criterio, evitar errores comunes y comunicar resultados de Machine Learning de manera prudente y responsable.


---

## Listado de Cuadernos Colab

#### (Esta parte está en construcción, y el contenido puede variar)

## Índice de capítulos

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

## Autor

Material desarrollado por **[Ariel Palazzesi / VintaBytes](../../../ACERCA-DE.md)** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos y programación con Python.
