# usuario_ops.py
import getpass
import bcrypt
from conexion import obtener_conexion

def insertar_usuario():
    nombre = input("Nombre: ").strip()
    password = getpass.getpass("Contraseña: ").encode("utf-8")
    rol = input("Rol: ").strip()
    pwd_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    cnx = obtener_conexion()
    cur = cnx.cursor()
    cur.execute(
        "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s, %s, %s)",
        (nombre, pwd_hash, rol)
    )
    cnx.commit()
    cur.close()
    cnx.close()
    print(f"Usuario '{nombre}' insertado.")


def consultar_usuarios():
    cnx = obtener_conexion()
    cur = cnx.cursor(dictionary=True)
    cur.execute("SELECT id, username, rol FROM usuarios")
    registros = cur.fetchall()
    cur.close()
    cnx.close()

    if registros:
        print("\n--- Lista de usuarios ---")
        for r in registros:
            print(f"{r['id']:3} | {r['username']:<15} | {r['rol']}")
    else:
        print("No hay usuarios registrados.")
