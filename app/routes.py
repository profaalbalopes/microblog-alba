from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Olá Mundo!"

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/outra')
def sobre():
    return "Aqui vai ter alguma coisa sobre o site"