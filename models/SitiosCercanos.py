from config.db import db, ma, app
from sqlalchemy import ForeignKey

class SitiosCercanos(db.Model):
    __tablename__ = 'near_sites'
    
    id = db.Column(db.String(255))
    lugar = db.Column(db.String(255))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'))
    
    def __init__(self, id, lugar):
        self.id = id
        self.lugar = lugar
        
with app .app_context:
    db.create_all()
    
class SitiosCercanosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'lugar', 'ubicacion_id')