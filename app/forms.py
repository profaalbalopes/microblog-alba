from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo
#from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    usuario = StringField("usuario", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired()])
    entrar = SubmitField("entrar")

class RegistrarForm(FlaskForm):
    usuario = StringField("usuario", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])
    senha = PasswordField("senha", validators=[InputRequired(), EqualTo("confirmarsenha", message="As senhas não conferem")])
    confirmarsenha = PasswordField("confirmarsenha", validators=[InputRequired()])
    registrar = SubmitField("registrar")