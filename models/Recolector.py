from config.db import db, app, ma

class Recolector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    