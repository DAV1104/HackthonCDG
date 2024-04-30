from config.db import db, app, ma

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))
    estado = db.Column(db.String(255))
    
    def __init__(self,  id, tipo, estado):
        self.id = id
        self.tipo = tipo
        self.estado = estado

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipo', 'estado')