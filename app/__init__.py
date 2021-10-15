from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha-chave-secreta"

#CONEXÃO COM O BD
usuario = "profaa16_teste"
senha = "minhasenhasecreta"
servidor = "profaalbalopes.info"
banco = "profaa16_psi21_alba"

conexao = "mysql://{0}:{1}@{2}/{3}".format(usuario, senha, servidor, banco)
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes