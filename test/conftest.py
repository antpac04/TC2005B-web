# conftest.py
import os
import tempfile
import pytest
from api import create_app
from api.db import get_db, init_db

# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context():
        init_db()
        db = get_db()
        cursor = db.cursor()
        for result in cursor.execute(_data_sql, multi=True):
            if result.with_rows:
                result.fetchall()
        cursor.execute("SELECT * FROM Estudiante WHERE id = 1")
        student = cursor.fetchone()
        assert student is not None, "Estudiante no insertado correctamente en la base de datos de prueba."
        cursor.close()

    yield app

    os.close(db_fd)
    os.unlink(db_path)
    
@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, id=1, numero_lista=4, genero='Masculino', grupo='Grupo A'):
        return self._client.post(
            "/auth/login", data={"id": id, "numero_lista": numero_lista, "genero": genero, "grupo": grupo}
        )

    def logout(self):
        return self._client.get("/auth/logout")

@pytest.fixture
def auth(client):
    return AuthActions(client)
