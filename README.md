# 🇪🇸 Entrenador de Español - Spanish Structure Trainer

Aplicación web interactiva para aprender las estructuras esenciales de las frases en español mediante un sistema de gamificación.

## ✨ Características

- 🎯 **100+ ejercicios** pre-cargados con diferentes contextos
- 📊 **Sistema de niveles y experiencia** (XP)
- 🏆 **Logros y medallas** desbloqueables
- 🔥 **Rachas de práctica** diarias
- 👥 **Sistema de usuarios** con perfiles personalizados
- 📈 **Ranking global** de puntuaciones
- ✍️ **Creación de ejercicios** personalizados
- 📱 **Diseño responsive** con Bootstrap 5

## 🚀 Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/spanish-trainer.git
cd spanish-trainer

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Edita .env con tus configuraciones

# Inicializar base de datos
flask init-db

# Ejecutar la aplicación
flask run --port 5001
