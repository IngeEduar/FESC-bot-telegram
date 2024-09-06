import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="nombre_basedatos",
        user="usuario",
        password="contraseña"
    )
    return connection
