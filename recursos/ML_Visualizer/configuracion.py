"""Lectura y escritura de configuraciones JSON de ML Visualizer."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


# -----------------------------------------------------------------------------
# Carga desde disco una configuración JSON y valida su estructura principal.
# -----------------------------------------------------------------------------
def cargar_json(ruta: str | Path) -> dict[str, Any]:
    """Lee una configuración y verifica que el nivel superior sea un objeto JSON."""

    ruta = Path(ruta)
    with ruta.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, dict):
        raise ValueError("El archivo no contiene una configuración válida.")  # noqa: TRY004
    return datos


# -----------------------------------------------------------------------------
# Guarda una configuración JSON legible, preservando tildes y caracteres Unicode.
# -----------------------------------------------------------------------------
def guardar_json(ruta: str | Path, datos: dict[str, Any]) -> None:
    """Guarda una configuración legible y compatible con caracteres españoles."""

    ruta = Path(ruta)
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)
        archivo.write("\n")
