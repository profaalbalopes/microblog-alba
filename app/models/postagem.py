from app import db

class Postagem(db.Model):
    __tablename__="postagem"
    id = db.Column(db.Integer, primary_key=True)
    postagem = db.Column(db.String)
    data = db.Column(db.DateTime)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario')

    def __init__(self, postagem, data, usuario_id):
        self.postagem = postagem
        self.data = data
        self.usuario_id = usuario_id

    def __repr__(self):
        return "<Postagem: {}, Data: {}, Usuario: {}>".format(self.postagem, self.data, self.usuario_id)