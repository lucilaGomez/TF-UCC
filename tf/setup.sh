#!/bin/bash

echo "==> Eliminando entorno virtual antiguo (si existe)..."
rm -rf venv

echo "==> Creando nuevo entorno virtual..."
python3 -m venv venv
source venv/bin/activate

echo "==> Actualizando pip, setuptools y wheel..."
pip install --upgrade pip setuptools wheel

echo "==> Desinstalando posibles versiones conflictivas..."
pip uninstall -y pydantic pydantic-settings spacy thinc numpy

echo "==> Instalando versiones compatibles:"
pip install pydantic==1.10.2
pip install numpy==1.24.3
pip install spacy==3.5.4
pip install thinc==8.1.12

echo "==> Instalando resto de dependencias desde requirements.txt..."
pip install -r requirements.txt

echo "==> Descargando modelo SpaCy para español..."
python -m spacy download es_core_news_sm

echo "==> Instalación y configuración completada."
echo "==> No olvides activar el entorno virtual con 'source venv/bin/activate' antes de correr tu app."

