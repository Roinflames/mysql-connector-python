#
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='testdb'
)

cursor = conexion.cursor()

# Insertar un usuario
sql = """
INSERT INTO usuarios (username, password_hash, rol) 
VALUES (%s, %s, %s)
"""

valores = ("rodrigo", "123456", "Administrador")

cursor.execute(sql, valores)

# Confirmar cambios
conexion.commit()

print(f"Usuario insertado con ID: {cursor.lastrowid}")

# Cerrar recursos
cursor.close()
conexion.close()