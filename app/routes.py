from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Lopes"
    dados = {"profissao": "Professora", "canal": "Profa. Alba Lopes"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/outra')
def sobre():
    return "Aqui vai ter alguma coisa sobre o site"