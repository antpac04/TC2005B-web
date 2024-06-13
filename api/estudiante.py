from flask import Blueprint, g, request, jsonify
from .db import get_db
import json

bp = Blueprint('estudiante', __name__)

@bp.route('/api/estudiantes/login', methods=['POST'])
def LogIn_estudiante():
    data = request.form["user"]
    user = json.loads(data)

    numero_lista = user["numero_lista"] 
    grupo = user["grupo"] 

    if numero_lista is None or grupo is None:
        return jsonify({'error': 'Se requieren número de lista y grupo'}), 400

    db = get_db()
    cursor = db.cursor()

    cursor.execute('SELECT * FROM Estudiante WHERE numero_lista = %s AND grupo = %s', (numero_lista, grupo))
    estudiante = cursor.fetchone()
    column_names = [desc[0] for desc in cursor.description]

    cursor.close()

    if estudiante:
        estudiante_dict = dict(zip(column_names, estudiante))
        return jsonify(estudiante_dict), 200
    else:
        return jsonify({'valido': False}), 404

@bp.route('/api/estudiantes', methods=['POST'])
def registro_estudiante():
     if request.method == 'POST':
        data = request.form["user"]
        user = json.loads(data)
        numero_lista = user["numero_lista"]
        grupo = user["grupo"] 
        genero = user["genero"]

        if numero_lista is None or grupo is None or genero is None:
            return jsonify({'error': 'Se requieren todos los campos'}), 400

        db = get_db()
        cursor = db.cursor()

        cursor.execute('INSERT INTO Estudiante (numero_lista, grupo, genero) VALUES (%s, %s, %s)', (numero_lista, grupo, genero))
        db.commit()

        cursor.execute('SELECT LAST_INSERT_ID()')
        last_id = cursor.fetchone()[0]
        cursor.close()

        user['id'] = last_id
        return jsonify(user), 200


@bp.route('/api/estudiantes/<int:id>', methods=['PUT', 'DELETE'])
def update_or_delete_student(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'PUT':
        grupo = request.json.get('grupo')
        sql = 'UPDATE Estudiante SET grupo = %s WHERE id = %s'
        cursor.execute(sql, (grupo, id))
        db.commit()
        cursor.close()
        return jsonify({"estatus": "Actualizado correctamente"})
    elif request.method == 'DELETE':
        sql = 'DELETE FROM Estudiante WHERE id = %s'
        cursor.execute(sql, (id,))
        db.commit()
        cursor.close()
        return jsonify({"estatus": "Eliminado correctamente"})