from config.db import db, app, ma

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lugar = db.Column(db.Integer, unique=True)
    sitios_cercanos