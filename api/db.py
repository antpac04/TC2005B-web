from flask import current_app, g
import mysql.connector
import click

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE']
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None and db.is_connected():
        db.close()

def init_db():
    db = get_db()
    cursor = db.cursor()

    # Disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS puntuacion")
    cursor.execute("DROP TABLE IF EXISTS estudiante")
    cursor.execute("DROP TABLE IF EXISTS maestro")
    cursor.execute("DROP TABLE IF EXISTS admin")

    # Enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    with current_app.open_resource('schema.sql') as f:
        sql_script = f.read().decode('utf8')
        for result in cursor.execute(sql_script, multi=True):
            if result.with_rows:
                result.fetchall()

    db.commit()
    cursor.close()

@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def seed_db():
    db = get_db()
    cursor = db.cursor()

    # Disable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS puntuacion")
    cursor.execute("DROP TABLE IF EXISTS estudiante")
    cursor.execute("DROP TABLE IF EXISTS maestro")
    cursor.execute("DROP TABLE IF EXISTS admin")

    # Enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    with current_app.open_resource('schema.sql') as f:
        sql_script = f.read().decode('utf8')
        for result in cursor.execute(sql_script, multi=True):
            if result.with_rows:
                result.fetchall()

    db.commit()
    cursor.close()

@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by the application factory."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)