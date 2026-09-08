#!/usr/bin/env bash

set -e

# Trabajar siempre desde la carpeta en la que se encuentra este iniciador.
DIRECTORIO_PROYECTO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIRECTORIO_PROYECTO"

ENTORNO_VIRTUAL=".venv"

if [ ! -d "$ENTORNO_VIRTUAL" ]; then
    echo "Creando el entorno virtual..."
    python3 -m venv "$ENTORNO_VIRTUAL"
fi

# Activar el entorno e instalar sólo las dependencias declaradas por el proyecto.
source "$ENTORNO_VIRTUAL/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Iniciando ML Visualizer 2.0..."
python main.py
