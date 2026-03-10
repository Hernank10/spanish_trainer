from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from datetime import datetime, timedelta
import json
import random

from config import Config
from models import db, User, Exercise, UserProgress, Score, CustomExercise
from forms import LoginForm, RegistrationForm, PracticeForm, CreateExerciseForm

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar extensiones
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Context processors
@app.context_processor
def utility_processor():
    return {
        'now': datetime.utcnow(),
        'enumerate': enumerate,
        'Config': Config
    }

# El resto de tu código de app.py continúa aquí...

# Comando para inicializar la base de datos
@app.cli.command("init-db")
def init_db_command():
    """Inicializar la base de datos con ejercicios."""
    import json
    from models import Exercise
    
    db.create_all()
    
    # Verificar si ya hay ejercicios
    if Exercise.query.first():
        print("✅ La base de datos ya tiene ejercicios.")
        return
    
    # Cargar ejercicios desde JSON
    try:
        with open('data/exercises.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for ex_data in data['exercises']:
            exercise = Exercise(
                sentence=ex_data['sentence'],
                quien=ex_data.get('quien', ''),
                verbo=ex_data['verbo'],
                que=ex_data.get('que', ''),
                a_quien=ex_data.get('a_quien', ''),
                contexto=ex_data.get('contexto', 'general'),
                tiempo_verbal=ex_data.get('tiempo_verbal', 'presente'),
                dificultad=ex_data.get('dificultad', 1),
                xp_reward=ex_data.get('xp_reward', 10)
            )
            db.session.add(exercise)
        
        db.session.commit()
        print(f'✅ Base de datos inicializada con {len(data["exercises"])} ejercicios.')
    except FileNotFoundError:
        print('⚠️ Archivo data/exercises.json no encontrado. Creando ejercicios por defecto...')
        # Crear ejercicios por defecto
        default_exercises = [
            {
                "sentence": "El profesor explicó la lección a los estudiantes",
                "quien": "El profesor",
                "verbo": "explicó",
                "que": "la lección",
                "a_quien": "a los estudiantes",
                "contexto": "academico",
                "tiempo_verbal": "pasado",
                "dificultad": 2,
                "xp_reward": 15
            },
            {
                "sentence": "La empresa lanzará un nuevo producto",
                "quien": "La empresa",
                "verbo": "lanzará",
                "que": "un nuevo producto",
                "a_quien": "",
                "contexto": "laboral",
                "tiempo_verbal": "futuro",
                "dificultad": 2,
                "xp_reward": 15
            }
        ]
        
        for ex_data in default_exercises:
            exercise = Exercise(**ex_data)
            db.session.add(exercise)
        
        db.session.commit()
        print(f'✅ Base de datos inicializada con {len(default_exercises)} ejercicios por defecto.')
    except Exception as e:
        print(f'❌ Error: {e}')

# Comando para inicializar la base de datos
@app.cli.command("init-db")
def init_db_command():
    """Inicializar la base de datos con ejercicios."""
    import json
    from models import Exercise
    
    db.create_all()
    
    # Verificar si ya hay ejercicios
    if Exercise.query.first():
        print("✅ La base de datos ya tiene ejercicios.")
        return
    
    # Intentar cargar desde JSON
    try:
        with open('data/exercises.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for ex_data in data['exercises']:
            exercise = Exercise(
                sentence=ex_data['sentence'],
                quien=ex_data.get('quien', ''),
                verbo=ex_data['verbo'],
                que=ex_data.get('que', ''),
                a_quien=ex_data.get('a_quien', ''),
                contexto=ex_data.get('contexto', 'general'),
                tiempo_verbal=ex_data.get('tiempo_verbal', 'presente'),
                dificultad=ex_data.get('dificultad', 1),
                xp_reward=ex_data.get('xp_reward', 10)
            )
            db.session.add(exercise)
        
        db.session.commit()
        print(f'✅ Base de datos inicializada con {len(data["exercises"])} ejercicios.')
    except FileNotFoundError:
        print('⚠️ No se encontró data/exercises.json. Usando ejercicios por defecto...')
        # Crear ejercicios por defecto
        default_exercises = [
            {
                "sentence": "El profesor explicó la lección a los estudiantes",
                "quien": "El profesor",
                "verbo": "explicó",
                "que": "la lección",
                "a_quien": "a los estudiantes",
                "contexto": "academico",
                "tiempo_verbal": "pasado",
                "dificultad": 2,
                "xp_reward": 15
            },
            {
                "sentence": "La empresa lanzará un nuevo producto",
                "quien": "La empresa",
                "verbo": "lanzará",
                "que": "un nuevo producto",
                "a_quien": "",
                "contexto": "laboral",
                "tiempo_verbal": "futuro",
                "dificultad": 2,
                "xp_reward": 15
            }
        ]
        
        for ex_data in default_exercises:
            exercise = Exercise(**ex_data)
            db.session.add(exercise)
        
        db.session.commit()
        print(f'✅ Base de datos inicializada con {len(default_exercises)} ejercicios por defecto.')
    except Exception as e:
        print(f'❌ Error: {e}')
