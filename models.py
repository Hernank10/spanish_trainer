from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import json

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    
    # Sistema de progreso
    total_xp = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    exercises_completed = db.Column(db.Integer, default=0)
    perfect_exercises = db.Column(db.Integer, default=0)
    current_streak = db.Column(db.Integer, default=0)
    longest_streak = db.Column(db.Integer, default=0)
    last_practice_date = db.Column(db.DateTime)
    
    # Estadísticas
    total_time_practiced = db.Column(db.Integer, default=0)
    average_score = db.Column(db.Float, default=0.0)
    favorite_context = db.Column(db.String(50))
    
    # Medallas (JSON)
    achievements = db.Column(db.Text, default='[]')
    
    # Relaciones
    progress = db.relationship('UserProgress', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    scores = db.relationship('Score', backref='user', lazy='dynamic')
    custom_exercises = db.relationship('CustomExercise', backref='creator', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def add_xp(self, xp_amount):
        self.total_xp += xp_amount
        self.update_level()
    
    def update_level(self):
        new_level = 1 + int(self.total_xp / 100)
        if new_level > self.level:
            self.level = min(new_level, 50)
            return True
        return False
    
    def update_streak(self):
        today = datetime.utcnow().date()
        if self.last_practice_date:
            last_date = self.last_practice_date.date()
            if last_date == today - timedelta(days=1):
                self.current_streak += 1
            elif last_date < today - timedelta(days=1):
                self.current_streak = 1
        else:
            self.current_streak = 1
        
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
        
        self.last_practice_date = datetime.utcnow()
    
    def get_achievements_list(self):
        if self.achievements:
            return json.loads(self.achievements)
        return []
    
    def get_next_level_xp(self):
        return (self.level * 100) - self.total_xp
    
    def get_level_progress(self):
        current_level_xp = (self.level - 1) * 100
        xp_in_level = self.total_xp - current_level_xp
        return (xp_in_level / 100) * 100

class Exercise(db.Model):
    __tablename__ = 'exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(300), nullable=False)
    quien = db.Column(db.String(100))
    verbo = db.Column(db.String(100), nullable=False)
    que = db.Column(db.String(200))
    a_quien = db.Column(db.String(200))
    contexto = db.Column(db.String(50))
    tiempo_verbal = db.Column(db.String(20))
    dificultad = db.Column(db.Integer, default=1)
    xp_reward = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Estadísticas
    times_completed = db.Column(db.Integer, default=0)
    average_score = db.Column(db.Float, default=0.0)
    
    def get_components(self):
        return {
            'quien': self.quien or '',
            'verbo': self.verbo,
            'que': self.que or '',
            'a_quien': self.a_quien or ''
        }
    
    def calculate_xp(self, score):
        base_xp = self.xp_reward
        multiplier = 1.0
        
        if score == 4:
            multiplier = 1.5
        elif score == 3:
            multiplier = 1.2
        
        return int(base_xp * multiplier)

class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    score = db.Column(db.Integer)
    xp_earned = db.Column(db.Integer)
    time_spent = db.Column(db.Integer)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    attempts = db.Column(db.Integer, default=1)

class Score(db.Model):
    __tablename__ = 'scores'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CustomExercise(db.Model):
    __tablename__ = 'custom_exercises'
    
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(300), nullable=False)
    quien = db.Column(db.String(100))
    verbo = db.Column(db.String(100), nullable=False)
    que = db.Column(db.String(200))
    a_quien = db.Column(db.String(200))
    contexto = db.Column(db.String(50))
    tiempo_verbal = db.Column(db.String(20))
    dificultad = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_public = db.Column(db.Boolean, default=True)
    likes = db.Column(db.Integer, default=0)
