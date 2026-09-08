@echo off
setlocal

rem Trabajar siempre desde la carpeta en la que se encuentra este iniciador.
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creando el entorno virtual...
    py -m venv .venv
    if errorlevel 1 goto :error
)

call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
if errorlevel 1 goto :error
python -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo Iniciando ML Visualizer 2.0...
python main.py
goto :fin

:error
echo.
echo No se pudo preparar o iniciar la aplicacion.
pause

:fin
endlocal
