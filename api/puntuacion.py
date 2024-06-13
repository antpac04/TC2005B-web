# puntuacion.py
from flask import Blueprint, g, request, jsonify
import pytz
import datetime
import json
from .db import get_db

bp = Blueprint('puntuacion', __name__)

@bp.route('/api/puntuaciones', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        nivel = request.args.get('nivel')
        estudiante = request.args.get('estudiante')

        db = get_db()
        cursor = db.cursor(dictionary=True)
        if nivel and estudiante:
            cursor.execute('SELECT * FROM Puntuacion WHERE nivel = %s AND id_estudiante = %s', (nivel, estudiante))
        elif nivel:
            cursor.execute('SELECT * FROM Puntuacion WHERE nivel = %s', (nivel,))
        elif estudiante:
            cursor.execute('SELECT * FROM Puntuacion WHERE id_estudiante = %s', (estudiante,))
        else:
            cursor.execute('SELECT * FROM Puntuacion')

        results = cursor.fetchall()
        cursor.close()
        return jsonify(results)

    elif request.method == 'POST':
        try:
            data = request.form["puntuacion"]
            puntuacion = json.loads(data)
            nivel = puntuacion["nivel"]
            id_estudiante = puntuacion["id_estudiante"]
            valor = puntuacion["valor"]
        except KeyError as e:
            return jsonify({"error": f"Missing field: {e}"}), 400
        
        # Set current date
        mexico_tz = pytz.timezone('America/Mexico_City')
        fecha = datetime.datetime.now(mexico_tz).strftime("%Y-%m-%d %H:%M:%S")

        db = get_db()
        cursor = db.cursor()
        sql = 'INSERT INTO Puntuacion (valor, nivel, id_estudiante, fecha) VALUES (%s, %s, %s, %s)'
        val = (valor, nivel, id_estudiante, fecha)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return jsonify({"estatus": "Creado correctamente"})
