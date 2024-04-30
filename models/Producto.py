from config.db import db, app, ma
from sqlalchemy import ForeignKey

class Producto(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))
    estado = db.Column(db.String(255))
    solicitud_id = db.relationship('requests', backref='producto')
    usuario_id = db.Column(db.Integer, ForeignKey('usuario.id'))
    
    def __init__(self, tipo, estado):
        self.id = id
        self.tipo = tipo
        self.estado = estado

with app.app_context():
    db.create_all

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('tipo', 'estado')