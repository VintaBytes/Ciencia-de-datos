# Instrucciones de uso de ML Visualizer 2.0

ML Visualizer permite generar un conjunto de datos sintético, observarlo sin aplicar ningún algoritmo y comparar luego cómo distintos modelos aprenden a partir de esos mismos datos. No pretende enseñar por sí solo toda la teoría de Machine Learning: funciona como una herramienta visual para acompañar explicaciones, demostraciones y experiencias de aula.

## Recorrido básico

1. Seleccione el **Tipo de problema**.
2. Elija un **Dataset sintético** y la cantidad de muestras.
3. Observe los puntos con **Ninguno — solo datos**.
4. Seleccione un **Modelo**. El programa lo entrenará sobre los puntos visibles.
5. Modifique sus parámetros y compare la forma de la frontera o de la curva.
6. Active **Visualización didáctica (V)** y mueva el cursor sobre el gráfico.
7. Consulte las métricas y, si lo desea, guarde la configuración.

## Panel lateral

### Tipo de problema

Determina qué clase de tarea se estudiará:

- **Clasificación:** cada punto pertenece a la clase 0 o a la clase 1. El modelo aprende a separar ambas clases.
- **Regresión:** cada observación relaciona un valor de entrada `x` con un valor numérico continuo `y`.
- **Agrupamiento:** los puntos no tienen una clase conocida; K-Means intenta organizarlos en grupos.

Al cambiar el tipo de problema, el programa selecciona el primer dataset compatible, vuelve a **Ninguno — solo datos** y genera una muestra nueva. Los modelos y controles disponibles se actualizan porque no todos sirven para las mismas tareas.

### Dataset sintético

Permite elegir la forma general de los datos. Los datasets disponibles dependen del tipo de problema. Por ejemplo, clasificación incluye lunas, círculos y espirales; regresión incluye relaciones lineales, ruidosas, con valores atípicos y no lineales; agrupamiento incluye grupos compactos o desiguales.

Elegir otro dataset genera puntos nuevos y, si hay un modelo seleccionado, lo entrena automáticamente sobre ellos. El botón **Nuevo dataset** genera otra realización aleatoria del dataset elegido.

### Número de muestras

Controla cuántos puntos tendrá la próxima muestra generada. Admite valores entre 20 y 2000. Una cantidad pequeña facilita examinar observaciones individuales; una cantidad grande muestra con mayor claridad la estructura general, aunque puede aumentar el tiempo de entrenamiento y redibujado.

Los datos sólo se regeneran si el número cambia realmente. Pasar el foco hacia otro control no altera el dataset.

### Modelo

La primera opción es **Ninguno — solo datos**. En ese estado no se entrena ningún algoritmo, no se dibuja una frontera o curva y las métricas predictivas permanecen desactivadas. Sirve para analizar primero la forma de los datos y plantear qué modelo podría resultar apropiado.

Al elegir un modelo, el programa conserva exactamente los puntos visibles y entrena el algoritmo sobre ellos. Cambiar de modelo tampoco reemplaza el dataset, por lo que la comparación se realiza sobre la misma muestra.

Modelos disponibles:

- **Clasificación:** regresión logística, KNN, árbol de decisión y Random Forest.
- **Regresión:** regresión lineal, regresión polinómica, KNN para regresión y árbol de regresión.
- **Agrupamiento:** K-Means.

### Parámetros del modelo

Esta sección cambia según el algoritmo elegido. Puede mostrar:

- **Regularización C:** controla la regularización de la regresión logística.
- **Cantidad de vecinos:** determina cuántas observaciones utiliza KNN.
- **Profundidad máxima:** limita el crecimiento de un árbol.
- **Cantidad de árboles:** fija el tamaño del Random Forest.
- **Grado del polinomio:** determina la complejidad de la regresión polinómica.
- **Cantidad de clusters:** indica cuántos grupos debe buscar K-Means.

Modificar un parámetro vuelve a entrenar el modelo, pero mantiene los mismos datos. Esto permite observar directamente el efecto del hiperparámetro.

### Representación del mapa

Se habilita únicamente para clasificación cuando hay un modelo seleccionado:

- **Normal:** muestra la clase asignada a cada región.
- **Probabilidad:** representa la probabilidad estimada para la clase 1.
- **Incertidumbre:** resalta las zonas donde el modelo tiene menos seguridad.

Cambiar el mapa no vuelve a entrenar el modelo; sólo modifica la forma de representar sus resultados. La tecla `B` recorre estas tres opciones.

### Visualización didáctica (V)

Agrega una capa de información propia del modelo. Según el caso, puede mostrar:

- vecinos y radio de consulta de KNN;
- hoja activa y cantidad de muestras de un árbol;
- votos individuales de los árboles de Random Forest;
- residuos de los modelos de regresión;
- vecinos promediados por KNN para regresión;
- grado usado por la regresión polinómica;
- centroides y valor silhouette en K-Means.

La casilla y la tecla `V` realizan la misma acción. El control permanece desactivado cuando no hay modelo.

### Nuevo dataset

Genera otra muestra aleatoria de la distribución seleccionada. Mantiene el tipo de problema, el modelo y sus parámetros. Si hay un modelo activo, lo entrena sobre los puntos nuevos.

### Reentrenar

Vuelve a ajustar el modelo sobre los puntos actuales sin generar otros datos. Resulta útil después de editar el gráfico manualmente. Se desactiva en el modo **Ninguno — solo datos**.

### Métricas

El contenido depende de la tarea:

- **Clasificación:** accuracy de entrenamiento y de prueba. Random Forest también informa la importancia de `X₁` y `X₂`.
- **Regresión:** `R²`, MAE y RMSE sobre el conjunto de prueba. Algunos modelos muestran además información propia, como ecuación, grado, vecinos, profundidad u hojas.
- **Agrupamiento:** silhouette e inercia.

En clasificación y regresión, el modelo se ajusta con el 75 % de las observaciones. Las métricas de prueba se calculan sobre el 25 % que quedó fuera del entrenamiento.

## Gráfico interactivo

### Movimiento del mouse

Sin modelo, el cursor muestra solamente las coordenadas. Con un modelo entrenado, muestra la predicción local y la información específica disponible: probabilidad, vecinos, votos, hoja, valor estimado o silhouette.

### Agregar y quitar puntos

- En **Clasificación**, el clic izquierdo agrega un punto de clase 0 y el clic derecho agrega uno de clase 1.
- En **Regresión**, el clic izquierdo agrega una observación en la posición elegida y el clic derecho elimina la más cercana.
- En **Agrupamiento**, el clic izquierdo agrega un punto y el derecho elimina el más cercano.

Cada edición actualiza el modelo activo. El programa conserva un mínimo de observaciones para evitar conjuntos demasiado pequeños para entrenar.

## Menús

### Archivo

- **Abrir:** carga una configuración JSON.
- **Guardar:** actualiza el archivo de configuración actual.
- **Guardar como:** crea un nuevo archivo JSON.
- **Salir:** cierra el programa y consulta qué hacer si existen cambios sin guardar.

Una configuración guarda las opciones y la semilla con la que se creó el dataset sintético. Por ese motivo puede reconstruir la muestra original. No guarda los puntos agregados o eliminados manualmente.

### Apariencia

Permite elegir entre los temas claros y oscuros disponibles en `ttkbootstrap`. El tema modifica ventanas y controles, pero no los colores del gráfico, para que la representación de clases y modelos sea consistente.

### Ayuda

- **Manual de uso:** abre la ayuda desplazable integrada. También puede abrirse con `F1`.
- **Acerca de:** muestra el nombre, la versión, la autoría y el enlace del proyecto.

## Atajos de teclado

| Atajo | Acción |
| --- | --- |
| `Ctrl+O` | Abrir configuración |
| `Ctrl+S` | Guardar configuración |
| `Ctrl+Mayús+S` | Guardar como |
| `F1` | Abrir el manual integrado |
| `V` | Alternar la visualización didáctica |
| `B` | Cambiar la representación del mapa |
| `R` | Generar un nuevo dataset |

## Sugerencia para comparar modelos

Para que una comparación resulte clara, genere una muestra y no pulse **Nuevo dataset** mientras cambia de modelo o modifica hiperparámetros. Así todos los resultados se obtendrán sobre exactamente los mismos puntos. Si desea conservar las opciones y regenerar posteriormente la muestra original, guarde una configuración antes de continuar.
