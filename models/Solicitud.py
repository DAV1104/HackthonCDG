from config.db import db, ma, app
from sqlalchemy import ForeignKey
from datetime import date
import datetime

class Solicitud(db.Model):
    __tablename__ = 'requests'
    
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.Integer, ForeignKey('producto.id'))
    usuario_id = db.Column(db.String, ForeignKey('usuario.id'))
    fecha = db.Column(db.Date, default=date.today())
    hora = db.Column(db.DateTime, default=datetime.datetime.now.hour)
    
    def __init__(self, id, producto, usuario_id, fecha, hora):
        self.id = id
        self.producto = producto
        self.usuario_id = usuario_id
        self.fecha = fecha
        self.hora = hora
        
with app.app_context:
    db.create_all()

class SolicitudSchema(ma.Schema):
    class Meta:
        fields = ('id', 'producto', 'usuario_id', 'fecha', 'hora')

solicitud_schema = SolicitudSchema()
solicitudes_schema = SolicitudSchema(many=True)