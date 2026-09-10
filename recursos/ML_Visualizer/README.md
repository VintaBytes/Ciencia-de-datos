# ML Visualizer 2.0

🤝 [Apoyar este proyecto](https://vintabytes.github.io/apoyar/) 🤝 

![Python](https://img.shields.io/badge/Python-FFD43B?logo=python&logoColor=blue)
![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?logo=python&logoColor=white)
![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-7952B3?logo=bootstrap&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-306998?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-3776AB?logo=python&logoColor=white)
![AppImage](https://img.shields.io/badge/AppImage-2CCCE4?logo=appimage&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows11&logoColor=white)


Aplicación de escritorio didáctica para explorar modelos sencillos de Machine Learning mediante datasets sintéticos y visualizaciones interactivas. Está desarrollada con Python, `ttkbootstrap`, Tkinter, NumPy, Pillow y scikit-learn.

El programa permite comenzar con **Ninguno — solo datos**, observar la distribución de los puntos y elegir después un modelo. Seleccionar o cambiar el modelo conserva exactamente el dataset visible.

## Contenido

- [Funciones principales](#funciones-principales)
- [Modelos y datasets](#modelos-y-datasets)
- [Requisitos](#requisitos)
- [Usar el programa en Linux](#usar-el-programa-en-linux)
- [Usar el programa en Windows](#usar-el-programa-en-windows)
- [Manual de uso](#manual-de-uso)
- [Configuraciones JSON](#configuraciones-json)
- [Crear un ejecutable para Windows con PyInstaller](#crear-un-ejecutable-para-windows-con-pyinstaller)
- [Crear una AppImage en Linux](#crear-una-appimage-en-linux)
  - [Crear el ejecutable autocontenido](#1-crear-el-ejecutable-autocontenido)
  - [Preparar el AppDir](#2-preparar-el-appdir)
  - [Generar la AppImage](#3-generar-la-appimage)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Atajos principales](#atajos-principales)
- [Autoría](#autoría)


<table align="center">
  <tr>
    <td align="center">
        <img src="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/recursos/imagenes/MLV1.png" width="800">
    </td>
  </tr>
</table>

[![Descargar AppImage](https://img.shields.io/badge/Descargar-Linux-2CCCE4?logo=appimage&logoColor=white)](https://drive.google.com/file/d/1Bg8LvE4o37OaHgU7GvsXdwa5ulseUxVr/view?usp=sharing) 
[![Descargar para Windows](https://img.shields.io/badge/Descargar-Windows-2CCCE4?logo=windows&logoColor=white)](https://drive.google.com/file/d/1oAFfma7YP744RVE_IhEzFalNwRocLcFg/view?usp=sharing)

(La versión de Windows fue creada gentilmente por [Pablo Damian.](https://github.com/Pablo-Damian/ML_Visualizer_Windows) ¡Gracias!

## Funciones principales

- Tres tipos de problema: clasificación, regresión y agrupamiento.
- Generación de datasets sintéticos con una cantidad configurable de muestras.
- Entrenamiento automático al seleccionar un modelo o modificar sus parámetros.
- Mapas de decisión, probabilidad e incertidumbre para clasificación.
- Visualizaciones didácticas específicas para cada familia de modelos.
- Predicciones y datos locales al mover el cursor sobre el gráfico.
- Incorporación y eliminación manual de observaciones.
- Temas claros y oscuros de `ttkbootstrap` sin alterar los colores del gráfico.
- Configuraciones que pueden abrirse y guardarse como archivos JSON.

## Modelos y datasets

| Tipo de problema | Modelos                                                               | Datasets sintéticos                                                             |
| ---------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Clasificación   | Regresión logística, KNN, árbol de decisión y Random Forest       | Blobs, grupos, lunas, círculos, clasificación, gaussianos, espiral y aleatorio |
| Regresión       | Regresión lineal, regresión polinómica, KNN y árbol de regresión | Lineal, con ruido, con valores atípicos y no lineal                             |
| Agrupamiento     | K-Means                                                               | Tres grupos, grupos desiguales, lunas, círculos y aleatorio                     |

Los modelos supervisados se ajustan con el 75 % de los datos y se evalúan con el 25 % restante. K-Means utiliza el conjunto completo porque trabaja sin etiquetas objetivo.

<table align="center">
  <tr>
    <td align="center">
        <img src="https://github.com/VintaBytes/Ciencia-de-datos/blob/main/recursos/imagenes/MLV2.png" width="800">
    </td>
  </tr>
</table>

## Requisitos

- Python 3.10 o posterior. Se recomienda Python 3.11 o 3.12.
- Tkinter.
- Las dependencias indicadas en `requirements.txt`.

## Usar el programa en Linux

En distribuciones basadas en Ubuntu o Linux Mint, instalar primero Python, el soporte para entornos virtuales y Tkinter:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-tk
```

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

También puede utilizarse el iniciador incluido:

```bash
chmod +x iniciar.sh
./iniciar.sh
```

El script crea `.venv` si no existe, instala o actualiza las dependencias necesarias y abre el programa.

## Usar el programa en Windows

Instalar Python desde [python.org](https://www.python.org/downloads/) y marcar **Add Python to PATH** durante la instalación. Tkinter se incluye normalmente en la instalación oficial de Python para Windows.

Abrir PowerShell o Símbolo del sistema dentro de la carpeta del proyecto y ejecutar:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

Como alternativa, puede hacerse doble clic en `iniciar.bat`. Ese archivo crea el entorno virtual, instala las dependencias y abre la aplicación.

## Manual de uso

El menú **Ayuda → Manual de uso** abre una guía integrada. El documento [instrucciones_de_uso.md](instrucciones_de_uso.md) contiene el mismo recorrido con información adicional sobre la relación entre los controles.

## Configuraciones JSON

El menú **Archivo** permite abrir, guardar y guardar como una configuración. Se conservan:

- tipo de problema y dataset;
- cantidad de muestras y semilla de generación;
- modelo e hiperparámetros;
- representación del mapa y visualización didáctica;
- tema de la interfaz.

La configuración reproduce el dataset sintético original mediante su semilla. Los puntos agregados o eliminados manualmente con el mouse no se guardan en el JSON.

## Crear un ejecutable para Windows con PyInstaller

> El `.exe` debe construirse en Windows. PyInstaller no genera de forma cruzada un ejecutable de Windows desde Linux.

1. Abrir una terminal en la carpeta del proyecto y activar el entorno virtual.
2. Instalar PyInstaller:

```powershell
python -m pip install --upgrade pyinstaller
```

3. Crear un ejecutable único, sin consola:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed --name ML_Visualizer --collect-all ttkbootstrap main.py
```

El resultado será `dist\ML_Visualizer.exe`. Conviene ejecutarlo en otra computadora con Windows antes de publicarlo. El arranque de la variante `--onefile` puede tardar unos segundos porque descomprime sus componentes en una carpeta temporal.

Durante la construcción se crean `build`, `dist` y `ML_Visualizer.spec`. Están excluidos del repositorio mediante `.gitignore`.

La sintaxis y las opciones utilizadas están documentadas en el [manual oficial de PyInstaller](https://pyinstaller.org/en/stable/usage.html).

## Crear una AppImage en Linux

> La AppImage debe construirse en Linux. Para mejorar la compatibilidad, conviene hacerlo en una distribución igual o más antigua que aquella en la que se distribuirá.

### 1. Crear el ejecutable autocontenido

Activar el entorno virtual del proyecto e instalar PyInstaller:

```bash
source .venv/bin/activate
python -m pip install --upgrade pyinstaller
python -m PyInstaller --noconfirm --clean --onedir --name ML_Visualizer --collect-all ttkbootstrap main.py
```

PyInstaller dejará la aplicación en `dist/ML_Visualizer/`.

### 2. Preparar el AppDir

El repositorio incluye `AppRun`, el archivo `.desktop` y un icono en `empaquetado/linux/`:

```bash
mkdir -p ML_Visualizer.AppDir/usr/bin
cp -a dist/ML_Visualizer/. ML_Visualizer.AppDir/usr/bin/
cp empaquetado/linux/AppRun ML_Visualizer.AppDir/
cp empaquetado/linux/ML_Visualizer.desktop ML_Visualizer.AppDir/
cp empaquetado/linux/ml-visualizer.svg ML_Visualizer.AppDir/
ln -sf ml-visualizer.svg ML_Visualizer.AppDir/.DirIcon
chmod +x ML_Visualizer.AppDir/AppRun
```

La estructura creada sigue el formato AppDir descrito por la [documentación oficial de AppImage](https://docs.appimage.org/packaging-guide/manual.html).

### 3. Generar la AppImage

Descargar `appimagetool` para la arquitectura correspondiente desde sus [versiones oficiales](https://github.com/AppImage/appimagetool/releases/continuous), otorgarle permiso de ejecución y colocarlo en el `PATH` o en la carpeta del proyecto.

Para una computadora `x86_64`:

```bash
chmod +x appimagetool-x86_64.AppImage
ARCH=x86_64 ./appimagetool-x86_64.AppImage ML_Visualizer.AppDir ML_Visualizer-x86_64.AppImage
chmod +x ML_Visualizer-x86_64.AppImage
./ML_Visualizer-x86_64.AppImage
```

Si `appimagetool` no puede usar FUSE, puede ejecutarse así:

```bash
ARCH=x86_64 APPIMAGE_EXTRACT_AND_RUN=1 ./appimagetool-x86_64.AppImage ML_Visualizer.AppDir ML_Visualizer-x86_64.AppImage
```

La AppImage resultante debe probarse en al menos otra distribución Linux antes de publicarse.

## Estructura del proyecto

| Archivo o carpeta                | Función                                               |
| -------------------------------- | ------------------------------------------------------ |
| `main.py`                      | Ventana principal, controles, estado y configuraciones |
| `ml_utils.py`                  | Datasets, modelos, entrenamiento, métricas y mapas    |
| `visualizer.py`                | Canvas interactivo y renderizado gráfico              |
| `dialogos.py`                  | Ayuda integrada y ventana Acerca de                    |
| `configuracion.py`             | Lectura y escritura de configuraciones JSON            |
| `instrucciones_de_uso.md`      | Manual breve del usuario                               |
| `requirements.txt`             | Dependencias de ejecución                             |
| `iniciar.sh` / `iniciar.bat` | Inicio asistido en Linux y Windows                     |
| `empaquetado/linux/`           | Archivos auxiliares para construir la AppImage         |

## Atajos principales

| Atajo             | Acción                                        |
| ----------------- | ---------------------------------------------- |
| `Ctrl+O`        | Abrir una configuración                       |
| `Ctrl+S`        | Guardar la configuración actual               |
| `Ctrl+Mayús+S` | Guardar como un archivo nuevo                  |
| `F1`            | Abrir el manual integrado                      |
| `V`             | Mostrar u ocultar la visualización didáctica |
| `B`             | Cambiar el mapa de clasificación              |
| `R`             | Generar un nuevo dataset                       |

## Autoría

ML Visualizer 2.0 fue creado por **Ariel Palazzesi** con ayuda de IA (ChatGPT). Puede encontrarse junto con más material de Ciencia de Datos y Machine Learning en [VintaBytes/Ciencia-de-datos](https://github.com/VintaBytes/Ciencia-de-datos).
