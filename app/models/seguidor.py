from app import db

class Seguidor(db.Model):
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    seguidor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    
    def __init__(self, usuario_id, seguidor_id):
        self.usuario_id = usuario_id
        self.seguidor_id = seguidor_id
        #usuario = db.relationship('Usuario')
        #usuario = db.relationship('Usuario')

    def __repr__(self):
        return "<Usuario: {}, Seguidor: {}>".format(self.usuario_id, self.seguidor_id)