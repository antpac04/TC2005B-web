from flask import Blueprint, g, request, jsonify
from .db import get_db


bp = Blueprint('admin', __name__)

@bp.route('/api/admins/login', methods=['POST'])
def login_admin():
    db = get_db()
    cursor = db.cursor()

    nombre_usuario = request.json.get('nombre_usuario')
    contrasena = request.json.get('contrasena')

    # Suponiendo que tienes una tabla llamada 'admins' con columnas 'nombre_usuario' y 'contrasena'
    sql = 'SELECT * FROM Admin WHERE nombre_usuario = %s AND contrasena = %s'
    cursor.execute(sql, (nombre_usuario, contrasena))
    admin = cursor.fetchone()

    if admin:
        cursor.close()
        return jsonify({"valido": True})
    else:
        cursor.close()
        return jsonify({"valido": False})

@bp.route('/api/admins', methods=['POST'])
def register_admin():
    db = get_db()
    cursor = db.cursor()

    nombre_usuario = request.json.get('nombre_usuario')
    contrasena = request.json.get('contrasena')

   
    sql = 'INSERT INTO Admin (nombre_usuario, contrasena) VALUES (%s, %s)'
    cursor.execute(sql, (nombre_usuario, contrasena))
    db.commit()
    cursor.close()

    return jsonify({"estatus": "Creado correctamente"})

@bp.route('/api/admins/<int:id>', methods=['PUT'])
def modificar_admin(id):
    db = get_db()
    cursor = db.cursor()

    contrasena = request.json.get('contrasena')
    cursor.execute('UPDATE Admin SET contrasena =%s WHERE id =%s',(contrasena,id))
    db.commit()
    cursor.close()

    return jsonify({'estatus':"Actualizado correctamente"})

@bp.route('/api/admins/<int:id>', methods=['PUT', 'DELETE'])
def delete_admin(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'DELETE':
        sql = 'DELETE FROM Admin WHERE id = %s'
        cursor.execute(sql, (id,))
        db.commit()
        cursor.close()

        return jsonify({"estatus": "Eliminado correctamente"})
    elif request.method == 'PUT':
        nombre_usuario = request.json.get('nombre_usuario')
        contrasena = request.json.get('contrasena')

        sql = 'UPDATE Admin SET nombre_usuario = %s, contrasena = %s WHERE id = %s'
        cursor.execute(sql, (nombre_usuario, contrasena, id))
        db.commit()
        cursor.close()

        return jsonify({"estatus": "Actualizado correctamente"})
