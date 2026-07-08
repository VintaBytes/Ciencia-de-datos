# Ciencia de Datos con Python - Vol III

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
        <img src="https://github.com/VintaBytes/VintaBytes.github.io/blob/main/images/portada3.png" alt="Ciencia de Datos con Python - Vol 3">
      </a>
      <br>
      <strong><a href="https://drive.google.com/file/d/1rGDPSz8Ggy9xMjGUS_Vynr4_rzejMfdt/view?usp=drive_link">Descargar PDF Volumen III</a></strong>
      <br>
      Machine Learning<br>Este libro está en desarrollo.<br>Pasá en unos días para ver las novedades.
    </td>
  </tr>
</table>


Este directorio reúne una serie de cuadernos de Google Colab orientados al aprendizaje progresivo de **Machine Learning** usando **Python** y **Pandas**, correspondientes al PDF **[Ciencia de Datos con Python - Vol III](https://drive.google.com/file/d/1rGDPSz8Ggy9xMjGUS_Vynr4_rzejMfdt/view?usp=drive_link)**.

[Ir al índice de Cuadernos Colab](#listado-de-cuadernos-colab)

---

# Introducción

Después de aprender a cargar, inspeccionar, limpiar, transformar, resumir, agrupar y visualizar datos, aparece una nueva etapa en el trabajo con Python: construir modelos capaces de aprender patrones a partir de esos datos. Ya no se trata solo de describir lo que ocurrió, comparar grupos o comunicar hallazgos exploratorios. Ahora comenzamos a preguntarnos si, a partir de la información disponible, es posible hacer predicciones, clasificar casos, estimar valores numéricos, detectar comportamientos particulares o descubrir estructuras que no estaban explícitamente marcadas.

Este tercer tomo de **Ciencia de Datos con Python** continúa el recorrido iniciado [en los volúmenes anteriores](https://github.com/VintaBytes/Ciencia-de-datos). Si el **[primer tomo](https://github.com/VintaBytes/Ciencia-de-datos/blob/main/Ciencia%20De%20Datos%20Con%20Python/readme.md)** estuvo centrado en comprender y preparar datos tabulares, y el segundo avanzó hacia el análisis exploratorio, este volumen introduce los conceptos fundamentales del **Machine Learning**. El objetivo es que el lector pueda comprender qué significa entrenar un modelo, qué tipos de problemas pueden abordarse, cómo se preparan los datos para aprender, cómo se evalúan los resultados y qué precauciones deben tomarse para no extraer conclusiones engañosas.

Machine Learning suele presentarse como una disciplina compleja, rodeada de términos técnicos, modelos sofisticados y promesas exageradas. En este libro vamos a recorrer el tema desde una perspectiva introductoria, pero cuidadosa. No empezaremos por los modelos más avanzados ni por fórmulas desconectadas de la práctica, sino por las preguntas básicas: qué es aprender a partir de datos, qué diferencia hay entre un problema de clasificación y uno de regresión, qué significa trabajar con datos etiquetados o no etiquetados, por qué es necesario separar datos de entrenamiento y prueba, y cómo sabemos si un modelo realmente está funcionando.

El contenido de este libro se apoya en una serie de cuadernos de trabajo preparados para Google Colab. En el libro en formato PDF, esos cuadernos se presentan como texto organizado para facilitar la lectura continua, la consulta y el estudio. Sin embargo, la experiencia más completa se obtiene al trabajar también con los cuadernos originales en línea: allí es posible ejecutar el código, modificarlo, observar los resultados, cambiar parámetros, comparar modelos y experimentar con distintos datasets.

Siempre que sea posible, los ejemplos se apoyan en situaciones reales o en datasets disponibles públicamente, incluyendo conjuntos de datos clásicos y datasets provenientes de plataformas como Kaggle. La intención no es trabajar con ejemplos artificiales demasiado simples, sino acercar al lector a problemas parecidos a los que puede encontrar en contextos de estudio, investigación, análisis profesional o proyectos personales.

## Qué vas a encontrar en este tomo

Este tomo se concentra en los fundamentos del Machine Learning aplicado con Python. A lo largo de los capítulos se presentan los conceptos centrales de la disciplina: modelos, entrenamiento, predicción, generalización, variables de entrada, variable objetivo, datos etiquetados, datos no etiquetados, aprendizaje supervisado, aprendizaje no supervisado, clasificación, regresión y agrupamiento.

En los primeros capítulos se construye una base conceptual. Antes de entrenar modelos, es necesario comprender qué tipo de problema tenemos entre manos y qué esperamos que el modelo aprenda. No es lo mismo predecir si un correo es spam que estimar el precio de una vivienda, agrupar clientes según su comportamiento o detectar observaciones extrañas dentro de un conjunto de datos. Cada problema requiere una forma distinta de pensar los datos, elegir modelos y evaluar resultados.

Luego se trabaja sobre la preparación de datos para Machine Learning. Se introducen ideas fundamentales como la separación entre variables de entrada y variable objetivo, la división entre datos de entrenamiento y prueba, el tratamiento de valores faltantes, la codificación de variables categóricas, el escalado de variables numéricas y el uso de herramientas como `ColumnTransformer` y `Pipeline`. También aparece una advertencia clave que acompañará todo el libro: la fuga de datos. Un modelo puede parecer muy bueno si, sin darnos cuenta, le damos información que no debería tener disponible al momento de predecir.

Más adelante se presentan los primeros modelos de clasificación, comenzando por enfoques intuitivos como K-Nearest Neighbors y avanzando hacia regresión logística y árboles de decisión. La intención no es memorizar instrucciones, sino entender cómo piensa cada modelo, qué tipo de frontera de decisión construye, qué ventajas ofrece, en qué situaciones puede fallar y qué cuidados requiere.

Una parte importante del recorrido está dedicada a la evaluación. En Machine Learning no alcanza con entrenar un modelo y obtener una predicción: necesitamos saber si esa predicción es confiable, si el modelo generaliza bien a datos nuevos y si la métrica utilizada realmente tiene sentido para el problema. Por eso se estudian la matriz de confusión, la accuracy, precision, recall, F1-score, curvas ROC, AUC y el uso de umbrales de decisión.

El libro también aborda problemas de regresión, donde la variable objetivo no es una categoría sino un valor numérico. Allí se introducen modelos como la regresión lineal y métricas como MAE, MSE, RMSE y $R^2$. El objetivo es que el lector pueda distinguir con claridad cuándo está frente a un problema de clasificación y cuándo frente a un problema de regresión, y que pueda interpretar los errores del modelo en unidades reales.

En la segunda mitad del tomo se profundiza en la generalización, la validación cruzada, el sobreajuste, el subajuste y la búsqueda de hiperparámetros. Estos temas son esenciales para construir modelos con mayor criterio. Un modelo no es mejor solo porque obtiene un buen resultado en una partición particular de los datos; necesitamos evaluar su comportamiento de manera más robusta y comparar alternativas con cuidado.

También se presentan modelos más potentes, como Random Forest, Gradient Boosting, Support Vector Machines y Naive Bayes. Cada uno se introduce desde su idea principal, sus condiciones de uso, sus fortalezas y sus limitaciones. El propósito no es agotar todos los detalles matemáticos o técnicos, sino construir una comprensión suficiente para usarlos con responsabilidad y saber cuándo conviene profundizar.

Hacia el final se introduce el aprendizaje no supervisado, donde no contamos con una variable objetivo. Se trabajan conceptos como clustering con K-Means y reducción de dimensionalidad con PCA. Estos capítulos permiten ampliar la mirada más allá de la predicción supervisada y comprender que Machine Learning también puede utilizarse para explorar estructuras, reducir complejidad y observar patrones no etiquetados.

El cierre del libro está dedicado a la interpretación, los sesgos, los errores frecuentes y la comunicación de resultados. Un modelo puede ser técnicamente correcto y, aun así, conducir a malas decisiones si se interpretan mal sus resultados, si los datos tienen sesgos importantes, si las métricas no reflejan el objetivo real o si se comunican conclusiones de manera exagerada. Por eso este tomo insiste en una idea central: usar Machine Learning implica también desarrollar criterio.

## Requisitos previos

Para aprovechar este libro conviene haber trabajado previamente con los contenidos de **[los tomos anteriores de **Ciencia de Datos con Python](https://github.com/VintaBytes/Ciencia-de-datos)** o contar con conocimientos equivalentes. En particular, se recomienda conocer:

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
* lectura e interpretación inicial de tablas, distribuciones y comparaciones.

No es necesario tener experiencia previa en Machine Learning. Este libro está pensado para lectores que se acercan al tema por primera vez. Tampoco se requiere un dominio avanzado de matemática, aunque sí se presentarán fundamentos matemáticos cuando sean necesarios para comprender una métrica, una idea de optimización, una distancia, un error o una medida de evaluación.

El objetivo no es evitar la matemática, sino incorporarla de forma gradual y conectada con problemas concretos. Cuando una fórmula aparezca, lo hará para explicar una idea útil: cómo se mide un error, qué significa maximizar una separación, cómo se resume el desempeño de un modelo o por qué una métrica puede ser más adecuada que otra.

## A quién está dirigido

Este material está pensado para personas que ya conocen Python y han trabajado con datos tabulares, pero no tienen experiencia previa en Machine Learning. Puede ser útil para estudiantes, docentes, programadores, analistas, profesionales que trabajan con datos, personas que preparan proyectos académicos y cualquier lector que quiera comprender los fundamentos de los modelos predictivos sin comenzar directamente por herramientas avanzadas.

El enfoque es introductorio, pero no superficial. Se busca que el lector pueda entrenar modelos, evaluar resultados y comparar alternativas, pero también que entienda las limitaciones de cada procedimiento. En Machine Learning, obtener una métrica no significa necesariamente haber resuelto un problema. Hay que mirar los datos, revisar supuestos, analizar errores, evitar fugas de información, considerar sesgos y comunicar conclusiones con prudencia.

Este libro puede acompañar a quienes estén comenzando un curso de Machine Learning, preparando un proyecto académico, explorando datasets de Kaggle o intentando comprender mejor cómo se aplican modelos predictivos en problemas reales. No está pensado como un manual exhaustivo de todos los algoritmos existentes, sino como una base sólida para empezar a construir criterio.

## Cómo trabajar con este libro y los cuadernos

Cada capítulo puede leerse directamente en el PDF, pero fue pensado también como una experiencia práctica apoyada en cuadernos ejecutables. La recomendación es acompañar la lectura con la versión online del cuaderno correspondiente siempre que sea posible.

En los cuadernos de Google Colab conviene ejecutar cada celda, observar la salida y preguntarse qué aporta ese resultado al problema que se está resolviendo. En Machine Learning, muchas veces el valor no está solo en que el código funcione, sino en interpretar qué ocurrió: cómo quedaron separados los datos, qué variables usó el modelo, qué métrica se obtuvo, qué errores cometió y si el resultado parece razonable.

También es recomendable modificar los ejemplos. Cambiar una variable, probar otro modelo, ajustar un hiperparámetro, alterar el tamaño del conjunto de prueba o comparar distintas métricas ayuda a comprender que los modelos no son cajas mágicas. Cada decisión del proceso puede influir en el resultado final.

Los capítulos fueron diseñados como una secuencia progresiva. Algunos conceptos reaparecen en distintos momentos porque forman parte del trabajo cotidiano con modelos. La separación entre entrenamiento y prueba, la evaluación sobre datos no vistos, el riesgo de sobreajuste, la importancia de elegir métricas adecuadas y el cuidado frente a la fuga de datos no se aprenden en una única aparición: se consolidan al verlos funcionar en distintos contextos.

## Enfoque del libro

El objetivo principal de este tomo es introducir el Machine Learning como una extensión natural del trabajo con datos. Antes de construir modelos, necesitamos comprender los datos; antes de confiar en una predicción, necesitamos evaluarla; antes de comunicar un resultado, necesitamos conocer sus límites.

A lo largo del recorrido se priorizan cuatro ideas:

* un modelo aprende patrones a partir de datos, no verdades absolutas;
* evaluar correctamente es tan importante como entrenar;
* no todos los problemas requieren el mismo tipo de modelo ni la misma métrica;
* una predicción útil debe interpretarse dentro del contexto del problema, los datos disponibles y sus limitaciones.

Con esa base, el lector queda preparado para avanzar hacia temas más especializados, como Deep Learning, procesamiento de lenguaje natural, series temporales, sistemas de recomendación o despliegue de modelos. Pero, sobre todo, queda mejor preparado para formular buenas preguntas, elegir herramientas con criterio y evitar algunos de los errores más comunes al comenzar a trabajar con Machine Learning.


---

## Listado de Cuadernos Colab

**Sección en construcción**


---

## Autor

Material desarrollado por **VintaByte** como parte de un recorrido formativo sobre ciencia de datos, análisis de datos y programación con Python.
