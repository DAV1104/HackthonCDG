from config.db import db, app, ma
from sqlalchemy.orm import relationship, backref

class Ubicacion(db.Model):
    __tablename__ = 'ubication'
    
    id = db.Column(db.Integer, primary_key=True)
    lugar = db.Column(db.Integer)
    sitios_cercanos = db.Column(relationship('sitios_cercanos', backref='ubicacion'))
    
    def __init__(self, id, lugar):
        self.id = id
        self.lugar = lugar
        
with app.app_context():
    db.create_all()

class UbicacionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'lugar')