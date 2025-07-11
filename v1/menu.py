import mysql.connector # Para conectar Python y BDD
import bcrypt # Para encriptar contraseñas
import getpass # Para ocultar la entrada de contraseñas

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='testdb'
    )

def login():
    print("=== Ingreso Seguro al Sistema ===")
    usuario = input("Usuario: ").strip()
    password = getpass.getpass("Contraseña: ").encode('utf-8')

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (usuario,))
    datos = cursor.fetchone()
    cursor.close()
    conexion.close()

    if datos and bcrypt.checkpw(password, datos["password_hash"].encode('utf-8')):
        print(f"Bienvenido, {usuario} (Rol: {datos['rol']})")
        return datos['rol']
    else:
        print("Credenciales incorrectas.")
        return None

def mostrar_menu(rol):
    while True:
        print("\n=== Menú Principal ===")
        print("1. Crear base de datos")
        print("2. Eliminar base de datos")
        print("3. Ver bases de datos")
        print("4. Crear tabla")
        print("5. Eliminar tabla")
        print("6. Insertar usuario")
        print("7. Consultar usuarios")
        print("8. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if rol != "Gerencia":
                print("No tiene permisos para crear bases de datos.")
                continue
            crear_base_datos()

        elif opcion == "2":
            if rol != "Gerencia":
                print("No tiene permisos para eliminar bases de datos.")
                continue
            eliminar_base_datos()

        elif opcion == "3":
            ver_bases_datos()

        elif opcion == "4":
            crear_tabla()

        elif opcion == "5":
            eliminar_tabla()

        elif opcion == "6":
            insertar_usuario()

        elif opcion == "7":
            consultar_usuarios()

        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# === Funciones placeholder ===

def crear_base_datos():
    print(">> [TODO] Crear base de datos")

def eliminar_base_datos():
    print(">> [TODO] Eliminar base de datos")

def ver_bases_datos():
    print(">> [TODO] Listar bases de datos")

def crear_tabla():
    print(">> [TODO] Crear tabla")

def eliminar_tabla():
    print(">> [TODO] Eliminar tabla")

def insertar_usuario():
    print(">> [TODO] Insertar usuario en tabla")

def consultar_usuarios():
    print(">> [TODO] Consultar usuarios desde tabla")

# === Crear usuario seguro solo una vez ===
def crear_usuario_seguro():
    usuario = input("Nuevo usuario: ").strip()
    password = getpass.getpass("Contraseña: ").encode('utf-8')
    rol = input("Rol (Administrador, MandosMedios, Gerencia): ").strip()

    password_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (username, password_hash, rol) VALUES (%s, %s, %s)",
            (usuario, password_hash, rol)
        )
        conexion.commit()
        print(f"Usuario '{usuario}' creado con éxito.")
    except mysql.connector.Error as err:
        print(f"Error al crear usuario: {err}")
    finally:
        cursor.close()
        conexion.close()

# === Programa Principal ===
if __name__ == "__main__":
    # Descomenta solo una vez para crear usuarios
    # crear_usuario_seguro()
    
    rol = login()
    if rol:
        mostrar_menu(rol)
