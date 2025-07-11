# conexion.py
import os
import mysql.connector

HOST = os.getenv("DB_HOST", "localhost")
USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASSWORD", "123456")
DB = os.getenv("DB_NAME", "testdb")

def obtener_conexion(nombre_bd: str | None = DB):
    """Devuelve una conexión a la BD indicada (o a la default)."""
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=nombre_bd
    )
