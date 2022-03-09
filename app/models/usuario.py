from app import db

class Usuario(db.Model):
    __tablename__="usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return "<Usuario: {}, Email: {}>".format(self.nome, self.email)