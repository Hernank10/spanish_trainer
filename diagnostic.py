#!/usr/bin/env python
import os
import sys

print("="*50)
print("DIAGNÓSTICO DEL SISTEMA")
print("="*50)

print(f"\nDirectorio actual: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

print("\nPYTHONPATH:")
for path in sys.path:
    print(f"  {path}")

print("\nArchivos .py en directorio actual:")
for file in os.listdir('.'):
    if file.endswith('.py'):
        size = os.path.getsize(file)
        print(f"  {file} ({size} bytes)")

print("\nIntentando importaciones:")
try:
    import config
    print(f"✅ config importado desde: {config.__file__}")
except ImportError as e:
    print(f"❌ config: {e}")

try:
    from config import Config
    print("✅ Config clase importada")
except ImportError as e:
    print(f"❌ Config: {e}")

try:
    import models
    print(f"✅ models importado desde: {models.__file__}")
except ImportError as e:
    print(f"❌ models: {e}")

print("\nVerificando contenido de config.py:")
if os.path.exists('config.py'):
    with open('config.py', 'r') as f:
        content = f.read()
        print(f"config.py existe y tiene {len(content)} caracteres")
        print("Primeras 3 líneas:")
        for i, line in enumerate(content.split('\n')[:3]):
            print(f"  {i+1}: {line}")
else:
    print("❌ config.py NO existe")
