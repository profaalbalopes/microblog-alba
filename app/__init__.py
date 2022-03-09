from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha-chave-secreta"

conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#login_manager = LoginManager()
#login_manager.init_app(app)

from app import routes