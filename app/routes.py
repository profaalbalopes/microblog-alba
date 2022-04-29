from app import app, db
from flask import render_template
from flask import request, flash, redirect
from app.forms import LoginForm, RegistrarForm
from app.models.usuario import Usuario
from app.models.postagem import Postagem
from app.models.seguidor import Seguidor

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
        usuario = Usuario.query.filter_by(email=form.usuario.data).first()
        if usuario and usuario.senha == form.senha.data:
            flash('O login está correto. ', "warning")
        else:
            flash('O login está incorreto. ', "danger")
            return redirect('/login')
        
        return "{} - {}".format(usuario.nome, usuario.senha)
    return render_template('login.html', form=form)

@app.route('/registrar', methods=['GET','POST'])
def registrar():
    form = RegistrarForm()
    if form.validate_on_submit():
        u = Usuario(form.usuario.data, form.email.data, form.senha.data)
        db.session.add(u)
        db.session.commit()
        flash("Usuário registrado com sucesso", "success")
        return (redirect("/registrar"))
    elif len(form.errors.items()) > 0:
        for campo, mensagens in form.errors.items():
            for m in mensagens:
                flash(m, "danger")
        return (redirect("/registrar"))

    return render_template("registrar.html", form=form)

@app.route('/testedb_insert')
def testedb_insert():
    u = Usuario("Alba Lopes", "alba.lopes@ifrn.edu.br", "123456")
    db.session.add(u)
    db.session.commit()
    return "Dados inseridos com sucesso!"

@app.route('/testedb_select')
def testedb_select():
    u = Usuario.query.get(1)
    print(u)
    return "Dados impressos no terminal"

@app.route('/testedb_update')
def testedb_update():
    u = Usuario.query.get(1)
    u.nome = "Alba L."
    print(u)
    db.session.add(u)
    db.session.commit()
    return "Dados atualizados com sucesso!"

@app.route('/testedb_delete')
def testedb_delete():
    u = Usuario.query.get(1)
    db.session.delete(u)
    db.session.commit()
    return "Dados excluídos com sucesso!"

@app.route('/listar_usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    for u in usuarios:
        print(u.nome)
    
    return render_template('listar_usuarios.html', usuarios=usuarios)

@app.route('/excluir_usuario/<id>')
def excluir_usuario(id):
    u = Usuario.query.get(id)
    db.session.delete(u)
    db.session.commit()

    return redirect('/listar_usuarios')
