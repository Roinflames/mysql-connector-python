# bd_ops.py
from conexion import obtener_conexion

def crear_base_datos(nombre: str):
    cnx = obtener_conexion(None)       # conectar sin BD
    cur = cnx.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {nombre}")
    cnx.close()
    print(f"Base de datos '{nombre}' creada / ya existía.")


def eliminar_base_datos(nombre: str):
    cnx = obtener_conexion(None)
    cur = cnx.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {nombre}")
    cnx.close()
    print(f"Base de datos '{nombre}' eliminada (si existía).")


def ver_bases_datos():
    cnx = obtener_conexion(None)
    cur = cnx.cursor()
    cur.execute("SHOW DATABASES")
    print("\n--- Bases de datos disponibles ---")
    for (db,) in cur.fetchall():
        print(f"- {db}")
    cur.close()
    cnx.close()
