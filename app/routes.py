from app import app
from flask import render_template
from flask import request, flash, redirect
from app.forms import LoginForm, RegistrarForm
from app.models.usuario import Usuario
from app import db

@app.route('/')
@app.route('/index/<nome>/<profissao>/<canal>')
@app.route('/index', defaults={"nome": "usuario", "profissao": "não informado", "canal":"não informado"})
def index(nome=None, profissao=None, canal=None):
    dados = {"profissao": profissao, "canal": canal}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = form.usuario.data
        senha = form.senha.data
        if usuario != 'admin' or senha != 'senha123':
            if (usuario == 'admin'):
                flash('O login está correto. ', "warning")
            else:
                flash('O login está incorreto. ', "danger")
            
            if (senha == 'senha123'):
                flash('A senha está correta. ', "warning")
            else:
                flash('A senha está incorreta. ', "danger")
            
            return redirect(url_for('/login'))
        
        return "{} - {}".format(usuario, senha)
    return render_template('login.html', form=form)

@app.route('/registrar', methods=['GET','POST'])
def registrar():
    form = RegistrarForm()
    if form.validate_on_submit():
        flash("Usuário registrado com sucesso", "success")
        return (redirect("/registrar"))
    elif len(form.errors.items()) > 0:
        for campo, mensagens in form.errors.items():
            for m in mensagens:
                flash(m, "danger")
        return (redirect("/registrar"))

    return render_template("registrar.html", form=form)


@app.route('/testebd')
def testebd():
    u = Usuario("Alba Lopes", "alba.lopes@ifrn.edu.br", '123456')
    db.session.add(u)
    db.session.commit()
    return "Dados inseridos"