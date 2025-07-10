#
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Eliminar la tabla usuarios si existe
cursor.execute("DROP TABLE IF EXISTS usuarios")

conexion.commit()

print("Tabla 'usuarios' eliminada (si existía).")

cursor.close()
conexion.close()