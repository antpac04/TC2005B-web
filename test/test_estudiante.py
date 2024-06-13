import json
import pytest
from api.db import get_db

def test_login_estudiante(client, app):
    # Crear un estudiante en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Estudiante (numero_lista, genero, grupo) VALUES (%s, %s, %s)', (1, 'M', 'A'))
        db.commit()
        cursor.close()

    data = {
        "user": json.dumps({"numero_lista": 1, "grupo": "A"})
    }
    response = client.post('/api/estudiantes/login', data=data)
    assert response.status_code == 200
    assert response.is_json
    estudiante = response.get_json()
    assert estudiante['numero_lista'] == 1
    assert estudiante['grupo'] == 'A'

def test_registro_estudiante(client):
    data = {
        "user": json.dumps({"numero_lista": 2, "grupo": "B", "genero": "F"})
    }
    response = client.post('/api/estudiantes', data=data)
    assert response.status_code == 200
    assert response.is_json
    estudiante = response.get_json()
    assert estudiante['numero_lista'] == 2
    assert estudiante['grupo'] == 'B'
    assert estudiante['genero'] == 'F'

def test_update_estudiante(client, app):
    # Crear un estudiante en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Estudiante (numero_lista, genero, grupo) VALUES (%s, %s, %s)', (3, 'M', 'C'))
        db.commit()
        estudiante_id = cursor.lastrowid
        cursor.close()

    data = {
        "grupo": "D"
    }
    response = client.put(f'/api/estudiantes/{estudiante_id}', json=data)
    assert response.status_code == 200
    assert response.is_json
    status = response.get_json()
    assert status['estatus'] == 'Actualizado correctamente'

def test_delete_estudiante(client, app):
    # Crear un estudiante en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Estudiante (numero_lista, genero, grupo) VALUES (%s, %s, %s)', (4, 'F', 'E'))
        db.commit()
        estudiante_id = cursor.lastrowid
        cursor.close()

    response = client.delete(f'/api/estudiantes/{estudiante_id}')
    assert response.status_code == 200
    assert response.is_json
    status = response.get_json()
    assert status['estatus'] == 'Eliminado correctamente'