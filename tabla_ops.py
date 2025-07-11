# tabla_ops.py
from conexion import obtener_conexion

def crear_tabla():
    cnx = obtener_conexion()
    cur = cnx.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            rol ENUM('Administrador','MandosMedios','Gerencia') NOT NULL
        )
    """)
    cnx.close()
    print("Tabla 'usuarios' creada / ya existía.")


def eliminar_tabla():
    cnx = obtener_conexion()
    cur = cnx.cursor()
    cur.execute("DROP TABLE IF EXISTS usuarios")
    cnx.close()
    print("Tabla 'usuarios' eliminada (si existía).")
