import os
from datetime import timedelta

# Obtener la ruta absoluta del directorio actual
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{os.path.join(basedir, "instance", "spanish_trainer.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración de sesión
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Niveles y experiencia
    XP_PER_LEVEL = 100
    MAX_LEVEL = 50
    
    # Medallas
    ACHIEVEMENTS = {
        'first_exercise': {'name': 'Primer Paso', 'description': 'Completa tu primer ejercicio', 'icon': '🎯', 'xp': 50},
        'perfect_score': {'name': 'Perfecto', 'description': 'Obtén 4/4 en un ejercicio', 'icon': '💯', 'xp': 100},
        'streak_7': {'name': 'Racha de 7 días', 'description': 'Practica 7 días seguidos', 'icon': '🔥', 'xp': 200},
        'streak_30': {'name': 'Racha de 30 días', 'description': 'Practica 30 días seguidos', 'icon': '⚡', 'xp': 500},
        'master_beginner': {'name': 'Aprendiz', 'description': 'Completa 10 ejercicios', 'icon': '🌱', 'xp': 150},
        'master_intermediate': {'name': 'Intermedio', 'description': 'Completa 50 ejercicios', 'icon': '🌿', 'xp': 300},
        'master_advanced': {'name': 'Avanzado', 'description': 'Completa 100 ejercicios', 'icon': '🌳', 'xp': 500},
        'master_expert': {'name': 'Experto', 'description': 'Completa 200 ejercicios', 'icon': '🏆', 'xp': 1000},
        'perfectionist': {'name': 'Perfeccionista', 'description': '10 ejercicios perfectos', 'icon': '✨', 'xp': 400},
    }
