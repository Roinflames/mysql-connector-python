# auth.py
import bcrypt
import getpass
from conexion import obtener_conexion

def login() -> str | None:
    print("=== Ingreso Seguro al Sistema ===")
    usuario = input("Usuario: ").strip()
    password = getpass.getpass("Contraseña: ").encode("utf-8")

    cnx = obtener_conexion()
    cur = cnx.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios WHERE username = %s", (usuario,))
    datos = cur.fetchone()
    cur.close()
    cnx.close()

    if datos and bcrypt.checkpw(password, datos["password_hash"].encode("utf-8")):
        print(f"Bienvenido, {usuario} (Rol: {datos['rol']})")
        return datos["rol"]
    print("Credenciales incorrectas.")
    return None


def crear_usuario_seguro():
    usuario = input("Nuevo usuario: ").strip()
    password = getpass.getpass("Contraseña: ").encode("utf-8")
    rol = input("Rol (Administrador, MandosMedios, Gerencia): ").strip()

    password_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode("utf-8")

    cnx = obtener_conexion()
    cur = cnx.cursor()
    try:
        cur.execute(
            "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s, %s, %s)",
            (usuario, password_hash, rol)
        )
        cnx.commit()
        print(f"Usuario '{usuario}' creado con éxito.")
    except mysql.connector.Error as err:
        print(f"Error al crear usuario: {err}")
    finally:
        cur.close()
        cnx.close()
