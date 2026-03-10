#!/bin/bash

echo "🚀 Instalando Spanish Trainer App..."

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Inicializar base de datos
export FLASK_APP=app.py
flask init-db

echo "✅ Instalación completada!"
echo "📝 Para ejecutar: flask run"
echo "🌐 Abrir navegador en: http://localhost:5000"
