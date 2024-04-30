from config.db import db, ma, app
from sqlalchemy.orm import relationship, backref

class Users(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    usuario = db.Column(db.String(255))
    contraseña = db.Column(db.String(255))
    productos = db.relationship('product', backref='usario')
    solicitudes = db.relationship('solicitudes', backref='usuario')
    
    def __init__ (self, nombre, usuario, contraseña):
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        
with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'usuario', 'contraseña')

users_schema = UsersSchema(many = True)
user_schema = UsersSchema()