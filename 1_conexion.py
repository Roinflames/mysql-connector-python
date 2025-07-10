# Conectar a una base de datos MySQL usando mysql-connector-python
import mysql.connector

# Datos de conexión
config = {
    'host': 'localhost',      # o la IP del servidor
    'user': 'root',
    'password': '123456',
    'database': 'testdb'
}

try:
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")