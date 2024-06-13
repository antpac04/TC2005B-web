import json
import pytest
from api.db import get_db

def test_login_admin(client, app):
    # Crear un admin en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Admin (nombre_usuario, contrasena) VALUES (%s, %s)', ('admin1', 'password1'))
        db.commit()
        cursor.close()

    data = {
        "nombre_usuario": "admin1",
        "contrasena": "password1"
    }
    response = client.post('/api/admins/login', json=data)
    assert response.status_code == 200
    assert response.is_json
    resultado = response.get_json()
    assert resultado['valido'] is True

def test_register_admin(client):
    data = {
        "nombre_usuario": "admin2",
        "contrasena": "password2"
    }
    response = client.post('/api/admins', json=data)
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Creado correctamente'

def test_modificar_admin(client, app):
    # Crear un admin en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Admin (nombre_usuario, contrasena) VALUES (%s, %s)', ('admin3', 'password3'))
        db.commit()
        admin_id = cursor.lastrowid
        cursor.close()

    data = {
        "contrasena": "newpassword3"
    }
    response = client.put(f'/api/admins/{admin_id}', json=data)
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Actualizado correctamente'

def test_delete_admin(client, app):
    # Crear un admin en la base de datos de prueba usando data.sql o aquí
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Admin (nombre_usuario, contrasena) VALUES (%s, %s)', ('admin4', 'password4'))
        db.commit()
        admin_id = cursor.lastrowid
        cursor.close()

    response = client.delete(f'/api/admins/{admin_id}')
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Eliminado correctamente'