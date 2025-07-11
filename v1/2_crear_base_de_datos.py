import mysql.connector
from mysql.connector import errorcode

# Configura tus credenciales
config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",  # Reemplaza por la clave que recuperaste
    "port": 3306,  # 👈 Puerto personalizado que elegiste
}

# Nombre de la base y tabla
nombre_base = "testdb"

# Conexión sin base aún, para crearla
try:
    conexion = mysql.connector.connect(**config)
    cursor = conexion.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_base}")
    print(f"✅ Base de datos '{nombre_base}' creada o ya existente.")
    cursor.close()
    conexion.close()
except mysql.connector.Error as err:
    print(f"❌ Error al crear la base de datos: {err}")
finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("🔒 Conexión cerrada.")
