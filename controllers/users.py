from flask import Flask, Blueprint, request, render_template, jsonify, json, redirect, url_for
from config.db import db, ma, app
from werkzeug.security import generate_password_hash

from models.users import Users, UsersSchema

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

ruta_user = Blueprint('route_user', __name__)

#Se define la ruta que devuelva la pagina de los usuarios
@ruta_user.route('/user', methods=['GET'])
def indexuser():
    return render_template('')

#Ruta para crear los usuarios
@app.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password,
                    )

                    db.session.add(new_user)
                    db.session.commit()
                except:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                return redirect(url_for('login.show') + '?success=account-created')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')

#Ruta para obtener todos los usuarios
@ruta_user.route('/ouser', methods=['GET'])
def get_users():
    #SELECT * FROM USERS
    result = db.session.query(Users).all()
    data = {}
    
    i=0
    for user in result:
        i+=1
        
        data[i]={
            'nombre': user.nombre,
            'usuario': user.usuario
        }
    return jsonify(data)

@ruta_user.route('/uuser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    Usuario = db.session.query(Users).get(user_id)
    if not Usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    
    usuario = request.json['usuario']
    nombre = request.json['nombre']
    
    #Se verifica que los datos no esten vacios
    if not nombre:
        return jsonify({'message': 'Nombre es requerido'}), 400
    if not usuario:
        return jsonify({'message': 'Usuario es requerido'}), 400
    
    Usuario.nombre = nombre
    Usuario.usuario = usuario    
    
    #Se agregan los cambios a la base de datos
    db.session.commit()
    return { 'message': 'Usuario actualizdo' }

@ruta_user.route('/duser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    Usuario = db.session.query(Users).get(user_id)
    #Se verifica que exista este usuario
    if Usuario is None:
        return jsonify({'message': 'User no encontrado'}), 404
    
    db.session.delete(Usuario)
    db.session.commit()
    return { 'message': 'Usuario eliminado' }

@ruta_user.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.query(Users).get(user_id)
    if user:
        return jsonify({'nombre': user.nombre, 'usuario': user.usuario})
    else:
        return jsonify({'message': 'User not found'}), 404
