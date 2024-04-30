from config.db import db, app, ma 
from models.Producto import Producto, ProductoSchema
from flask import Flask, Blueprint, request, render_template, jsonify, json

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

ruta_producto = Blueprint('route_producto', __name__)

@ruta_producto('/cproducto', methods='POST')
def create_product():
    tipo = request.json[tipo]
    estado = request.json[estado]
    
    return 

@app.route('/gproducts', methods=['POST', 'GET'] )
def get_produts():
    result = db.session.query(Producto).all()
    data = {}
    
    i=0
    for product in result:
        i+=1
        data[i] = {
            'tipo': product.tipo,
            'estado': product.estado
        }
    return jsonify(data)

@app.route('/gproduct/<id>', methods=[ 'GET'])
def get_product(id):
    result = db.session.query(Producto).get(id)
    