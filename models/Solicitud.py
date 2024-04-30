from config.db import db, ma, app

class Solicitud(db.Model):
    __tablename__ = 'solicitud'
    
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.Integer, db.ForeignKey('producto.id'))