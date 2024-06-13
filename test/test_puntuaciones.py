import json
import pytest
from api.db import get_db

def test_get_puntuaciones(client, app):
    # Crear datos de prueba para puntuaciones
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Estudiante (numero_lista, genero, grupo) VALUES (%s, %s, %s)', (1, 'M', 'A'))
        db.commit()
        estudiante_id = cursor.lastrowid
        cursor.execute('INSERT INTO Puntuacion (valor, nivel, id_estudiante, fecha) VALUES (%s, %s, %s, %s)', (90, 1, estudiante_id, '2023-01-01 00:00:00'))
        db.commit()
        
        # Verificar la inserción de los datos directamente en la base de datos
        cursor.execute('SELECT * FROM Puntuacion WHERE nivel = %s AND id_estudiante = %s', (1, estudiante_id))
        inserted_puntuaciones = cursor.fetchall()
        assert len(inserted_puntuaciones) == 1

        cursor.close()

    response = client.get(f'/api/puntuaciones?nivel=1&estudiante={estudiante_id}')
    assert response.status_code == 200
    assert response.is_json
    puntuaciones = response.get_json()
    assert len(puntuaciones) == 1
    assert puntuaciones[0]['valor'] == 90
    assert puntuaciones[0]['nivel'] == 1
    assert puntuaciones[0]['id_estudiante'] == estudiante_id

def test_post_puntuacion(client, app):
    # Crear un estudiante en la base de datos de prueba
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Estudiante (numero_lista, genero, grupo) VALUES (%s, %s, %s)', (2, 'F', 'B'))
        db.commit()
        estudiante_id = cursor.lastrowid
        cursor.close()

    data = {
        "puntuacion": json.dumps({
            "valor": 85,
            "nivel": 2,
            "id_estudiante": estudiante_id
        })
    }
    response = client.post('/api/puntuaciones', data=data)
    assert response.status_code == 200
    assert response.is_json
    estatus = response.get_json()
    assert estatus['estatus'] == 'Creado correctamente'

    # Verificar que la puntuación se haya insertado correctamente
    with app.app_context():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Puntuacion WHERE id_estudiante = %s AND nivel = %s', (estudiante_id, 2))
        puntuacion = cursor.fetchone()
        cursor.close()
        assert puntuacion is not None
        assert puntuacion['valor'] == 85
        assert puntuacion['nivel'] == 2
        assert puntuacion['id_estudiante'] == estudiante_id

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

