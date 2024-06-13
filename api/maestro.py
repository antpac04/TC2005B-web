from flask import Blueprint, g, request, jsonify
from .db import get_db

bp = Blueprint('maestro', __name__)


@bp.route('/api/maestros/login', methods=['POST'])
def LogIn_maestro():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    contrasena = data.get('contrasena')

    if nombre_usuario is None or contrasena is None:
        return jsonify({'error':"No deje ningun campo vacio"})
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Maestro WHERE nombre_usuario = %s AND contrasena = %s', (nombre_usuario,contrasena))
    maestro = cursor.fetchone()
    cursor.close()

    if maestro:
        return jsonify({'valido': True})
    else:
        return jsonify({'valido': False})


@bp.route('/api/maestros/', methods=['POST'])
def registro_maestro():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    contrasena = data.get('contrasena')

    if nombre_usuario is None or contrasena is None:
        return jsonify({'error': 'No deje ningun campo vacio'}), 400
    
    db = get_db()
    cursor = db.cursor()

    cursor.execute('INSERT INTO Maestro (nombre_usuario, contrasena) VALUES (%s, %s)', (nombre_usuario, contrasena))
    db.commit()
    cursor.close()

    return jsonify({'estatus': 'Creado correctamente'}), 201


@bp.route('/api/maestros/<int:id>', methods=['PUT'])
def modificar_maestro(id):
    db = get_db()
    cursor = db.cursor()
    contrasena = request.json.get('contrasena')
    cursor.execute('UPDATE Maestro SET contrasena = %s WHERE id = %s', (contrasena,id))
    db.commit()
    cursor.close()

    return jsonify({'estatus':"Actualizado correctamente"})


@bp.route('/api/maestros/<int:id>', methods=['DELETE'])
def delete(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM Maestro WHERE id = %s', (id,))
    db.commit()
    cursor.close()

    return jsonify({"estatus": "Eliminado correctamente"})
