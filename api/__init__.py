# __init__.py
from flask import Flask
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from . import db
from . import puntuacion
from . import maestro
from . import estudiante
from . import admin

load_dotenv()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # load default configuration
    app.config.from_mapping(
        SECRET_KEY=environ.get('SECRET_KEY'),
        DB_HOST=environ.get('DB_HOST'),
        DB_USER=environ.get('DB_USER'),
        DB_PASSWORD=environ.get('DB_PASSWORD'),
        DB_DATABASE=environ.get('DB_DATABASE')
    )

    if test_config is not None:
        # load the test config if passed in
        app.config.update(test_config)

    # initialize database
    db.init_app(app)

    # register blueprints
    app.register_blueprint(puntuacion.bp)
    app.register_blueprint(maestro.bp)
    app.register_blueprint(estudiante.bp)
    app.register_blueprint(admin.bp)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
