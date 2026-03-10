from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')

class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este usuario ya está registrado.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email ya está registrado.')

class PracticeForm(FlaskForm):
    quien = StringField('👤 QUIÉN')
    verbo = StringField('🎬 VERBO', validators=[DataRequired()])
    que = StringField('📦 QUÉ')
    a_quien = StringField('🎯 A QUIÉN')

class CreateExerciseForm(FlaskForm):
    contexto = SelectField('Contexto', choices=[
        ('academico', '📚 Académico'),
        ('laboral', '💼 Laboral'),
        ('cotidiano', '🏠 Cotidiano'),
        ('creativo', '🎨 Creativo'),
        ('social', '🌍 Social')
    ], validators=[DataRequired()])
    
    tiempo = SelectField('Tiempo Verbal', choices=[
        ('pasado', '⏪ Pasado'),
        ('presente', '⏺️ Presente'),
        ('futuro', '⏩ Futuro')
    ], validators=[DataRequired()])
    
    quien = StringField('👤 QUIÉN', validators=[DataRequired()])
    verbo = StringField('🎬 VERBO', validators=[DataRequired()])
    que = StringField('📦 QUÉ', validators=[DataRequired()])
    a_quien = StringField('🎯 A QUIÉN', validators=[DataRequired()])
    
    dificultad = SelectField('Dificultad', choices=[
        (1, '⭐ Básico'),
        (2, '⭐⭐ Intermedio'),
        (3, '⭐⭐⭐ Avanzado')
    ], coerce=int)
