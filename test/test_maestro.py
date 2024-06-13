import json
import pytest
from api.db import get_db

def test_login_maestro(client, app):
    # Crear un maestro en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Maestro (nombre_usuario, contrasena) VALUES (%s, %s)', ('maestro1', 'password1'))
        db.commit()
        cursor.close()

    data = {
        "nombre_usuario": "maestro1",
        "contrasena": "password1"
    }
    response = client.post('/api/maestros/login', json=data)
    assert response.status_code == 200
    assert response.is_json
    resultado = response.get_json()
    assert resultado['valido'] is True

def test_registro_maestro(client):
    data = {
        "nombre_usuario": "maestro2",
        "contrasena": "password2"
    }
    response = client.post('/api/maestros/', json=data)
    assert response.status_code == 201
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Creado correctamente'

def test_modificar_maestro(client, app):
    # Crear un maestro en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Maestro (nombre_usuario, contrasena) VALUES (%s, %s)', ('maestro3', 'password3'))
        db.commit()
        maestro_id = cursor.lastrowid
        cursor.close()

    data = {
        "contrasena": "newpassword3"
    }
    response = client.put(f'/api/maestros/{maestro_id}', json=data)
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Actualizado correctamente'

def test_delete_maestro(client, app):
    # Crear un maestro en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Maestro (nombre_usuario, contrasena) VALUES (%s, %s)', ('maestro4', 'password4'))
        db.commit()
        maestro_id = cursor.lastrowid
        cursor.close()

    response = client.delete(f'/api/maestros/{maestro_id}')
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Eliminado correctamente'